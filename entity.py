import pygame

import copy
from constants import *
from learner import BasicLearner


class BasicEntity(object):

    """
    :left: int, the x leftmost position of the entity
    :top: int, the y topmost position of the entity
    :width: int, width of the entity
    :height: int, height of the entity
    :learner: BasicLearner, learner object to get behaviour from
    :color: (int, int, int), the color of the entity
    :outline: bool, if true the object will have an outline
    :outline_size: int, size of the outline
    :inner_color: (int, int, int), color of the inner part of the outlined object
    :skip_collision_on_sides: bools [top, right, bottom, left], each bool represents
        a side of the entity, where if the bool is true like [True, False, False, False]
        this means that the entity will not check for collision from the top
    :no_outline_on_sides: bools [top, right, bottom, left], same way as with the collison 
        argument, [False, True, False, False] means that there will be no outline in the 
        right side of the entity
    """
    def __init__(self, left, top, width, height, learner=BasicLearner(), color=Colors.green,
                    outline=False, outline_size=1, inner_color=None,
                    skip_collision_on_sides=[False, False, False, False],
                    no_outline_on_sides=[False, False, False, False]):
        
        global ENTITY_ID
        self.id = ENTITY_ID
        ENTITY_ID += 1

        self.left, self.top, self.width, self.height = left, top, width, height
        self.color = copy.deepcopy(color)
        self.learner = learner
        self.marked_as_deletable = False  # When true, it can be deleted from the array
        self.is_outlined = outline

        self.scos = skip_collision_on_sides
        self.noos = no_outline_on_sides

        self.rect = pygame.Rect(self.left, self.top, width, height)
        if self.is_outlined:
            self.inner_rect = pygame.Rect(
                self.left + outline_size//2,
                self.top + outline_size//2,
                width - outline_size*(0 if self.noos[1] else 1),
                height - outline_size*(0 if self.noos[2] else 1)
            )
            
            # Outline on top
            if self.noos[0]:
                self.inner_rect.top = self.top - outline_size//2
                self.inner_rect.height += outline_size

            # Outline on left
            if self.noos[3]:
                self.inner_rect.left = self.left - outline_size//2
                self.inner_rect.width += outline_size

            self.inner_color = inner_color

        self.xspeed, self.yspeed = 0, 0

    def move(self, wall_collision=True):
        if wall_collision:

            # In case of collision with the wall
            if self.rect.left < self.width//2 or self.rect.right > Screen.width - self.width//2:
                self.xspeed = 0
            if self.rect.top + self.yspeed < self.height//2 or self.rect.bottom + self.yspeed > Screen.height - self.height//2:
                self.yspeed = 0

        self.rect.height = self.height
        self.rect.width = self.width

        self.rect = self.rect.move(self.xspeed, self.yspeed)
        if self.is_outlined:
            self.inner_rect = self.inner_rect.move(self.xspeed, self.yspeed)

    def get_size(self):
        return self.width * self.height

    def in_collision(self, entity):
        if self.is_outlined:
            if self.inner_rect.colliderect(entity.rect):
                return False
        elif entity.is_outlined:
            if entity.inner_rect.colliderect(self.rect):
                return False
        return self.rect.colliderect(entity.rect)

    def getpos(self):
        return [self.rect.left, self.rect.top]

    """
    Learn, note the positions of objects
    """
    def perceive(self, entities):
        pass

    """
    Move, according to what we precieve
    """
    def behave(self, entities):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.is_outlined:
            pygame.draw.rect(screen, self.inner_color if self.inner_color is not None else Screen.bg_color, self.inner_rect)
