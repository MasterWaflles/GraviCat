import pygame


class Text:

    def __init__(self, size, text):
        # Creates text
        self.text = text
        self.font = pygame.font.Font("C:\\Users\\julia\\PycharmProjects\\GraviCat\\myfont.ttf", size)

        self.render = self.font.render(text, False, (250, 250, 250))
        self.render_yellow = self.font.render(text, False, (255, 240, 0))

        self.rect = self.render.get_rect()

    # Draws text in screen
    def draw(self, render, window, x, y):
        window.blit(render, (x, y))

    # Returns width and height of text
    def get_size(self):
        text_width, text_height = self.font.size(self.text)
        return text_width, text_height

