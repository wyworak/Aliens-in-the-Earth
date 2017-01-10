# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *

from random import randint

from files import constants as c, level
from models import camera as cam
from models import enemy as en
from models import player as pl
from models import stars as st
from models import sounds

# Armazena o valor em milisegundos da ultima atualização
last_tick = 0


def texts(screen, font_size, color, text, x, y):
    # função para exibir os textos na tela
    font = pygame.font.Font("resources/fonts/Fixedsys500c.ttf", font_size)
    scoretext = font.render(str(text), 1, color)
    screen.blit(scoretext, (x, y))


def spawnEnemies(level, seconds):
    # função para geração aleatória dos inimigos
    global last_tick
    now = pygame.time.get_ticks()
    if (now - last_tick) / 1000 >= seconds:
        level.enemy_group.add(en.Enemy(32 * randint(1, 38), 32))
        last_tick = now


def main():
    # status para fechar o aplicativo
    close = False

    # status da música da tela do final do jogo
    start_end_music = False

    # inicia o pygame
    pygame.init()

    # controla as musicas do jogo
    music = sounds.Sound(False)

    # inicia a tela do jogo
    # Modo janela
    # screen = pygame.display.set_mode(c.DISPLAY, c.FLAGS, c.DEPTH)
    # modo fullscreen
    screen = pygame.display.set_mode((c.DISPLAY), FULLSCREEN)

    # define o texto que aparece na barra superior
    pygame.display.set_caption(c.CAPTION)

    # controla o tempo do jogo
    timer = pygame.time.Clock()

    # ultima atualização da tela
    last_tick = pygame.time.get_ticks()

    # variáveis que controlam o movimento do personagem
    up = down = left = right = running = False

    # variavél que representa o jogador em uma determinada posição da tela
    player = pl.Player(600, 680)

    # cria o nível do jogo, todas as definições do nível estão na classe Level
    level_01 = level.Level()
    level_01.Level_01()

    # total de blocos na largura da tela
    total_level_width = len(level_01.char_level[0]) * c.LEVEL_BLOCK_WIDTH

    # total de blocos na altura da tela
    total_level_height = len(level_01.char_level) * c.LEVEL_BLOCK_HEIGHT

    # cria a camera do jogo
    camera = cam.Camera(cam.complex_camera, total_level_width, total_level_height)

    # adiciona o jogador à lista de entidades
    level_01.entities.add(player)

    # cria alguns inimigos para iniciar o jogo
    level_01.enemy_group.add(en.Enemy(32 * 6, 32))
    level_01.enemy_group.add(en.Enemy(64 * 9, 32))
    level_01.enemy_group.add(en.Enemy(32 * 12, 32))

    # cria os itens que poderão ser coletados
    level_01.star_group.add(st.Star(-50, -50))
    level_01.star_group.add(st.Star(990, 62))
    level_01.star_group.add(st.Star(212, 190))
    level_01.star_group.add(st.Star(660, 286))
    level_01.star_group.add(st.Star(970, 256))
    level_01.star_group.add(st.Star(800, 416))
    level_01.star_group.add(st.Star(420, 352))
    level_01.star_group.add(st.Star(230, 478))
    level_01.star_group.add(st.Star(560, 128))
    level_01.star_group.add(st.Star(740, 544))
    level_01.star_group.add(st.Star(840, 62))

    # loop principal do jogo
    while 1:

        # Define o frame rate
        timer.tick(60)

        # Pega os eventos
        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_RETURN:
                close = True

        # cria os inimigos em posições eleatórias a cada dois segundos
        spawnEnemies(level_01, 2)

        # exibe o background na cena
        screen.blit(level_01.bg, (0, 0))

        # atualiza a camera com a posição do jogador
        camera.update(player)

        # Atualiza o jogador e desenha o restante da cena enquanto ele não perder
        if not player.game_over:
            player.update(up, down, left, right, running, level_01.platforms, level_01.enemy_group, level_01.star_group)

            # exibe todas as entidades na tela
            for e in level_01.entities:
                screen.blit(e.image, camera.apply(e))

            # exibe os itens que podem ser coletados e cuida das colisões com o jogador
            for s in level_01.star_group:
                screen.blit(s.image, camera.apply(s))
                s.update(level_01.star_group, player)

            # exibe os inimigos e cuida das colisões com o jogador
            for e in level_01.enemy_group:
                screen.blit(e.image, camera.apply(e))
                e.update(level_01.platforms, level_01.entities)

            # exibe a sprite que mostra a pontuação
            screen.blit(level_01.gui, (1075, 5))

            # seta quantos inimigos o jogador matou
            player.enemies = en.Enemy.getCounter()

            # seta quantos itens o jogador pegou
            player.stars = st.Star.getCounter()

            # calcula a pontuação do jogador
            player.calculate_score()

            # exibe os textos de pontuação do jogador
            texts(screen, 30, c.WHITE, player.score, 1130, 10)
            texts(screen, 30, c.WHITE, player.stars, 1130, 65)
        else:
            # quando o jogador perde, troca a música e o background
            if not start_end_music:
                music.set_music_mixer(True)
                start_end_music = True

            # gerencia qual a imagem será exibida na tela final de acordo com a pontuação do jogador
            level_01.EndGame(player.enemies, player.stars)
            screen.blit(level_01.bg, (0, 0))

            # reposiciona os textos de pontuação do jogador
            texts(screen, 50, c.ORANGE, player.score, 675, 380)
            texts(screen, 50, c.ORANGE, str(player.stars) + "/10", 675, 515)

            if close:
                # quando o jogador precionar ENTER na tela final o jogo finaliza
                pygame.event.post(pygame.event.Event(QUIT))

        # atualiza a cada frame tudo que está sendo exibido
        pygame.display.update()


if __name__ == "__main__":
    # chamada no inicio do programa
    main()