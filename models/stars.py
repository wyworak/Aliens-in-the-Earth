# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *
from files import constants as c
from models import entity, sounds

class Star(entity.Entity):

    __counter = 0

    def __init__(self, x, y):
        entity.Entity.__init__(self)
        self.image = pygame.image.load("resources/graphics/star.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (c.ENEMY_WIDTH, c.ENEMY_HEIGHT))
        self.rect = Rect(x, y, c.ENEMY_WIDTH, c.ENEMY_HEIGHT)

    def __del__(self):
        sounds.Sound.get_star()
        Star.__counter += 1

    def update(self, entities, player):
        self.collide(player)

    def collide(self, player):
        if pygame.sprite.collide_rect(self, player):
            dif = player.rect.centerx - self.rect.centerx
            if dif <= 8:
                self.kill()

    @staticmethod
    def getCounter():
        return Star.__counter