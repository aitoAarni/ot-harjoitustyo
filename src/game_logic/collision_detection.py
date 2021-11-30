import pygame as py
from pygame.locals import *

class Collisions:
    def __init__(self, falling, landed):
        self.falling = falling
        self.landed = landed

    def detect_collision(self):
        
            