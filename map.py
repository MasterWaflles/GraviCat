import pygame

from objects.obj import Obj

from objects.player import Player

from objects.green_crocodile import GreenCrocodile
from objects.red_crocodile import RedCrocodile

from objects.blue_bird import BlueBird
from objects.orange_bird import OrangeBird

import config


class Map:
    def __init__(self, tile_map, *group):

        # Attributes for the dimensions of the blocks
        self.tile_width = config.TILE_SIZE
        self.tile_height = config.TILE_SIZE

        # Attribute for the map itself
        self.tile_map = tile_map

        # Stores width and height of the map
        self.dimensions = pygame.Vector2(len(tile_map[0]) * self.tile_width, len(tile_map) * self.tile_height)

        # Declare groups
        try:
            self.all_sprites = group[0]
        except IndexError:
            pass

        try:
            self.all_tiles = group[1]
        except IndexError:
            self.all_tiles = pygame.sprite.Group()

        try:
            self.all_enemies = group[2]
        except IndexError:
            self.all_enemies = pygame.sprite.Group()

        self.all_clouds = pygame.sprite.Group()
        self.all_trees = pygame.sprite.Group()

        self.player = 0

    # Method to create the blocks
    def generate_tile_map(self):
        # i represents the x position of a block
        for i in range(len(self.tile_map)):
            # j represents the y position of a block
            for j in range(len(self.tile_map[i])):
                character = self.tile_map[i][j]
                # If not empty space
                if character != ".":
                    # Creates player if character is A
                    if character == "A":
                        self.player = Player("sprites/cat/cat_idle.png", j * self.tile_width, i * self.tile_height, 90,
                                             105, self.all_tiles, self.all_enemies)

                        # Position the player in the midbottom of a tile
                        displace = self.align_object(self.player.rect.width, self.player.rect.height)
                        self.player.rect.x += displace[0]
                        self.player.rect.y += displace[1]

                    # Creates green crocodile if character is B or b
                    elif character == "B" or character == "b":
                        green_crocodile = GreenCrocodile("sprites/crocodile/walking_Gcrocodile0.png", j * self.tile_width,
                                i * self.tile_height, 108, 54, self.all_tiles, self.all_enemies)

                        # Position the enemy in the midbottom of a tile
                        displace = self.align_object(green_crocodile.rect.width, green_crocodile.rect.height)
                        green_crocodile.rect.x += displace[0]
                        green_crocodile.rect.y += displace[1]

                        # Make the enemy move right depending on the character
                        if character == "b":
                            green_crocodile.velocityX *= -1

                    # Creates red crocodile if character is C or c
                    elif character == "C" or character == "c":
                        red_crocodile = RedCrocodile("sprites/crocodile/walking_Rcrocodile0.png", j * self.tile_width,
                                i * self.tile_height, 108, 54, self.all_tiles, self.all_enemies)

                        # Position the enemy in the midbottom of a tile
                        displace = self.align_object(red_crocodile.rect.width, red_crocodile.rect.height)
                        red_crocodile.rect.x += displace[0]
                        red_crocodile.rect.y += displace[1]

                        # Make the enemy move right depending on the character
                        if character == "c":
                            red_crocodile.velocityX *= -1

                    # Creates blue bird if character is D or d
                    elif character == "D" or character == "d":
                        blue_bird = BlueBird("sprites/bird/Bbird_hitbox.png", j * self.tile_width,
                                i * self.tile_height, 78, 33, self.all_tiles, self.all_enemies)

                        # Position the bird in the midbottom of a tile
                        displace = self.align_object(blue_bird.rect.width, blue_bird.rect.height)
                        blue_bird.rect.x += displace[0]
                        blue_bird.rect.y += displace[1] * (1/2)

                        if character == "d":
                            blue_bird.velocityX *= -1

                    # Creates orange bird if character is O or I
                    elif character == "E" or character == "e":
                        orange_bird = OrangeBird("sprites/bird/Bbird_hitbox.png", j * self.tile_width,
                                i * self.tile_height, 78, 33, self.all_tiles, self.all_enemies)

                        # Position the bird in the midbottom of a tile
                        displace = self.align_object(orange_bird.rect.width, orange_bird.rect.height)
                        orange_bird.rect.x += displace[0]
                        orange_bird.rect.y += displace[1] * (1/2)

                        if character == "e":
                            orange_bird.velocityX *= -1

                    # Creates trees and align their midbottom with the tile midbottom
                    elif character == "F":
                        pine = Obj("sprites/pine.png", j * self.tile_width, i * self.tile_height, 228, 400,
                                   self.all_trees)
                        displace = self.align_object(pine.rect.width, pine.rect.height)
                        pine.rect.x += displace[0]

                    elif character == "G":

                        maple = Obj("sprites/tree.png", j * self.tile_width, i * self.tile_height, 204, 300,
                                    self.all_trees)

                        displace = self.align_object(maple.rect.width, maple.rect.height)
                        maple.rect.x += displace[0]

                    # Creates and align their middle with the tile middle
                    elif character == "H":

                        cloud = Obj("sprites/cloud.png", j * self.tile_width, i * self.tile_height, 220, 100,
                                    self.all_clouds)

                        displace = self.align_object(cloud.rect.width, cloud.rect.height)
                        cloud.rect.x += displace[0]
                        cloud.rect.y += displace[1] * (1/2)

                    # If is not E and F, it is a number so create platform
                    else:
                        if ord(character) < 48:
                            # Sprite number
                            num = ord(character) - 34
                            if num % 2 == 1:
                                width = 75
                                height = 51
                            else:
                                width = 51
                                height = 75

                            # Creates spike
                            spike = Obj("sprites/spike/spike" + str(num) + ".png", j * self.tile_width,
                                       i * self.tile_height, width, height, self.all_enemies)

                            displace = self.align_object(spike.rect.width, spike.rect.height)

                            # Moves the spike to the  correct position in the tile depending on the sprite
                            if num == 1:
                                spike.rect.x += displace[0]
                                spike.rect.y += displace[1]

                            if num == 2:
                                spike.rect.y += (1/2) * displace[1]

                            if num == 3:
                                spike.rect.x += displace[0]

                            if num == 4:
                                spike.rect.x += 2 * displace[0]
                                spike.rect.y += (1/2) * displace[1]

                        else:
                            # Creates tile
                            tile = Obj("sprites/platform/platform" + character + ".png", j * self.tile_width,
                                      i * self.tile_height, self.tile_width, self.tile_height, self.all_tiles)

        for tree in self.all_trees:
            for tile in self.all_tiles:
                while tree.rect.colliderect(tile):
                    tree.rect.y -= 1

        # Append groups to all_sprites in order
        self.all_sprites.add(self.all_clouds, self.all_trees)

        try:
            self.all_sprites.add(self.player)
        except AttributeError:
            pass

        for enemy in self.all_enemies:
            if enemy.__class__.__name__ == "BlueBird":
                self.all_sprites.add(enemy)

        for enemy in self.all_enemies:
            if enemy.__class__.__name__ == "OrangeBird":
                self.all_sprites.add(enemy)

        for enemy in self.all_enemies:
            if enemy.__class__.__name__ == "GreenCrocodile":
                self.all_sprites.add(enemy)

        for enemy in self.all_enemies:
            if enemy.__class__.__name__ == "RedCrocodile":
                self.all_sprites.add(enemy)

        for enemy in self.all_enemies:
            if enemy.__class__.__name__ == "Obj":
                self.all_sprites.add(enemy)

        self.all_sprites.add(self.all_tiles)

    def align_object(self, w, h):
        x = (self.tile_width - w) * (1/2)
        y = self.tile_height - h

        return x, y
