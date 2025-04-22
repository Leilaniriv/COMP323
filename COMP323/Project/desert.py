import pygame
from spritesheet import *
from carnival import *
import sys


class Desert:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def carnival_prompt(self):
        mouse = pygame.mouse.get_pos()
        font = pygame.font.Font('freesansbold.ttf', 18)
        
        optionbar = pygame.Rect(width/4, height / 2 + 200, 600, 100)

        prompt = font.render('Would you like to visit the Carnival?', True, white)

        option1 = font.render('Yes', True, white)
        option1_button = pygame.Rect(width/4 + 138, height / 2 + 240, 60, 40)

        option2 = font.render('No', True, white)
        option2_button = pygame.Rect(width/4 + 380, height / 2 + 240, 60, 40)


        pygame.draw.rect(self.screen, black, optionbar)

        self.screen.blit(prompt, (width/4 + 110, height/2 + 220))

        pygame.draw.rect(self.screen, light, option1_button)
        self.screen.blit(option1, (width/4 + 150 , height/2 + 250))
        

        pygame.draw.rect(self.screen, light, option2_button)
        self.screen.blit(option2, (width/4 + 400, height/2 + 250))
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if option1_button.collidepoint(mouse):
                    #change to carnival scene
                    Carnival.carnival_scene(self)

                if option2_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()
            
    def desertescape(self):
        x = 500
        y = 400
        sprite_width = 32
        sprite_height = 32
        

        #Creates sprite from spritesheet
        sprite = pygame.image.load('aliens.png').convert_alpha()
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
        
        sign_clicked = False
        show_prompt = False

        
        run = True
        while run:
            mouse = pygame.mouse.get_pos()

            font = pygame.font.Font('freesansbold.ttf', 18)

            background = pygame.image.load('desert_background.jpeg').convert_alpha()
            background = pygame.transform.scale(background,(1200,750))
            self.screen.blit(background, (0,0))

            #add carnival sign eventually
            carnival_sign = pygame.Rect(width/2 + 300, height/2 - 50, 150, 90)
            pygame.draw.rect(self.screen,black, carnival_sign)

            optionbar = pygame.Rect(width/4, height / 2 + 200, 600, 100)

            if carnival_sign.collidepoint(mouse) and sign_clicked:
                show_prompt = True
                #if show_prompt:
                    #self.carnival_prompt()
            if show_prompt:
                self.carnival_prompt()

        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if carnival_sign.collidepoint(mouse):
                            sign_clicked = True
                            show_prompt = True
  


            #up, down, left, right keys move sprite in given direction
            keys = pygame.key.get_pressed()
            moving = False

            if keys[pygame.K_a] and x > width/4:
                x -= 2
                #while moving left second set of animations in an_list used
                action = 1
                moving = True

            elif keys[pygame.K_d] and x < width - sprite_width:
                x += 2
                #while moving right first set of animations in an_list used
                action = 0
                moving = True
            else:
                frame = 0

            if keys[pygame.K_w] and y > height/2:
                y -= 2
                moving = True

            if keys[pygame.K_s] and y < height /2 + 200:
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

    def run(self):
        self.desertescape()