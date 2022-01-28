import pygame

from constants import Screen, Colors
from entity import BasicEntity


"""
Gets event functions as parameters.
"""
def start_graphics(on_load=lambda:None, on_behave=lambda:None, on_perceive=lambda:None):
    pygame.init()
    on_load()
    is_running = True
    screen = pygame.display.set_mode(Screen.size)
    clock = pygame.time.Clock()

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        # Fill the screen
        screen.fill(Colors.black)

        for entity in Screen.entities:
            if entity.marked_as_deletable:
                continue

            # Behave before getting drawn out
            entity.behave(Screen.entities)
            pygame.draw.rect(screen, entity.color, entity.rect)
            on_behave()

        # Perceive after drawing everything
        for entity in Screen.entities:
            if entity.marked_as_deletable:
                continue

            entity.perceive(Screen.entities)
            on_perceive()

        # FPS lock
        clock.tick(Screen.FPS)
        pygame.display.flip()


    pygame.quit()
