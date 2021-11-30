import pygame as py
from pygame.locals import *


class Events:
    def __init__(self):
        py.init()
        self.reset_keys_pressed()

    def reset_keys_pressed(self):
        self.left_pressed, self.right_pressed, self.down_pressed = False, False, False

    def event_loop(self):
        for event in py.event.get():

            if event.type == py.QUIT:
                py.quit()

            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    self.left_pressed = True
                if event.key == py.K_RIGHT:
                    self.right_pressed = True
                if event.key == py.K_DOWN:
                    self.down_pressed = True

            if event.type == py.KEYUP:
                if event.key == py.K_LEFT:
                    self.left_pressed = False
                if event.key == py.K_RIGHT:
                    self.right_pressed = False
                if event.key == py.K_DOWN:
                    self.down_pressed = False
