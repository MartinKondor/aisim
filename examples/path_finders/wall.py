import numpy as np
from entity import BasicEntity
from constants import Colors
from entity_types import EntityType


class WallEntity(BasicEntity):

    def __init__(self, *args, **kwargs):
        super(WallEntity, self).__init__(*args, **kwargs)
        self.type = EntityType.WALL

    def perceive(self, entities):
        pass

    def behave(self, entities):
        pass
