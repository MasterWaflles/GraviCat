import pygame


from state_manager import StateManager
from main_menu import MainMenu


# Class to manage the parts of the game
class Control:

    def __init__(self, window):

        self.window = window

        # Instantiates the parts
        self.game = StateManager(self.window)
        self.menu = MainMenu(self.window)

        self.part = 1

    # Updates current part
    def update(self):
        if self.part == 1:
            #self.menu.colour()
            self.menu.draw()
        if self.part == 2:
            self.game.update()
            self.game.verify()

    # Check if the user entered an input to change the part
    def event(self, event):
        if self.part == 1:
            # Starts the game if the user pressed the play button with the mouse
            mpos = pygame.mouse.get_pos()
            if self.menu.play.rect.collidepoint(mpos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.part = 2
