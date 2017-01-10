# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *

class Entity(pygame.sprite.Sprite):
    'representa todos os elementos que fazem parte do cenário'
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)