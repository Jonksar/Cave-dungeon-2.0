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

    for y, j in enumerate(map_subsection):
        for x, i in enumerate(j):
            if i == 1:
                surface.fill(TILE_COLOR,
                             [x*TILE_SIZE - cam_offset_x,
                              y*TILE_SIZE - cam_offset_y,
                              TILE_SIZE,
                              TILE_SIZE])


def map_collide(player_rect, map_data, cam_pos):
    tiles_x = RESOLUTION[0] // TILE_SIZE + 1
    tiles_y = RESOLUTION[1] // TILE_SIZE + 1

    cam_offset_x = (cam_pos[0] % TILE_SIZE)
    cam_offset_y = (cam_pos[1] % TILE_SIZE)

    tile_start_x = int((cam_pos[0]) // TILE_SIZE)
    tile_start_y = int((cam_pos[1]) // TILE_SIZE)

    map_coords = list(product(list(range(tile_start_x, tiles_x + tile_start_x)), list(range(tile_start_y, tiles_y + tile_start_y))))

    collider_list = []

    for i in map_coords:
        if map_data.map[i[0]][i[1]] == 1:
            collider_list.append(pygame.Rect([i[0] * TILE_SIZE, i[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE]))

    index = player_rect.collidelist(collider_list)

    if index != -1:
        return collider_list[index]

    else:
        return None
