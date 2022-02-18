
# First entity ID to give, with each 
# entity created, it will increase by one
ENTITY_ID = 0 


class Colors:
    black = [0, 0, 0]
    white = [255, 255, 255]
    red = [255, 0, 0]
    green = [0, 255, 0]
    blue = [0, 0, 255]
    yellow = [255, 255, 0]
    orange = [255, 165, 0]
    purple = [128, 0, 128]

    king_blue = [65, 105, 225]
    emperor_red = [78, 13, 20]

    def combine(c1, c2):
        return [(c1[0]+c2[0])/2, (c1[1]+c2[1])/2, (c1[2]+c2[2])/2]


class Screen:
    width = 350
    height = 350
    size = (width, height,)
    center = (width / 2, height / 2,)
    entities = []
    FPS = 24
    bg_color = Colors.black

    def set_size(width, height):
        Screen.width = width
        Screen.height = height
        Screen.size = (width, height,)
