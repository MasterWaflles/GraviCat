import pygame

from map import Map
from camera import Camera


class StateCreator:

    def __init__(self, tile_map, window):
        # Screen rectangle
        self.screen = pygame.Rect(0, 0, 1280, 720)
        self.window = window

        # Creates groups
        self.all_sprites = pygame.sprite.Group()
        self.all_tiles = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()

        # Generated the level
        self.map = Map(tile_map, self.all_sprites, self.all_tiles, self.all_enemies)
        self.map.generate_tile_map()

        self.player = self.map.player

        # Generates camera
        self.camera = Camera(self.all_sprites, self.player.rect.center, self.map.dimensions, self.player, self.window,
                             self.screen)

        self.next_state = False

    def update(self):
        # Updates screen position
        self.screen.x = self.camera.offset.x
        self.screen.y = self.camera.offset.y

        # If the player is off the map
        if self.player.rect.bottom < 0 or self.player.rect.y > self.map.dimensions.y:
            self.player.alive = False
            # Sets player velocity to 0, so it doesn't come back dead from a hole
            self.player.velocityY = 0

        # Changes state if player reached the end of the level
        if self.player.rect.x > self.map.dimensions.x and self.player.alive:
            self.next_state = True

        # Calls the update method of every enemy alive
        for enemy in self.all_enemies:
            try:
                enemy.set_gravity(self.player.gravity)
            # If the object has no set_gravity method do nothing
            except AttributeError:
                pass

            try:
                enemy.generate(self.screen)
            # If the object has no generate method do nothing
            except AttributeError:
                pass
            else:
                if enemy.alive:
                    enemy.update()

            if enemy.rect.bottom < 0 or enemy.rect.y > self.map.dimensions.y:
                enemy.alive = False

        self.player.update()
        self.camera.camera_align(self.player.rect.center, self.player.velocityX)
        self.window.fill((153, 204, 255))
        self.camera.draw()

        # If dead, sets player horizontal direction to 0 so that it decelerates.
        if not self.player.alive:
            self.player.dx = 0
