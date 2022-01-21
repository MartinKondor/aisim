from constants import *
from graphics import start_graphics


"""
Runs only once at the begining.
"""
def on_load():
    pass


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
