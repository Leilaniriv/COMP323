import pygame
from spritesheet import *
import sys
from pygame.locals import *
from config import *

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
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        exit = font.render('exit', True, white)
        begin = font.render('begin', True, white)
        title = font.render("NOVA", True, white)

        exit_button = pygame.Rect(width/4 + 60, height/2 + 100, 150, 90)
        begin_button = pygame.Rect(width/2 + 170, height/2 + 100,150,90)

        running = True
        while running:
            self.screen.fill(black)
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
                        running = False
                        self.game_loop()


        #buttons are black, when hovered over they are drawn white
            if exit_button.collidepoint(mouse):
                pygame.draw.rect(self.screen,light, exit_button)
            else:
                pygame.draw.rect(self.screen, black, exit_button)
        
            if begin_button.collidepoint(mouse):
                pygame.draw.rect(self.screen,light, begin_button)
            else:
                pygame.draw.rect(self.screen, black, begin_button) 
        #puts the title, exit button, and begin button
            self.screen.blit(exit, (width/4+100, height/2 + 125))
            self.screen.blit(begin, (width/2+200, height/2 + 125))
            self.screen.blit(title, (width/2 - 50, height/4))
            
            pygame.display.update()
            self.clock.tick(60)

    def game_loop(self):
        x = 500
        y = 550
        sprite_width = 32
        sprite_height = 32
        

        #Creates sprite from spritesheet
        sprite = pygame.image.load('skeleton.png').convert_alpha()
        sprite_sheet = SpriteSheet(sprite)

        #animation list
        an_list = []
        an_steps = 10
        frame = 0
        frame_delay = 20
        frame_counter = 0

        for i in range (an_steps):
            an_list.append(sprite_sheet.get_sprite(i, 32, 45, 3, black))

        
        run = True
        while run:
            self.screen.fill(black)
            
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

        #up, down, left, right keys move sprite in given direction
            keys = pygame.key.get_pressed()
            moving = False

            if keys[pygame.K_LEFT] and x > 0:
                x -= 2
                moving = True

            if keys[pygame.K_RIGHT] and x < width - sprite_width:
                x += 2
                moving = True

            if keys[pygame.K_UP] and y > 0:
                y -= 2
                moving = True
            if keys[pygame.K_DOWN] and y < height - sprite_height:
                y += 2
                moving = True

        #animates sprite movements/ cycles through frames
            if moving:
                frame_counter += 1
        
            if frame_counter >= frame_delay:
                frame = (frame + 1) % an_steps
                frame_counter = 0
        #draws sprite on screen
            self.screen.blit(an_list[frame], (x, y))
            pygame.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.Start_screen()

