"""
File Description : Main Loop for the Game 

Author: Matthew Ogden (2/4/2024)
Co-Auther/Editors:
    > 

"""


"""

Import Modules

"""
import pygame
import sys

"""

Initialize pygame / window / clock 

"""


class Tilemap:
    def __init__(self, tile_size=16):
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap 