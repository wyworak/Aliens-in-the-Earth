# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *
from files import constants as c
from models import entity, exit_block, sounds

# carrega a sequencia de imagens do jogador
spritesheet = pygame.image.load("resources/graphics/player.png")

# separa cada quadro da sequencia para gerar as animações

sprite_frame = Surface((c.PLAYER_SPRITE_WIDTH, c.PLAYER_SPRITE_HEIGHT), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-96, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.PLAYER_WIDTH, c.PLAYER_HEIGHT))
player_idle_1 = sprite_frame

sprite_frame = Surface((c.PLAYER_SPRITE_WIDTH, c.PLAYER_SPRITE_HEIGHT), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-64, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.PLAYER_WIDTH, c.PLAYER_HEIGHT))
player_walk_1 = sprite_frame

sprite_frame = Surface((c.PLAYER_SPRITE_WIDTH, c.PLAYER_SPRITE_HEIGHT), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-32, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.PLAYER_WIDTH, c.PLAYER_HEIGHT))
player_walk_2 = sprite_frame

sprite_frame = Surface((c.PLAYER_SPRITE_WIDTH, c.PLAYER_SPRITE_HEIGHT), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (0, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.PLAYER_WIDTH, c.PLAYER_HEIGHT))
player_walk_3 = sprite_frame

sprite_frame = Surface((c.PLAYER_SPRITE_WIDTH, c.PLAYER_SPRITE_HEIGHT), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-128, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.PLAYER_WIDTH, c.PLAYER_HEIGHT))
player_jump = sprite_frame

class Player(entity.Entity):
    'representa o jogador no jogo'
    def __init__(self, x, y):
        entity.Entity.__init__(self)
        # velocidade no eixo x
        self.x_vel = 0
        # velocidade no eixo y
        self.y_vel = 0
        # verifica se o jogador está olhando para a direita
        self.face_right = True
        # verifica se o jogador está no chão
        self.on_ground = False
        # verifica se o jogador está no ar
        self.airborne = False
        # contador para animação
        self.counter = 0
        # imagem inicial do jogador
        self.image = player_idle_1
        # posiciona o jogador em uma posição passada por parametros
        self.rect = Rect(x, y, c.PLAYER_WIDTH, c.PLAYER_HEIGHT)
        # pontuação do jogador
        self.score = 0
        # total de itens coletados
        self.stars = 0
        # total de inimigos mortos
        self.enemies = 0
        # verifica se o jogador perdeu o jogo
        self.game_over = False

    def update(self, up, down, left, right, running, platforms, enemy_group, star_group):

        if up:
            # só pula se estiver no chão
            if self.on_ground:
                self.y_vel -= 10
                sounds.Sound.player_jump()
        if down:
            pass
        if running:
            self.x_vel = 12
        if left:
            self.x_vel = -5
            self.face_right = False
        if right:
            self.x_vel = 5
            self.face_right = True
        if not self.on_ground:
            # só acelera com gravidade se o jogador está no ar
            self.y_vel += 0.5
            # velocidade máxima de queda
            if self.y_vel > 100: self.y_vel = 100
        if not (left or right):
            self.x_vel = 0
        if self.y_vel < 0 or self.y_vel > 1.2: self.airborne = True
        # incrementa na direção x
        self.rect.left += self.x_vel
        # verifica colisões no eixo x
        self.collide(self.x_vel, 0, platforms, enemy_group, star_group)
        # incrementa na direção y
        self.rect.top += self.y_vel
        # considera que o jogador está no ar
        self.on_ground = False;
        # verifica colisões no eixo y
        self.collide(0, self.y_vel, platforms, enemy_group, star_group)

        self.animate()

    def collide(self, xvel, yvel, platforms, enemy_group, star_group):
        'gerencia as colisões'
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, exit_block.ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.airborne = False
                    self.y_vel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
        for e in enemy_group:
            if pygame.sprite.collide_rect(self, e):
                dif = self.rect.bottom - e.rect.top
                if dif <= 8:
                    self.y_vel = - 8
                    self.score += 25
                else:
                    self.game_over = True

        for s in star_group:
            if pygame.sprite.collide_rect(self, s):
                dif = self.rect.centerx - s.rect.centerx
                if dif <= 8:
                    self.score += 125

    def animate(self):
        'gerencia as trocas de animações'
        if self.x_vel > 0 or self.x_vel < 0:
            self.walk_loop()
            if self.airborne: self.updatesprite_frame(player_jump)
        else:
            self.updatesprite_frame(player_idle_1)
            if self.airborne: self.updatesprite_frame(player_jump)

    def walk_loop(self):
        'troca as sriptes para criar a animação de andar'
        if self.counter == 5:
            self.updatesprite_frame(player_walk_3)
        elif self.counter == 10:
            self.updatesprite_frame(player_walk_2)
        elif self.counter == 15:
            self.updatesprite_frame(player_walk_1)
            self.counter = 0
        self.counter = self.counter + 1

    def updatesprite_frame(self, sprite):
        if not self.face_right: sprite = pygame.transform.flip(sprite, True, False)
        self.image = sprite

    def calculate_score(self):
        self.score = self.stars * c.SCORE_STARS_MULTIPLIER + self.enemies * c.SCORE_ENEMY_MULTIPLIER