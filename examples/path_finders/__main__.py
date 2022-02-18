"""
Goal for entities (king_blue) to not collide with the walls
(black) and to arrive at the goal (emperor_red)
"""
import os
import sys

from pygame import Color
sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import numpy as np
from constants import Colors, Screen
from graphics import start_graphics

from cell import CellEntity
from wall import WallEntity
from goal import GoalEntity


"""
Runs only once at the begining.
"""
def on_load():
    np.random.seed(0)
    Screen.set_size(1280, 720)
    Screen.bg_color = Colors.white

    Screen.entities.extend([
        WallEntity(
            25, 25, 250, 100, color=Colors.black,
            outline=True, outline_size=10,
            skip_collision_on_sides=[False, True, False, False],
            no_outline_on_sides=[False, True, False, False]
        ),
        WallEntity(
            250 + 25, 25, 100, 250, color=Colors.black,
            outline=True, outline_size=10,
            skip_collision_on_sides=[False, False, True, True],
            no_outline_on_sides=[False, False, True, True]
        ),
        WallEntity(
            250 + 25, 250 + 25, 250, 100, color=Colors.black,
            outline=True, outline_size=10,
            skip_collision_on_sides=[True, False, False, False],
            no_outline_on_sides=[True, False, False, False]
        ),
        GoalEntity(450 - 25//2, 200 - 25//2, 25, 25, color=Colors.emperor_red),
        CellEntity(25 + 10, 25 + 10, 10, 10, color=Colors.king_blue)
    ])

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
