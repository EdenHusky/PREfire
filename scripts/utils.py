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

Base Utils

"""

BASE_IMG_PATH = 'assets/00_resources/data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img