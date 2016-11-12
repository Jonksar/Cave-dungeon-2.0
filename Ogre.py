import pygame
from constants import *


class Ogre:
    def __init__(self):
        # player's position in world coordinates
        self.pos = [100, 100]

        # player's velocity
        self.vel = [0, 0]

        # the speed at which the player can move
        self.speed = 10

        # a rectangle object for collision detection
        self.rect = pygame.Rect(self.pos + [TILE_SIZE, TILE_SIZE])

        # the color of the player currently
        self.color = [255, 105, 100]

    # called every frame
    def update(self):
        # when moving diagonally the velocity must be changed so that the player wouldn't move faster
        if abs(self.vel[0]) == self.speed and abs(self.vel[1]) == self.speed:
            self.vel[0] /= 1.414
            self.vel[1] /= 1.414

        # update the character position
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        # update the character rectangle
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    # called every frame after the update function
    def draw(self, surface, cam_pos):
        # subtracting the camera pos from the player pos gives the players position relative to the camera
        # aka the players position on the screen
        pos_on_screen = [self.pos[0] - cam_pos[0], self.pos[1] - cam_pos[1]]

        # draw a polygon with three points on the screen
        # all three points must be screen coordinate pairs [x, y]
        point1 = [pos_on_screen[0] + 0.5*TILE_SIZE, pos_on_screen[1] - 0.5 * TILE_SIZE]
        point2 = [pos_on_screen[0] + 2, pos_on_screen[1] + TILE_SIZE]
        point3 = [pos_on_screen[0] + TILE_SIZE - 2, pos_on_screen[1] + TILE_SIZE]

        pygame.draw.polygon(surface, self.color, [point1, point2, point3], 3)

