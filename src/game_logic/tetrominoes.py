import random, load_store.load_tetrominoes, pygame as py
import game_logic.tetromino
from pygame.locals import *


# Handles the Tetrominoes
class Tetrominoes:
    def __init__(self):
        py.init()
        self.block_images = load_store.load_tetrominoes.LoadTetrominoes().load_pictures()
        self.counter = 0
        self.landed_tetrominoes = []
        self.create_new_tetrominoe()

    def create_new_tetrominoe(self):
        #shape = random.choice([i for i in self.block_images.keys()])
        shape = "L"
        self.falling_tetrominoe = game_logic.tetromino.Block(self.block_images[shape], shape)

    def falling_tetrominoe_landed(self):
        self.landed_tetrominoes.append(self.falling_tetrominoe)

    
    def move_tetrominoe_down_by_a_block(self, move):
        if move:
            self.falling_tetrominoe.move(0, 45)

    def move_tetrominoe_right(self, move):
        if move:
            self.falling_tetrominoe.move(45, 0)

    def move_tetrominoe_left(self, move):
        if move:
            self.falling_tetrominoe.move(-45, 0)

    def move_tetrominoe(self, right, left, down):
        moved = False
        if self.counter % 20 == 0:
            moved = True
            self.move_tetrominoe_left(left)
            self.move_tetrominoe_right(right)
        if self.counter % 75 == 0:
            self.move_tetrominoe_down_by_a_block(down)
        self.counter += 1
        return moved

    


        