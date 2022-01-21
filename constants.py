
# First entity ID to give, with each 
# entity created, it will increase by one
ENTITY_ID = 0  


class Screen:
    width = 350
    height = 350
    size = (width, height,)
    center = (width / 2, height / 2,)
    entities = []
    FPS = 24


class Colors:
    black = 0, 0, 0
    white = 255, 255, 255
    red = 255, 0, 0
    green = 0, 255, 0
    blue = 0, 0, 255
