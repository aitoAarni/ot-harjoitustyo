import pygame as py
from pygame.locals import *


class MoveTetrominoe:
    def __init__(self, right_pressed=False, left_pressed=False):
        py.init()
        self.counter = 0
        self.left_pressed = left_pressed
        self.right_pressed = right_pressed
    

    def move_tetrominoe(self, right_pressed, left_pressed):
        self.left_pressed, self.right_pressed = left_pressed, right_pressed
        self.move_tetrominoe_right = False
        self.move_tetrominoe_left = False
            # Move left
        if self.left_pressed and not self.right_pressed:
            self.move_tetrominoe_left = True
        
        # Move right
        if self.right_pressed and not self.left_pressed:
            self.move_tetrominoe_right = True

        self.move_tetrominoe_down = True
    
        self.counter += 1


