# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import os

WIN_WIDTH = 1280
WIN_HEIGHT = 768
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

CAPTION = "11145 - Programacao Em Jogos Digitais"

PLAYER_WIDTH = 32
PLAYER_HEIGHT = 64

PLAYER_SPRITE_WIDTH = 32
PLAYER_SPRITE_HEIGHT = 64

ENEMY_WIDTH = 32
ENEMY_HEIGHT = 32

ENEMY_SPRITE_WIDTH = 32
ENEMY_SPRITE_HEIGHT = 32

LEVEL_BLOCK_WIDTH = 32
LEVEL_BLOCK_HEIGHT = 32

SCORE_STARS_MULTIPLIER = 200
SCORE_ENEMY_MULTIPLIER = 50

# Diretórios
BASE_DIR = os.path.abspath('.')
MUSICS_DIR = BASE_DIR + "\\" + os.path.join("resources", "music")
SFX_DIR = BASE_DIR + "\\" + os.path.join("resources", "sound")

# COLORS
#                R    G    B
GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK    = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)