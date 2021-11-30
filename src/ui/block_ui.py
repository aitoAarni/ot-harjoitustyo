import pygame as py
from game_view import Game_interface


class Block_ui:
    def __init__(self, edge):
        self.edge = edge

    def create_block(self):
        return py.draw.rect(Game_interface.game_display, (255, 240, 4), (50, 50, 35, 35))
