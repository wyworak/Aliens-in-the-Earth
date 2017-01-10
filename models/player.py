# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *
from files import constants as c
from models import entity, exit_block, sounds

spritesheet = pygame.image.load("resources/graphics/player.png")

sprite_frame = Surface((c.PLAYER_SPRITE_WIDTH, c.PLAYER_SPRITE_HEIGHT), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-96, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.PLAYER_WIDTH, c.PLAYER_HEIGHT))
player_idle_1 = sprite_frame

sprite_frame = Surface((c.PLAYER_SPRITE_WIDTH, c.PLAYER_SPRITE_HEIGHT), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-64, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.PLAYER_WIDTH, c.PLAYER_HEIGHT))
player_walk_1 = sprite_frame

sprite_frame = Surface((c.PLAYER_SPRITE_WIDTH, c.PLAYER_SPRITE_HEIGHT), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-32, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.PLAYER_WIDTH, c.PLAYER_HEIGHT))
player_walk_2 = sprite_frame

sprite_frame = Surface((c.PLAYER_SPRITE_WIDTH, c.PLAYER_SPRITE_HEIGHT), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (0, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.PLAYER_WIDTH, c.PLAYER_HEIGHT))
player_walk_3 = sprite_frame

sprite_frame = Surface((c.PLAYER_SPRITE_WIDTH, c.PLAYER_SPRITE_HEIGHT), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-128, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.PLAYER_WIDTH, c.PLAYER_HEIGHT))
player_jump = sprite_frame

class Player(entity.Entity):
    def __init__(self, x, y):
        entity.Entity.__init__(self)
        self.x_vel = 0
        self.y_vel = 0
        self.face_right = True
        self.on_ground = False
        self.airborne = False
        self.counter = 0
        self.image = player_idle_1
        self.rect = Rect(x, y, c.PLAYER_WIDTH, c.PLAYER_HEIGHT)
        self.score = 0
        self.stars = 0
        self.enemies = 0
        self.game_over = False

    def update(self, up, down, left, right, running, platforms, enemy_group, star_group):

        if up:
            # only jump if on the ground
            sounds.Sound.player_jump()
            if self.on_ground:
                self.y_vel -= 10
        if down:
            pass
        if running:
            self.x_vel = 12
        if left:
            self.x_vel = -5
            self.face_right = False
        if right:
            self.x_vel = 5
            self.face_right = True
        if not self.on_ground:
            # only accelerate with gravity if in the air
            self.y_vel += 0.5
            # max falling speed
            if self.y_vel > 100: self.y_vel = 100
        if not (left or right):
            self.x_vel = 0
        if self.y_vel < 0 or self.y_vel > 1.2: self.airborne = True
        # increment in x direction
        self.rect.left += self.x_vel
        # do x-axis collisions
        self.collide(self.x_vel, 0, platforms, enemy_group, star_group)
        # increment in y direction
        self.rect.top += self.y_vel
        # assuming we're in the air
        self.on_ground = False;
        # do y-axis collisions
        self.collide(0, self.y_vel, platforms, enemy_group, star_group)

        self.animate()

    def collide(self, xvel, yvel, platforms, enemy_group, star_group):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, exit_block.ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print "collide right"
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print "collide left"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.airborne = False
                    self.y_vel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
        for e in enemy_group:
            if pygame.sprite.collide_rect(self, e):
                dif = self.rect.bottom - e.rect.top
                if dif <= 8:
                    self.y_vel = - 8
                    self.score += 25
                else:
                    self.game_over = True

        for s in star_group:
            if pygame.sprite.collide_rect(self, s):
                dif = self.rect.centerx - s.rect.centerx
                if dif <= 8:
                    self.score += 125

    def animate(self):

        if self.x_vel > 0 or self.x_vel < 0:
            self.walk_loop()
            if self.airborne: self.updatesprite_frame(player_jump)
        else:
            self.updatesprite_frame(player_idle_1)
            if self.airborne: self.updatesprite_frame(player_jump)

    def walk_loop(self):
        if self.counter == 5:
            self.updatesprite_frame(player_walk_3)
        elif self.counter == 10:
            self.updatesprite_frame(player_walk_2)
        elif self.counter == 15:
            self.updatesprite_frame(player_walk_1)
            self.counter = 0
        self.counter = self.counter + 1

    def updatesprite_frame(self, ansurf):
        if not self.face_right: ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf

    def calculate_score(self):
        self.score = self.stars * c.SCORE_STARS_MULTIPLIER + self.enemies * c.SCORE_ENEMY_MULTIPLIER