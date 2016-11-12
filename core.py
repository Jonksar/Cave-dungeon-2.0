import pygame, sys
from constants import *
import player
import map_gen
import map_draw
from ObjectList import GameobjectListUpdater


# world coordinates of the top-left corner of the camera
cam_pos = [50, 50]

# an object to represent the player
player_obj = player.Player()

# set the player's location to x = 200; y = 200
# note that these are world coordinates not screen coordinates
player_obj.pos = [200, 200]

# a surface to draw the character and all it's related effects onto
character_surface = pygame.Surface(RESOLUTION, flags=pygame.SRCALPHA)


pygame.init()
window = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
ms = clock.tick(FPS_CAP)
current_fps = 1000//ms
default_font = pygame.font.Font(None, 26)

gameObjectListUpdater = GameobjectListUpdater(char_surface=character_surface, surface=window, player=player_obj, def_font=default_font)
# called when the window is closed
def game_quit():
    pygame.quit()  # close pygame window
    sys.exit()  # terminate the program from this line


# minu muudatus
# called every frame
def update():
    gameObjectListUpdater._update()

# called every frame after the update function
def draw(surface):
    gameObjectListUpdater._draw(surface=surface, current_fps=current_fps)


# called once when the game starts
def game_start():
    global ms, current_fps

    # game loop
    while True:
        for e in pygame.event.get():
            current_fps = 1000 // ms

            if e.type == pygame.QUIT:
                game_quit()

            elif e.type == pygame.KEYDOWN:
                print('PLAYER POSITION',
                      (player_obj.pos[0] + 0.5*TILE_SIZE)//TILE_SIZE,
                      (player_obj.pos[1] + 0.5*TILE_SIZE)//TILE_SIZE,
                      player_obj.pos)

                if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                    player_obj.vel[0] = -player_obj.speed

                elif e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                    player_obj.vel[0] = player_obj.speed

                elif e.key == pygame.K_w or e.key == pygame.K_UP:
                    player_obj.vel[1] = -player_obj.speed

                elif e.key == pygame.K_s or e.key == pygame.K_DOWN:
                    player_obj.vel[1] = player_obj.speed

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                    player_obj.vel[0] = 0

                elif e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                    player_obj.vel[0] = 0

                elif e.key == pygame.K_w or e.key == pygame.K_UP:
                    player_obj.vel[1] = 0

                elif e.key == pygame.K_s or e.key == pygame.K_DOWN:
                    player_obj.vel[1] = 0

        update()
        draw(window)

        pygame.display.flip()
        ms = clock.tick(FPS_CAP)
