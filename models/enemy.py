# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *
from files import constants as c
from models import entity, exit_block, sounds

# carrega a sequencia de imagens do inimigo
spritesheet = pygame.image.load("resources/graphics/enemy.png")

# separa cada quadro da sequencia para gerar as animações
sprite_frame = Surface((c.ENEMY_SPRITE_WIDTH, c.ENEMY_SPRITE_WIDTH), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (0, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.ENEMY_WIDTH, c.ENEMY_HEIGHT))
enemy_walk_1 = sprite_frame

sprite_frame = Surface((c.ENEMY_SPRITE_WIDTH, c.ENEMY_SPRITE_WIDTH), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-32, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.ENEMY_WIDTH, c.ENEMY_HEIGHT))
enemy_walk_2 = sprite_frame

sprite_frame = Surface((c.ENEMY_SPRITE_WIDTH, c.ENEMY_SPRITE_WIDTH), pygame.SRCALPHA)
sprite_frame.blit(spritesheet, (-64, 0))
sprite_frame = pygame.transform.scale(sprite_frame, (c.ENEMY_WIDTH, c.ENEMY_HEIGHT))
enemy_die = sprite_frame

class Enemy(entity.Entity):
    'representa os inimigos do jogo'

    # contador de inimigos
    __counter = 0

    def __init__(self, x, y):
        entity.Entity.__init__(self)
        # velocidade no eixo x
        self.x_vel = -1
        # velocidade no eixo y
        self.y_vel = 0
        # verifica se o inimigo está no chão
        self.on_ground = False
        # verifica se o inimigo está destruido
        self.destroyed = False
        # contador para animação
        self.counter = 0
        # imagem inicial do inimigo
        self.image = enemy_walk_1
        # posiciona o inimigo em uma posição passada por parametros
        self.rect = Rect(x, y, c.ENEMY_WIDTH, c.ENEMY_HEIGHT)

    def __del__(self):
        'ao destruir um inimigo é emitido um som e o contador é acrescentado'
        sounds.Sound.get_enemy()
        Enemy.__counter += 1

    @staticmethod
    def getCounter():
        'retorna o total de inimigos destruidos'
        return Enemy.__counter

    def update(self, platforms, entities):
        if not self.on_ground:
            # só acelera com gravidade se o inimigo está no ar
            self.y_vel += 0.3
            # velocidade máxima de queda
            if self.y_vel > 100: self.y_vel = 100

        # incrementa na direção x
        self.rect.left += self.x_vel
        # verifica colisões no eixo x
        self.collide(self.x_vel, 0, platforms, entities)
        # incrementa na direção y
        self.rect.top += self.y_vel
        # considera que o inimigo está no ar
        self.on_ground = False;
        # verifica colisões no eixo y
        self.collide(0, self.y_vel, platforms, entities)

        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        'gerencia as colisões'
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, exit_block.ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.x_vel = -abs(xvel)
                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.x_vel = abs(xvel)
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.y_vel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        for p in entities:
            if pygame.sprite.collide_rect(self, p):
                dif = p.rect.bottom - self.rect.top
                if dif <= 8:
                    self.destroyed = True
                    self.counter = 0
                    self.x_vel = 0

    def animate(self):
        'gerencia as trocas de animações'
        if not self.destroyed:
            self.walk_loop()
        else:
            self.destroyloop()

    def walk_loop(self):
        'troca as sriptes para criar a animação de andar'
        if self.counter == 10:
            self.updatesprite_frame(enemy_walk_1)
        elif self.counter == 20:
            self.updatesprite_frame(enemy_walk_2)
            self.counter = 0
        self.counter = self.counter + 1

    def destroyloop(self):
        'cria a animação de destruir o inimigo'
        if self.counter == 0:
            self.updatesprite_frame(enemy_die)
        elif self.counter == 10:
            self.kill()
        self.counter = self.counter + 1

    def updatesprite_frame(self, sprite):
        self.image = sprite
