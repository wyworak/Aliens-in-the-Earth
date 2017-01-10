# -*- coding: utf-8 -*-

__author__ = 'Willyan Schultz Dworak'
__author__ = 'Jessica Vicente'

import pygame
from pygame import *
from files import constants as c

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l + c.HALF_WIDTH, -t + c.HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l + c.HALF_WIDTH, -t + c.HALF_HEIGHT, w, h

    l = min(0, l)  # para a rolagem na borda esquerda
    l = max(-(camera.width - c.WIN_WIDTH), l)  # para a rolagem na borda direita
    t = max(-(camera.height - c.WIN_HEIGHT), t)  # para a rolagem na borda de baixo
    t = min(0, t)  # para a rolagem na borda superior
    return Rect(l, t, w, h)