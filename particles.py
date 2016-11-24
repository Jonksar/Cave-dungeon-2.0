import pygame
from Timer import Timer
from Buff import interpolate


class Particle:
    def __init__(self, pos, vel, buff, duration, start_radius):
        self.timer = Timer()
        self.pos = pos
        self.vel = vel

        self.start_radius = start_radius
        self.cur_radius = start_radius
        self.end_radius = 10 * start_radius

        self.buff = buff
        self.duration = duration
        self.dead = False

    def update(self, collide_list):
        self.buff.update()

        if not self.collide(collide_list, self.vel[0], 0):
            self.pos[0] += self.vel[0]

        else:
            self.vel[0] *= -1

        if not self.collide(collide_list, 0, self.vel[1]):
            self.pos[1] += self.vel[1]

        else:
            self.vel[1] *= -1

        self.pos[0] = self.pos[0]
        self.pos[1] = self.pos[1]

        self.cur_radius = interpolate(self.start_radius, self.end_radius, self.timer.time_since_start() / self.duration)

        if self.timer.time_since_start() >= self.duration:
            self.dead = True

    def draw(self, screen, cam_pos):
        pygame.draw.circle(screen, self.buff.cur_color, [int(self.pos[0]-cam_pos[0]), int(self.pos[1]-cam_pos[1])], self.cur_radius)

    def collide(self, collide_list, dx, dy):
        pos = [self.pos[0] + dx, self.pos[1] + dy]

        for i in collide_list:
            if i.collidepoint(pos):
                return True

        return False
