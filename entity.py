import pygame

from constants import *
from learner import BasicLearner


class BasicEntity(object):

    def __init__(self, left, top, width, height, learner=BasicLearner(), color=Colors.green):
        global ENTITY_ID
        self.id = ENTITY_ID
        ENTITY_ID += 1

        self.left, self.top, self.width, self.height = left, top, width, height
        self.color = color
        self.learner = learner

        self.rect = pygame.Rect(self.left, self.top, width, height)
        self.xspeed, self.yspeed = 0, 0

    def move(self, wall_collision=True):
        
        if wall_collision:
            # In case of collision with the wall
            if self.rect.left < 0 or self.rect.right > Screen.width:
                self.xspeed = -self.xspeed
            if self.rect.top < 0 or self.rect.bottom > Screen.height:
                self.yspeed = -self.yspeed

        self.rect.height = self.height
        self.rect.width = self.width
        self.rect = self.rect.move(self.xspeed, self.yspeed)

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
