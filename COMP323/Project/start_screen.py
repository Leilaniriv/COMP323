import pygame
from spritesheet import *
import sys
from pygame.locals import *
from config import *
from desert import *
from desert import run_desert_text
from laserhallway import *
from prologue import run_prologue
from carnival import Carnival
from tanklevel import *
from nova_game import player



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        

    def createTileMap(self): #iterates through the tile map of B's and .'s and places images based on what char 
        for i, row in enumerate(tilemap): # 'i' stands for string, row is the row # of tilemap
            for j, column in enumerate(row):
                if column == 'B' :
                    Block(self ,j, i)
                #if column = 'P': //for player
                    #Block()
    
    
    def Start_screen(self):
        
        font = pygame.font.Font('ByteBounce.ttf', 32)
        fontTitle = pygame.font.Font('ByteBounce.ttf', 62)

        exit = font.render('exit', True, white)
        begin = font.render('begin', True, white)
        title = fontTitle.render("NOVA", True, white)

        exit_button = pygame.Rect(width/4 - 45, height/2 + 100, 140, 90)
        begin_button = pygame.Rect(width/2 + 270, height/2 + 100,135,90)

        running = True
        while running:
            bg_image = pygame.image.load('nightsky.jpg').convert_alpha()
            bg_image = pygame.transform.scale(bg_image,(1200,750))
            bg_rect = bg_image.get_rect()
            self.screen.blit(bg_image, bg_rect)
            #self.screen.fill(black)
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                #if exit is clicked page exits
                    if exit_button.collidepoint(mouse):
                        pygame.quit()
                        sys.exit()
                #if begin button is clicked game begins
                    if begin_button.collidepoint(mouse):
                        pygame.time.wait(500)
                        self.game_loop()
                        running = False


        #buttons are drawn white when hovered over
            if exit_button.collidepoint(mouse):
                pygame.draw.rect(self.screen,light, exit_button)
        
            if begin_button.collidepoint(mouse):
                pygame.draw.rect(self.screen,light, begin_button)


        #adds the title, exit, and begin text
            self.screen.blit(exit, (width/4, height/2 + 125))
            self.screen.blit(begin, (width/2 + 300, height/2 + 125))
            self.screen.blit(title, (width/2 -50, height/4))
            
            pygame.display.update()
            self.clock.tick(60)

    def game_loop(self):
        run_prologue(self.screen)
        tanklevel = LevelTank(player)
        tanklevel.run()

        laserhallway = LaserHallway(player)
        laserhallway.run()

        run_desert_text(self.screen)

        desert = Desert(player)
        desert.run()




                        

if __name__ == "__main__":
    game = Game()
    game.Start_screen()
    game.game_loop
    pygame.quit()

