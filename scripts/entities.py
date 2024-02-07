"""
File Description :
    > pretty much just a character parent class that can take in different physics systems. 
        > think diddy and donkey

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

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]

    def update(self, movement=(0, 0)):
        # calliate the position update
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        # change possiiton of character
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]
    
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos) ## renders asset on the surface