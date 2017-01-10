# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import os
import pygame
from pygame import *
import wave

from files import constants as c

class Sound(object):
    'carrega e toca as músicas e efeitos sonoros do jogo'
    def __init__(self, game_over):
        self.music_dict = self.set_music_mixer(game_over)

    def set_music_mixer(self, game_over):
        'define qual a música que fica tocando'
        if game_over:
            # musica de gameover
            print c.MUSICS_DIR + '\game_over.ogg'
            pygame.mixer.music.load(c.MUSICS_DIR + '\game_over.ogg')
            pygame.mixer.music.play(-1)
        else:
            # musica do jogo
            print c.MUSICS_DIR + '\main_theme.ogg'
            pygame.mixer.music.load(c.MUSICS_DIR + '\main_theme.ogg')
            pygame.mixer.music.play(-1)

    @staticmethod
    def get_star():
        'som emitido jogador coletar um item'
        star_sound = pygame.mixer.Sound(c.SFX_DIR + '\star.wav')
        star_sound.play()

    @staticmethod
    def get_enemy():
        'som emitido ao jogador matar um inimigo'
        enemy_sound = pygame.mixer.Sound(c.SFX_DIR + '\enemy.wav')
        enemy_sound.play()

    @staticmethod
    def player_jump():
        'som emitido ao jogador pular'
        player_jump_sound = pygame.mixer.Sound(c.SFX_DIR + '\jump.wav')
        player_jump_sound.play()