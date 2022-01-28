import pygame

import copy
from constants import *
from learner import BasicLearner


class BasicEntity(object):

    def __init__(self, left, top, width, height, learner=BasicLearner(), color=Colors.green):
        global ENTITY_ID
        self.id = ENTITY_ID
        ENTITY_ID += 1

        self.left, self.top, self.width, self.height = left, top, width, height
        self.color = copy.deepcopy(color)
        self.learner = learner
        self.marked_as_deletable = False  # When true, it can be deleted from the array

        self.rect = pygame.Rect(self.left, self.top, width, height)
        self.xspeed, self.yspeed = 0, 0

    def move(self, wall_collision=True):
        if wall_collision:
            # In case of collision with the wall
            if self.rect.left < self.width//2 or self.rect.right > Screen.width - self.width//2:
                self.xspeed = 0
            if self.rect.top + self.yspeed < self.height//2 or self.rect.bottom + self.yspeed > Screen.height - self.height//2:
                self.yspeed = 0

            """
            if self.rect.left < self.width//2:
                self.rect.left = 0
                self.xspeed = 0            
            if self.rect.right > Screen.width - self.width//2:
                self.rect.right = Screen.width
                self.xspeed = 0
            if self.rect.top < self.height//2:
                self.rect.top = 0
                self.yspeed = 0
            if self.rect.bottom + self.yspeed > Screen.height - self.height//2:
                self.rect.bottom = Screen.height
                self.yspeed = 0
            """

        self.rect.height = self.height
        self.rect.width = self.width
        self.rect = self.rect.move(self.xspeed, self.yspeed)

    def get_size(self):
        return self.width * self.height

    def in_collision(self, entity):
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
