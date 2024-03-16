import pygame

from text import Text
from map import Map

import config


class MainMenu:

    def __init__(self, window):
        self.window = window

        self.all_sprites = pygame.sprite.Group()
        # Creates a text message
        self.play = Text(80, "PLAY")

        self.texts = [self.play]


    # Draws all elements in the screen and update their positions
    def draw(self):
        self.window.fill((153, 204, 255))

        self.all_sprites.draw(self.window)

        for text in self.texts:
            x = 640 - text.get_size()[0] / 2
            y = self.texts.index(text) * 150 + 100

            text.rect.x = x
            text.rect.y = y

            mpos = pygame.mouse.get_pos()
            if text.rect.collidepoint(mpos):
                text.draw(text.render_yellow, self.window, x, y)
            if not text.rect.collidepoint(mpos):
                text.draw(text.render, self.window, x, y)
