import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import numpy as np
from constants import Colors, Screen
from graphics import start_graphics

from cell import CellEntity


"""
Runs only once at the begining.
"""
def on_load():
    np.random.seed(0)
    Screen.set_size(1280, 720)
    choosen_x, choosen_y = [], []

    for i in range(50):
        x, y = np.random.randint(11, Screen.width), np.random.randint(20, Screen.height - 20)
        while x in choosen_x and y in choosen_y:
            x, y = np.random.randint(11, Screen.width), np.random.randint(20, Screen.height - 20)

        choosen_x.append(x)
        choosen_y.append(y)
        Screen.entities.append(CellEntity(x, y, 10, 10, color=Colors.red if i%2==0 else Colors.yellow))


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
