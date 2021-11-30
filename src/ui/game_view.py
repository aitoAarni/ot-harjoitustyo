import pygame as py
from pygame.locals import *


class Game_interface:
    def __init__(self, width, heigth, colors):
        py.init()
        self.game_display = py.display.set_mode((width, heigth))
        self.colors = colors

    def draw_tetrominoe(self, falling_tetrominoe, landed_tetrominoes):
        # draw falling tetrominoe
        self.game_display.blit(falling_tetrominoe.image, (falling_tetrominoe.x, falling_tetrominoe.y))

        # draw landed tetrominoe
        for tet in landed_tetrominoes:
            self.game_display.blit(tet.image, (tet.x, tet.y))

    def draw_window(self, falling_tetrominoe, landed_tetrominoes):
        self.game_display.fill((0, 0, 0))
        self.draw_tetrominoe(falling_tetrominoe, landed_tetrominoes)
        py.display.update()
