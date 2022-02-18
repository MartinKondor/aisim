import numpy as np
from entity import BasicEntity
from constants import Colors
from entity_types import EntityType


class CellEntity(BasicEntity):

    def __init__(self, *args, **kwargs):
        super(CellEntity, self).__init__(*args, **kwargs)
        self.type = EntityType.CELL

    def perceive(self, entities):
        for entity in entities:
            if entity.marked_as_deletable or entity.id == self.id:
                continue

            if self.in_collision(entity) and entity.type == EntityType.WALL:
                self.marked_as_deletable = True

    def behave(self, entities):
        """
        self.xspeed = np.random.randint(-10, 10)
        self.yspeed = np.random.randint(-10, 10)
        self.move()
        """
