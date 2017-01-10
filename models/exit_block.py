# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

from models import platform as p

class ExitBlock(p.Platform):
    'bloco com colisão para finalizar o jogo quando o player colidir com ele'
    def __init__(self, x, y):
        p.Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))