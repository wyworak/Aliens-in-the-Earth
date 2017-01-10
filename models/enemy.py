# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *
from files import constants as c
from models import entity, exit_block, sounds

spritesheet = pygame.image.load("resources/graphics/enemy.png")

sprite_frame = Surface((c.ENEMY_SPRITE_WIDTH, c.ENEMY_SPRITE_WIDTH), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (0, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.ENEMY_WIDTH, c.ENEMY_HEIGHT))
enemy_walk_1 = sprite_frame

sprite_frame = Surface((c.ENEMY_SPRITE_WIDTH, c.ENEMY_SPRITE_WIDTH), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-32, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.ENEMY_WIDTH, c.ENEMY_HEIGHT))
enemy_walk_2 = sprite_frame

sprite_frame = Surface((c.ENEMY_SPRITE_WIDTH, c.ENEMY_SPRITE_WIDTH), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-64, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.ENEMY_WIDTH, c.ENEMY_HEIGHT))
enemy_flat = sprite_frame

class Enemy(entity.Entity):

    __counter = 0

    def __init__(self, x, y):
        entity.Entity.__init__(self)
        self.x_vel = -1
        self.y_vel = 0
        self.on_ground = False
        self.destroyed = False
        self.counter = 0
        self.image = enemy_walk_1
        self.rect = Rect(x, y, c.ENEMY_WIDTH, c.ENEMY_HEIGHT)

    def __del__(self):
        sounds.Sound.get_enemy()
        Enemy.__counter += 1

    @staticmethod
    def getCounter():
        return Enemy.__counter

    def update(self, platforms, entities):
        if not self.on_ground:
            # only accelerate with gravity if in the air
            self.y_vel += 0.3
            # max falling speed
            if self.y_vel > 100: self.y_vel = 100

        # increment in x direction
        self.rect.left += self.x_vel
        # do x-axis collisions
        self.collide(self.x_vel, 0, platforms, entities)
        # increment in y direction
        self.rect.top += self.y_vel
        # assuming we're in the air
        self.on_ground = False;
        # do y-axis collisions
        self.collide(0, self.y_vel, platforms, entities)

        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, exit_block.ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.x_vel = -abs(xvel)
                    print "collide right"
                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.x_vel = abs(xvel)
                    print "collide left"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.y_vel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        for p in entities:
            if pygame.sprite.collide_rect(self, p):
                dif = p.rect.bottom - self.rect.top
                if dif <= 8:
                    self.destroyed = True
                    self.counter = 0
                    self.x_vel = 0

    def animate(self):

        if not self.destroyed:
            self.walk_loop()
        else:
            self.destroyloop()

    def walk_loop(self):
        if self.counter == 10:
            self.updatesprite_frame(enemy_walk_1)
        elif self.counter == 20:
            self.updatesprite_frame(enemy_walk_2)
            self.counter = 0
        self.counter = self.counter + 1

    def destroyloop(self):
        if self.counter == 0:
            self.updatesprite_frame(enemy_flat)
        elif self.counter == 10:
            self.kill()
        self.counter = self.counter + 1

    def updatesprite_frame(self, ansurf):
        self.image = ansurf
