import pygame as py


class LoadTetrominoes:
    def __init__(self):
        pass

    def load_pictures(self):
        img_dict = {}
        img_dict["I"] = py.image.load("data/block_pictures/I_block")
        img_dict["J"] = py.image.load("data/block_pictures/J_block")
        img_dict["L"] = py.image.load("data/block_pictures/L_block")
        img_dict["O"] = py.image.load("data/block_pictures/O_block")
        img_dict["S"] = py.image.load("data/block_pictures/S_block")
        img_dict["T"] = py.image.load("data/block_pictures/T_block")
        img_dict["Z"] = py.image.load("data/block_pictures/Z_block")
        return  img_dict