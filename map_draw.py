import pygame
from constants import *
from itertools import product


def map_draw(surface, map_data, cam_pos):

    tiles_x = RESOLUTION[0] // TILE_SIZE + 1
    tiles_y = RESOLUTION[1] // TILE_SIZE + 1

    cam_offset_x = (cam_pos[0] % TILE_SIZE)
    cam_offset_y = (cam_pos[1] % TILE_SIZE)

    tile_start_x = int((cam_pos[0]) // TILE_SIZE)
    tile_start_y = int((cam_pos[1]) // TILE_SIZE)

    map_subsection = [map_data.return_value(tile_start_x, tile_start_x+tiles_x, j)
                      for j in range(tile_start_y, tile_start_y + tiles_y)]

    rect_list = []

    for y, j in enumerate(map_subsection):
        for x, i in enumerate(j):
            if i == 1:
                rect = pygame.Rect([x*TILE_SIZE - cam_offset_x,
                                    y*TILE_SIZE - cam_offset_y,
                                    TILE_SIZE,
                                    TILE_SIZE])

                pygame.draw.rect(surface, TILE_COLOR, rect)
                rect.x += cam_pos[0]
                rect.y += cam_pos[1]
                rect_list.append(rect)

    return rect_list