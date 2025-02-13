import pygame
import spritesheet
import sys
from pygame.locals import *

pygame.init()

black = (0,0,0)
white = (255,255,255)
light = (192,192,192)
rect_color = (255,0,0)



# CREATING CANVAS 
canvas = pygame.display.set_mode((1200, 750), pygame.RESIZABLE) 

# TITLE OF CANVAS 
pygame.display.set_caption("Alien Game") 

width = canvas.get_width() 
    
height = canvas.get_height() 



def game():
    x = 500
    y = 550 


    sprite_width = 150
    sprite_height = 170

    
    sprite = pygame.image.load('skeleton.png').convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(sprite)


    #animation list
    an_list = []
    an_steps = 10
    frame = 0

    for x in range (an_steps):
        an_list.append(sprite_sheet.get_sprite(x, 32, 45, 3, black))


    #frame_1 = get_sprite(sprite, 1, 30, 35, 3, black)
    #frame_2 = get_sprite(sprite, 2, 30, 35, 3, black)

    run = True
    while run:
        canvas.fill(black)
        
        canvas.blit(an_list[frame], (x, y))

        #canvas.blit(frame_1, (0,0))
        #canvas.blit(frame_2, (30,70))

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if keys[pygame.K_LEFT] and x > 0:
            x -= 0.5
            
        if keys[pygame.K_RIGHT] and x < width - sprite_width:
            frame += 1
            x += 0.5

        if keys[pygame.K_UP] and y > 0:
            y -= 0.5
        
        if keys[pygame.K_DOWN] and y < height - sprite_height:
            y += 0.5

    

        #pygame.draw.rect(canvas, rect_color, pygame.Rect(x,y,rec_width,rec_height))
       
        


        pygame.display.update()


def Start_screen():

    font = pygame.font.Font('freesansbold.ttf', 32)

    exit = font.render('exit', True, white)
    begin = font.render('begin', True, white)
    title = font.render("Game Title", True, white)
    #textRect = pygame.Rect(525,550,150,90)
    #textRect.center = (550,550)



    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/4 <= mouse[0] <= width/4 + 200 and height/2 + 100 <= mouse[1] <= height/2+200: 
                    pygame.quit()
                    sys.ecit()
                if width/2 <= mouse[0] <= width/2 + 300 and height/2 + 100 <= mouse[1] <= height/2+200:
                    game()
        canvas.fill(black)
     

        mouse = pygame.mouse.get_pos()


        if width/4 <= mouse[0] <= width/4+200 and height/2 + 25 <= mouse[1] <= height/2+ 225: 
            pygame.draw.rect(canvas,light,[width/4 + 60, height/2 + 100, 150, 90])
        else:
            pygame.draw.rect(canvas, black, [width/4 + 60 , height/2 + 100, 150, 90])
        
            if width/2 <= mouse[0] <= width/2+300 and height/2 + 25 <= mouse[1] <= height/2+ 225: 
                pygame.draw.rect(canvas,light,[width/2 + 170,height/2 + 100,150,90])
            else:
                pygame.draw.rect(canvas, black, [width/4 + 170 , height/2 + 100, 150, 90]) 
     
        canvas.blit(exit, (width/4+100, height/2 + 125))
        canvas.blit(begin, (width/2+200, height/2 + 125))
        canvas.blit(title, (width/2 - 50, height/4))
        

        pygame.display.update() 

Start_screen()