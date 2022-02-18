import numpy as np
from entity import BasicEntity
from constants import Colors


class CellEntity(BasicEntity):

    def __init__(self, *args, **kwargs):
        super(CellEntity, self).__init__(*args, **kwargs)

    def perceive(self, entities):
        for entity in entities:
            if entity.marked_as_deletable or entity.id == self.id:
                continue

            if self.in_collision(entity):
                if entity.get_size() >= self.get_size():
                    self.marked_as_deletable = True
                    entity.width += 10 + np.random.randint(-5, 5)
                    entity.height += 10 + np.random.randint(-5, 5)
                else:
                    entity.marked_as_deletable = True
                    self.width += 10 + np.random.randint(-5, 5)
                    self.height += 10 + np.random.randint(-5, 5)
                break

    def behave(self, entities):
        self.xspeed = np.random.randint(-10, 10)
        self.yspeed = np.random.randint(-10, 10)
        self.move()
