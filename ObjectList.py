import pygame, sys
from constants import *
import player
import map_gen
import map_draw
import pygame


# called every frame after the update function
class Map:
    def __init__(self):
        self.map_data = map_gen.CellularAutomaton(size=128)
        self.map_data()

    def draw(self, surface, cam_pos):
        return map_draw.map_draw(surface, self.map_data, cam_pos)


class GameobjectListUpdater:
    def __init__(self, *args, char_surface=None, surface=None, player=player.Player(), map=Map(), def_font=None):
        self.obj_list = list(args)
        self.gameobj_dict = {'map': map,
                             'obj_list': self.obj_list,
                             'player': player,
                             'char_surface': char_surface,
                             'surface': surface}

        self.obj_list.append(player)
        self.player = self.gameobj_dict['player']
        self.cam_pos = [50, 50]
        self.def_font = def_font
        self.map_rect_list = [pygame.Rect(0,0,0,0)]

    def iter(self):
        self._update()
        self._draw()

    def _draw(self, surface, current_fps):
        # Reset the surface
        self.gameobj_dict['char_surface'].fill([0, 0, 0, 0])
        self.gameobj_dict['surface'].fill([0, 0, 0, 0])

        # Draw the map
        self.map_rect_list = self.gameobj_dict['map'].draw(self.gameobj_dict['surface'], self.cam_pos)

        for item in self.obj_list:
            item.draw(self.gameobj_dict['char_surface'], self.cam_pos)

        surface.blit(self.gameobj_dict['char_surface'], [0, 0])

        # FPS
        fps_surface = self.def_font.render(str(current_fps), False, (255, 255, 255))
        surface.blit(fps_surface, [5, 5])

    def _update(self):
        self.player.update(self.map_rect_list)

        # update camera position
        # cam_pos_center = [cam_pos[0] + RESOLUTION[0]/2, cam_pos[1] + RESOLUTION[1]/2]
        player_pos_center = self.player.rect.center
        self.cam_pos = [player_pos_center[0] - RESOLUTION[0] / 2, player_pos_center[1] - RESOLUTION[1] / 2]

    def add(self, *args):
        self.obj_list += list(args)

    def remove(self, *args):
        for item in args:
            self.obj_list.remove(item)

