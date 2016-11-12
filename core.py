import pygame, sys
from constants import *
import player
import map_gen
import map_draw

# world coordinates of the top-left corner of the camera
cam_pos = [50, 50]

# an object to represent the player
player_obj = player.Player()

# set the player's location to x = 200; y = 200
# note that these are world coordinates not screen coordinates
player_obj.pos = [200, 200]

# a surface to draw the character and all it's related effects onto
character_surface = pygame.Surface(RESOLUTION, flags=pygame.SRCALPHA)

map_data = map_gen.CellularAutomaton(size=128)
map_data()

pygame.init()
window = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
ms = clock.tick(FPS_CAP)
current_fps = 1000//ms

default_font = pygame.font.Font(None, 26)


# called when the window is closed
def game_quit():
    pygame.quit()  # close pygame window
    sys.exit()  # terminate the program from this line


# minu muudatus
# called every frame
def update():
    global cam_pos

    collison = map_draw.map_collide(player_obj.rect, map_data, cam_pos)
    if collison:
        print(collison.x, collison.y)

    player_obj.update()

    # update camera position
    # cam_pos_center = [cam_pos[0] + RESOLUTION[0]/2, cam_pos[1] + RESOLUTION[1]/2]
    player_pos_center = player_obj.rect.center
    cam_pos = [player_pos_center[0] - RESOLUTION[0]/2, player_pos_center[1] - RESOLUTION[1]/2]


# called every frame after the update function
def draw(surface):
    surface.fill([0, 0, 0])

    map_draw.map_draw(surface, map_data, cam_pos)

    surface.fill(TILE_COLOR, [0, 0, RESOLUTION[0], TILE_SIZE])
    surface.fill(TILE_COLOR, [0, 0, TILE_SIZE, RESOLUTION[1]])
    surface.fill(TILE_COLOR, [RESOLUTION[0]-TILE_SIZE, 0, TILE_SIZE, RESOLUTION[1]])
    surface.fill(TILE_COLOR, [0, RESOLUTION[1]-TILE_SIZE, RESOLUTION[0], TILE_SIZE])

    character_surface.fill([0, 0, 0, 0])
    player_obj.draw(character_surface, cam_pos)
    surface.blit(character_surface, [0, 0])

    fps_surface = default_font.render(str(current_fps), False, (255, 255, 255))
    surface.blit(fps_surface, [5, 5])


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
