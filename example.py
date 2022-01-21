import numpy as np
from constants import *
from graphics import start_graphics

from entity import BasicEntity


class ExampleEntity(BasicEntity):

    def __init__(self, *args, **kwargs):
        super(ExampleEntity, self).__init__(*args, **kwargs)

    def perceive(self, entities):
        for entity in entities:
            if entity.id == self.id:
                continue

            if entity.getpos()[0] < self.getpos()[0]:
                entity.width += 0.5
                entity.height += 0.5

    def behave(self, entities):
        self.xspeed, self.yspeed = 5*np.random.random(), 5*np.random.random()
        self.move()


"""
Runs only once at the begining.
"""
def on_load():
    np.random.seed(0)
    Screen.entities.append(ExampleEntity(50, 50, 10, 10, color=Colors.green))
    Screen.entities.append(ExampleEntity(10, 10, 10, 10, color=Colors.red))


"""
Runs in each behave loop.
"""
def on_behave():
    pass


"""
Runs in each perceive loop.
"""
def on_perceive():
    pass


if __name__ == "__main__":
    start_graphics(on_load=on_load, on_behave=on_behave, on_perceive=on_perceive)
