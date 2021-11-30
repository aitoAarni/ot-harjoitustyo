import random, load_store.load_tetrominoes, pygame as py
from pygame.locals import *


# Handles the Tetrominoes
class Tetrominoe:
    def __init__(self):
        py.init()
        self.counter = 0
        self.landed_tetrominoes = []
        self.create_new_tetrominoe()
        self.block_images = load_store.load_tetrominoes.LoadTetrominoes().load_pictures()

    def create_new_tetrominoe(self):
        x = random.randint(0,350-35)
        self.falling_tetrominoe = py.Rect((x,0),(35,35)).unionall([py.Rect((x+35,0),(35,35))])

    
    def falling_tetrominoe_landed(self):
        self.landed_tetrominoes.append(self.falling_tetrominoe)

    
    def move_tetrominoe_down_by_a_block(self, move):
        if move:
            self.falling_tetrominoe = self.falling_tetrominoe.move(0, 35)

    def move_tetrominoe_right(self, move):
        if move:
            self.falling_tetrominoe = self.falling_tetrominoe.move(35, 0)

    def move_tetrominoe_left(self, move):
        if move:
            self.falling_tetrominoe = self.falling_tetrominoe.move(-35, 0)

    def move_tetrominoe(self, right, left, down):
        moved = False
        if self.counter % 20 == 0:
            moved = True
            print(right)
            self.move_tetrominoe_left(left)
            self.move_tetrominoe_right(right)
        if self.counter % 75 == 0:
            self.move_tetrominoe_down_by_a_block(down)
        self.counter += 1
        return moved


    def __str__(self):
        return "Falling tetrominoe: " + ", ".join(self.falling_tetrominoe)

        