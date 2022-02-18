import numpy as np
from entity import BasicEntity
from constants import Colors
from entity_types import EntityType


class GoalEntity(BasicEntity):

    def __init__(self, *args, **kwargs):
        super(GoalEntity, self).__init__(*args, **kwargs)
        self.type = EntityType.GOAL

    def perceive(self, entities):
        pass

    def behave(self, entities):
        pass
