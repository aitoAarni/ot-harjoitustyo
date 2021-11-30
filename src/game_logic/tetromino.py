import pygame as py
from pygame.locals import *

class Block(py.sprite.Sprite):
    def __init__(self, img, shape):
        super(Block, self).__init__()
        py.init()
        py.display.set_mode()
        self.shape = shape
        self.image = img.convert_alpha()
        self.configure_image()
    def configure_image(self):
        size_dict = {"L" : (135, 90)}

        self.image = py.transform.scale(self.image, size_dict[self.shape])
        self.mask = py.mask.from_surface(self.image)
        width, length = self.image.get_size()

        self.x = 225 - width
        self.y = 0 - length
        self.rect = py.Rect(self.y, self.x, width, length)
    
    def move(self, x, y):
        self.x += x
        self.y += y
    
    
    
    def __str__(self) -> str:
        return print(f"shape: {self.shape}, pos: {(self.x, self.y)}")
    