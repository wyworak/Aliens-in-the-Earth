# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

# nesse arquivo se encontram todas as constantes utilizadas no projeto.
# foram criadas para facilitar caso se deseje altera alguma configuração do jogo sem ter que procurar todas as
# utilizações no código

import os

# largura da tela
WIN_WIDTH = 1280
# altura da tela
WIN_HEIGHT = 768
# metade da largura da tela
HALF_WIDTH = int(WIN_WIDTH / 2)
# metade da altura da tela
HALF_HEIGHT = int(WIN_HEIGHT / 2)

# tamanho do display
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
# profundidade de cores
DEPTH = 32
# marcador para a criação da tela
FLAGS = 0

# titulo do aplicativo no modo janela
CAPTION = "Aliens in the Earth"

# largura do jogador em pixels
PLAYER_WIDTH = 32
# altura do jogador em pixels
PLAYER_HEIGHT = 64

# largura da sprite do jogador em pixels
PLAYER_SPRITE_WIDTH = 32
# altura da sprite do jogador em pixels
PLAYER_SPRITE_HEIGHT = 64

# largura do inimigo em pixels
ENEMY_WIDTH = 32
# altura do inimigo em pixels
ENEMY_HEIGHT = 32

# largura da sprite do inimigo em pixels
ENEMY_SPRITE_WIDTH = 32
# altura da sprite do inimigo em pixels
ENEMY_SPRITE_HEIGHT = 32

# largura dos blocos da plataforma em pixels
LEVEL_BLOCK_WIDTH = 32
# altura dos blocos da plataforma em pixels
LEVEL_BLOCK_HEIGHT = 32

# multiplicador de pontuação por cada item coletado
SCORE_STARS_MULTIPLIER = 200
# multiplicador de pontuação por cada inimigo morto
SCORE_ENEMY_MULTIPLIER = 50

# diretorio base do projeto
BASE_DIR = os.path.abspath('.')
# diretório das músicas
MUSICS_DIR = BASE_DIR + "\\" + os.path.join("resources", "music")
# diretório dos efeitos sonoros
SFX_DIR = BASE_DIR + "\\" + os.path.join("resources", "sound")

# cores
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