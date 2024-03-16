import pygame

import config
from control import Control


# Initiate pygame
pygame.init()

# Sets the resolution and removes the borders
window = pygame.display.set_mode([config.WIDTH, config.HEIGHT], pygame.NOFRAME)

# Instantiate level
control = Control(window)

# Creates variable for the fps
fps = pygame.time.Clock()

loop = True

while loop:
    # Defines the fps as 40
    fps.tick(config.FPS)

    # Update level
    control.update()

    # Checks for inputs
    for event in pygame.event.get():
        # Provides input for player if alive and in game
        if control.part == 2:
            if control.game.player.alive:
                control.game.player.event(event)

        control.event(event)

        # Checks if the user tried to quit the game
        if event.type == pygame.QUIT:
            loop = False

    # Updates window
    pygame.display.update()

