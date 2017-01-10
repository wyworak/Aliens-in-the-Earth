# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *
from files import constants as c
from models import entity, sounds

class Star(entity.Entity):
    'representa os itens que podem ser coletados no jogo'

    # contador de itens
    __counter = 0

    def __init__(self, x, y):
        entity.Entity.__init__(self)
        # carrega a sprite do item a ser coletado
        self.image = pygame.image.load("resources/graphics/star.png").convert_alpha()
        # define o tamanho do item
        self.image = pygame.transform.scale(self.image, (c.ENEMY_WIDTH, c.ENEMY_HEIGHT))
        # posiciona o item na tela
        self.rect = Rect(x, y, c.ENEMY_WIDTH, c.ENEMY_HEIGHT)

    def __del__(self):
        'quando o item é coletado emite um som e soma o contador de itens'
        sounds.Sound.get_star()
        Star.__counter += 1

    def update(self, entities, player):
        'atualiza a verificação de colisões entre o jogador e os itens'
        self.collide(player)

    def collide(self, player):
        'verifica as colisões entre o jogador e os itens'
        if pygame.sprite.collide_rect(self, player):
            dif = player.rect.centerx - self.rect.centerx
            if dif <= 8:
                self.kill()

    @staticmethod
    def getCounter():
        'retorna o total de itens coletados pelo jogador'
        return Star.__counter