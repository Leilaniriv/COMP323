import pygame
import sys
from spritesheet import *
from config import*
from nova_game import player

class Carnival:
    def __init__(self,player):
        pygame.init()
        self.player = player
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()

    def carnival_scene(self):
        background = pygame.image.load('carnival_background1.png').convert_alpha()
        background = pygame.transform.scale(background,(1200,750))

        x = 10
        y = 300

        run = True
        while run:
            self.screen.blit(background, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            player.update()
            self.screen.blit(player.image, player.rect)

            pygame.display.update()
            self.clock.tick(60)