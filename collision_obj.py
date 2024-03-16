import math

from objects.animated_obj import AnimatedObj


class CollisionObj(AnimatedObj):

    def __init__(self, image, x, y, w, h, tiles, *groups):
        super().__init__(image, x, y, w, h, *groups)

        # Attribute for the tiles' and enemies' group
        self.tiles = tiles

        # List to keep track of the collisions
        self.collisions = [False, False, False, False]

    def horizontal_collision(self):
        # Resets collisions attributes
        self.collisions[2] = False
        self.collisions[3] = False

        # Checks all the tiles
        for obj in self.tiles:
            # If the player is colliding with one of the tiles
            if self.rect.colliderect(obj.rect):
                # If player is moving right
                if self.velocityX > 0:
                    # Teleports right of the player to the left of the tile and sets x velocity to 0
                    self.rect.right = obj.rect.left
                    self.velocityX = 0
                    self.collisions[2] = True
                # If player is moving left
                elif self.velocityX < 0:
                    # Teleports left of the player to the right of the tile and sets x velocity to 0
                    self.rect.left = obj.rect.right
                    self.velocityX = 0
                    self.collisions[3] = True

    def vertical_collision(self):
        # Resets collisions attributes
        self.collisions[0] = False
        self.collisions[1] = False

        # Moves player by 1 pixel so that being adjacent to the platform counts as a collision
        displace = self.gravity/(math.fabs(self.gravity))
        if self.velocityY * self.gravity > 0:
            self.rect.y += displace

        # Check all the tiles
        for obj in self.tiles:
            # If the player is colliding with one of the tiles
            if self.rect.colliderect(obj.rect):
                # If player is moving down
                if self.velocityY > 0:
                    # Teleports bottom of the player to the top of the tile
                    self.rect.bottom = obj.rect.top
                    self.collisions[0] = True
                    # Sets the y velocity to 1 if moving in the direction of gravity
                    if self.gravity > 0:
                        self.velocityY = 0
                    # Sets the y velocity to 0 and stops the jump if moving in the opposite direction of gravity
                    else:
                        self.velocityY = 0
                        self.jumping = False

                # If player is moving up
                elif self.velocityY < 0:
                    # Teleports top of the player to the bottom of the tile
                    self.rect.top = obj.rect.bottom
                    self.collisions[1] = True
                    # Sets the y velocity to -1 if moving in the direction of gravity
                    if self.gravity < 0:
                        self.velocityY = 0
                    # Sets the y velocity to 0 and stops the jump if moving in the opposite direction of gravity
                    else:
                        self.velocityY = 0
                        self.jumping = False

        # Makes gravity inversion impossible when the player is standing in the ground
        if not self.collisions[0] and not self.collisions[1]:
            if self.velocityY * self.gravity > 0:
                self.rect.y -= displace
