import pygame
import sys
from spritesheet import *
from config import*

class Carnival:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()

    def carnival_scene(self):
        x = 500
        y = 400
        sprite_width = 32
        sprite_height = 32

        sprite = pygame.image.load('aliens.png').convert_alpha()
        sprite_sheet = SpriteSheet(sprite)

        #animation list
        an_list = []
        #left and right facing animations
        an_steps = [12,12]
        #tracks sprite action on spritesheet
        action = 0
        frame = 0
        frame_delay = 20
        frame_counter = 0
        step_counter = 0


        for animation in an_steps:
            #cycles through an_steps list appending to temp and back in order to loop through all animations
            temp_list = []
            for _ in range (animation):
                #sets frame to step_counter, width = 32, height = 45, scale = 3, color = black
                temp_list.append(sprite_sheet.get_sprite(step_counter, 26, 45, 1.75, black))
                step_counter += 1
            an_list.append(temp_list)

        run = True
        while run:


            background = pygame.image.load('carnival_background1.png').convert_alpha()
            background = pygame.transform.scale(background,(1200,750))
            self.screen.blit(background, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            #up, down, left, right keys move sprite in given direction
            keys = pygame.key.get_pressed()
            moving = False

            if keys[pygame.K_a] and x > 0:
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

            if keys[pygame.K_w] and y > 0:
                y -= 2
                moving = True

            if keys[pygame.K_s] and y < height - sprite_height:
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

