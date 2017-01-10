# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *
from files import constants as c
from models import platform, exit_block

class Level(object):
    'Esta classe cria a estrutura do cenário'
    def __init__(self):
        self.platforms = []
        self.entities = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.star_group = pygame.sprite.Group()
        self.x = 0
        self.y = 0
        self.char_level = []

    def BuildLevel(self, level):
        'cria as plataformas com base em um array de caracteres'
        for row in level:
            for col in row:
                if col == "P":
                    # para cada P encontrado no array será criado um bloco com colisão no cenário
                    p = platform.Platform(self.x, self.y)
                    self.platforms.append(p)
                    self.entities.add(p)
                if col == "E":
                    # para cada E encontrado no array será criado um bloco para finalizar o jogo quando o jogador colidir com ele
                    e = exit_block.ExitBlock(self.x, self.y)
                    self.platforms.append(e)
                    self.entities.add(e)
                self.x += c.LEVEL_BLOCK_WIDTH
            self.y += c.LEVEL_BLOCK_HEIGHT
            self.x = 0

    def Level_01(self):
        'cria o nível 01 do jogo'
        self.gui = pygame.image.load("resources/graphics/gui.png").convert_alpha()
        self.gui = pygame.transform.scale(self.gui, (200, 100))
        self.bg = pygame.image.load("resources/graphics/bg.jpg").convert()
        self.platforms = []
        self.x = 0
        self.y = 0

        # array de caracteres com o desenho do cenário.
        # cada P é um bloco com colisão onde o jogador poderá andar
        self.char_level = [
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "P                                      P",
            "P                                      P",
            "P                    PPPPPPPPPPP       P",
            "P                  PP                  P",
            "P                PP                    P",
            "P                                      P",
            "P    PPPPPPPP                          P",
            "P            PP                        P",
            "P                          PPPPPPP     P",
            "P                 PPPPPP               P",
            "P                                      P",
            "P         PPPPPPP                      P",
            "P       PP                             P",
            "P                     PPPPPP           P",
            "P                                      P",
            "P   PPPPPPPPPPP                        P",
            "P                                      P",
            "P                 PPPPPPPPPPP          P",
            "P                            PP        P",
            "P                              PP      P",
            "P                                      P",
            "P                                      P",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]

        self.BuildLevel(self.char_level)

    def EndGame(self, enemies, stars):
        'esta função define, com base no número de inimigos mortos e itens coletados, qual tela será exibida no final do jogo'
        if stars < 3:
            self.bg = pygame.image.load("resources/graphics/bg_no_stars.png").convert()
        elif stars > 2 and stars < 5:
            self.bg = pygame.image.load("resources/graphics/bg_one_star.png").convert()
        elif stars > 4 and stars < 8:
            if enemies > 10:
                self.bg = pygame.image.load("resources/graphics/bg_two_stars.png").convert()
            else:
                self.bg = pygame.image.load("resources/graphics/bg_one_star.png").convert()
        elif stars > 9:
            if enemies > 20:
                self.bg = pygame.image.load("resources/graphics/bg_three_stars.png").convert()
            else:
                self.bg = pygame.image.load("resources/graphics/bg_two_stars.png").convert()