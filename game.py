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
from scripts.entities import PhysicsEntity
from scripts.utils  import load_image

"""

Initialize pygame / window / clock 

"""

class Game:
    def __init__(self):

        pygame.init()

        pygame.display.set_caption('PREFire') ## name
        self.screen = pygame.display.set_mode((640, 480)) ## screen
        self.display = pygame.Surface((320,240)) ## generates an empty image basically with the dimensions passed
        self.clock = pygame.time.Clock() ## clock set

        # self.img = pygame.image.load('./assets/00_resources/data/images/clouds/cloud_1.png')
        self.img_pos = [160, 260]
        self.movement = [False, False]
        # self.collision_area = pygame.Rect(50, 50, 300, 50)
        self.assets = {
            'player': load_image('entities/player.png')
        }

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
    
    def run(self):
        while True:


            self.display.fill((14, 219, 248))

            self.player.update((self.movement[1] - self.movement[0], 0))

            self.player.render(self.display)


            for event in pygame.event.get(): # gets the evnet
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True 
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False 
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False


            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update() ## -> updates the display on the screen
            self.clock.tick(60) ## -> forces the game to remain at 60 frames per seconds (will sleep the game)
        


Game().run()