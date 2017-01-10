# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *
from files import constants as c
from models import entity

class Platform(entity.Entity):
    'representa os blocos onde o jogador e os inimigos podem andar'
    def __init__(self, x, y):
        entity.Entity.__init__(self)
        self.image = pygame.image.load("resources/graphics/block.png").convert()
        self.image = pygame.transform.scale(self.image, (c.LEVEL_BLOCK_WIDTH, c.LEVEL_BLOCK_HEIGHT))
        self.rect = Rect(x, y, c.LEVEL_BLOCK_WIDTH, c.LEVEL_BLOCK_HEIGHT)

    def update(self):
        pass