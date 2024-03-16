import config
from state_creator import StateCreator


class StateManager:
    def __init__(self, screen):

        self.screen = screen
        # Index of the first state
        self.state_num = 0
        # Creates initial state
        self.state = StateCreator(config.LEVEL1[self.state_num], self.screen)
        self.player = self.state.player

    def verify(self):
        # Increments the index of the state if it needs to be changed, it also updates the player
        if self.state.next_state:
            self.state_num += 1
            self.state = StateCreator(config.LEVEL1[self.state_num], self.screen)
            self.player = self.state.player

    def update(self):
        self.state.update()

