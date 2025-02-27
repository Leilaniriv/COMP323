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
        fontTitle = pygame.font.Font('freesansbold.ttf', 62)

        exit = font.render('exit', True, white)
        begin = font.render('begin', True, white)
        title = fontTitle.render("NOVA", True, white)

        exit_button = pygame.Rect(width/4 - 45, height/2 + 100, 150, 90)
        begin_button = pygame.Rect(width/2 + 270, height/2 + 100,150,90)

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
                        #running = False
                        self.game_loop()


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
        x = 500
        y = 550
        sprite_width = 32
        sprite_height = 32
        

        #Creates sprite from spritesheet
        sprite = pygame.image.load('skeletons.png').convert_alpha()
        sprite_sheet = SpriteSheet(sprite)

        #animation list
        an_list = []
        #left and right facing animations
        an_steps = [10,10]
        #tracks sprite action on spritesheet
        action = 0
        frame = 0
        frame_delay = 20
        frame_counter = 0
        step_counter = 0

        #runs through animation steps
        for animation in an_steps:
            #cycles through an_steps list appending to temp and back in order to loop through all animations
            temp_list = []
            for _ in range (animation):
                #sets frame to step_counter, width = 32, height = 45, scale = 3, color = black
                temp_list.append(sprite_sheet.get_sprite(step_counter, 32, 45, 3, black))
                step_counter += 1
            an_list.append(temp_list)

        
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
                #while moving left second set of animations in an_list used
                action = 1
                moving = True

            elif keys[pygame.K_RIGHT] and x < width - sprite_width:
                x += 2
                #while moving right first set of animations in an_list used
                action = 0
                moving = True
            else:
                frame = 0

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
                frame = (frame + 1) % len(an_list[action]) 
                frame_counter = 0

        #draws sprite on screen
            self.screen.blit(an_list[action][frame], (x, y))
            pygame.display.update()
            self.clock.tick(90)


if __name__ == "__main__":
    game = Game()
    game.Start_screen()

