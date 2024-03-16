import pygame

import config


class Camera:

    # Receives the group of all sprites, player position and window
    def __init__(self, sprites, pos, dimensions, player, window, screen_obj):
        self.width = config.WIDTH
        self.height = config.HEIGHT

        # Vector defining where all the sprites should move
        self.offset = pygame.Vector2(pos)
        self.offset.x -= self.width * (1/2)
        self.offset.y -= self.height * (1/2)

        self.offsetX_change = 0

        self.sprites = sprites
        self.window = window

        self.level_dimensions = dimensions

        self.left_extremity = self.width * (2/5)
        self.right_extremity = self.width * (3/5)

        self.repos = 0

        self.mov_right = False
        self.mov_left = False

        self.player = player
        self.screen = screen_obj

    def camera_align(self, pos, dir):
        '''print(pos[0] - self.offset.x)
        if dir < 0:
            self.mov_right = False
            self.mov_left = True
        if dir > 0:
            self.mov_right = True
            self.mov_left = False

        if self.mov_left:
            if self.repos < self.width * (1/5):
                self.repos += 6
            else:
                self.mov_left = False
                self.repos = self.width * (1/5)

        if self.mov_right:
            if self.repos > 0:
                self.repos -= 6
            else:
                self.mov_right = False
                self.repos = 0

        if pos[0] < self.width * (2/5):
            self.mov_left = False
            self.repos = 0

        if pos[0] > self.level_dimensions.x - self.width * (2/5):
            self.mov_right = False
            self.repos = self.width * (1/5)'''

        self.offset.x = pos[0] - self.width * (1/2)

        self.offset.y = pos[1] - self.height * (1/2)

        # Aligning Camera so it does not go out of borders
        if self.offset.x < 0:
            self.offset.x = 0
        elif self.offset.x > self.level_dimensions.x - self.width:
            self.offset.x = self.level_dimensions.x - self.width

        if self.offset.y < 0:
            self.offset.y = 0
        elif self.offset.y > self.level_dimensions.y - self.height:
            self.offset.y = self.level_dimensions.y - self.height

    def screen_pos(self, pos):
        return pos - self.offset.x

    def draw(self):
        for sprite in self.sprites:
            try:
                offset = sprite.image_rect.topleft - self.offset
            except AttributeError:
                offset = sprite.rect.topleft - self.offset
            if sprite.rect.colliderect(self.screen):
                self.window.blit(sprite.image, offset)



