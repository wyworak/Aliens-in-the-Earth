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

last_tick = 0


def texts(screen, font_size, color, text, x, y):
   font=pygame.font.Font("resources/fonts/Fixedsys500c.ttf",font_size)
   scoretext=font.render(str(text), 1, color)
   screen.blit(scoretext, (x, y))

def spawnEnemies(level, seconds):
    global last_tick
    now = pygame.time.get_ticks()
    if (now - last_tick) / 1000 >= seconds:
        level.enemy_group.add(en.Enemy(32 * randint(1, 38), 32))
        last_tick = now

def main():

    close = False

    start_end_music = False

    pygame.init()

    music = sounds.Sound(False)

    screen = pygame.display.set_mode((c.DISPLAY), FULLSCREEN)

    pygame.display.set_caption(c.CAPTION)

    timer = pygame.time.Clock()

    last_tick = pygame.time.get_ticks()

    up = down = left = right = running = False

    player = pl.Player(c.PLAYER_WIDTH, c.PLAYER_HEIGHT)

    level_01 = level.Level()
    level_01.Level_01()

    total_level_width = len(level_01.char_level[0]) * c.LEVEL_BLOCK_WIDTH
    total_level_height = len(level_01.char_level) * c.LEVEL_BLOCK_HEIGHT
    camera = cam.Camera(cam.complex_camera, total_level_width, total_level_height)
    level_01.entities.add(player)

    level_01.enemy_group.add(en.Enemy(32 * 6, 32))
    level_01.enemy_group.add(en.Enemy(64 * 9, 32))
    level_01.enemy_group.add(en.Enemy(32 * 12, 32))

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

        spawnEnemies(level_01, 2)

        screen.blit(level_01.bg, (0, 0))

        camera.update(player)

        # Atualiza o jogador e desenha o restante da cena enquanto ele não perder
        if not player.game_over:
            player.update(up, down, left, right, running, level_01.platforms, level_01.enemy_group, level_01.star_group)

            for e in level_01.entities:
                screen.blit(e.image, camera.apply(e))

            for s in level_01.star_group:
                screen.blit(s.image, camera.apply(s))
                s.update(level_01.star_group, player)

            for e in level_01.enemy_group:
                screen.blit(e.image, camera.apply(e))
                e.update(level_01.platforms, level_01.entities)

            screen.blit(level_01.gui, (1075, 5))

            player.enemies = en.Enemy.getCounter()
            player.stars = st.Star.getCounter()
            player.calculate_score()

            texts(screen, 30, c.WHITE, player.score, 1130, 10)
            texts(screen, 30, c.WHITE, player.stars, 1130, 65)
        else:
            if not start_end_music:
                music.set_music_mixer(True)
                start_end_music = True

            level_01.EndGame(player.enemies, player.stars)
            screen.blit(level_01.bg, (0, 0))

            texts(screen, 50, c.ORANGE, player.score, 675, 380)
            texts(screen, 50, c.ORANGE, str(player.stars) + "/10", 675, 515)

            if close:
                pygame.event.post(pygame.event.Event(QUIT))



        pygame.display.update()

if __name__ == "__main__":
    main()