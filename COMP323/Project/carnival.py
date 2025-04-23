import pygame
import sys
from spritesheet import *
from config import*
from nova_game import Player
from balloon_pop import Balloon

class Carnival:
    def __init__(self,player):
        pygame.init()
        self.player = player
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()


    def carnival_scene(self):
        background = pygame.image.load('carnival.png').convert_alpha()
        background = pygame.transform.scale(background,(1200,750))

        booth1 = pygame.Rect(width/4 - 120, height / 4 - 70, 180, 192)
        booth2 = pygame.Rect(width/4 - 275, height / 2 + 34, 180, 194)
        booth3 = pygame.Rect(width/2 - 90, height / 4 - 4, 180, 193)
        booth4 = pygame.Rect(width/3 - 12, height / 2 + 156, 169, 193)
        booth5 = pygame.Rect(width/2 + 25, height / 2 + 35, 180, 193)
        booth6 = pygame.Rect(width/2 + 389, height / 2 + 156, 167, 193)
        booth7 = pygame.Rect(width/2 + 510, height / 4 - 4, 90, 193)

        booths = [booth1, booth2, booth3, booth4, booth5, booth6, booth7]

        run = True
        while run:
            self.screen.blit(background, (0,0))
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                '''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if booth2.collidepoint(mouse):
                        balloon = Balloon()
                        balloon.run()
                '''

            self.player.update()
            self.player.handle_collision(booths)
            
            for booth in booths:
                pygame.draw.rect(self.screen, black, booth)

            
            #draw player
            self.screen.blit(self.player.image, self.player.rect.topleft)

        
            pygame.display.update()
            self.clock.tick(60)


    def run(self):
        self.carnival_scene()