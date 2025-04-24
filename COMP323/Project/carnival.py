import pygame
import sys
from spritesheet import *
from config import*
from nova_game import Player
#from balloon_pop import Balloon

class Carnival:
    def __init__(self,player):
        pygame.init()
        self.player = player
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()


    def carnival_scene(self):
        tan = (211, 167, 124)
        background = pygame.image.load('carnival.png').convert_alpha()
        background = pygame.transform.scale(background,(1200,750))

        font = pygame.font.Font('freesansbold.ttf', 18)
        smaller_font = pygame.font.Font('freesansbold.ttf', 14)
        
        #carnival signs
        sign1 = pygame.Rect(width/4 - 90, height / 4 - 60, 110, 30)
        sign2 = pygame.Rect(width/4 - 245, height / 2 + 44, 110, 30)
        sign3 = pygame.Rect(width/2 - 50, height / 3 - 55, 110, 30)
        sign4 = pygame.Rect(width/3 + 15, height / 2 + 166, 110, 30)
        sign5 = pygame.Rect(width/2 + 60, height / 2 + 45, 110, 30)
        sign6 = pygame.Rect(width/2 + 415, height / 2 + 166, 110, 30)
        sign7 = pygame.Rect(width/2 + 540, height / 4, 60, 30)

        signs = [sign1, sign2, sign3, sign4, sign5, sign6, sign7]

        #carnival sign text
        pretzel_vendor_sign = font.render('PRETZELS', True, black)
        balloon_pop_sign = smaller_font.render('BALLOON POP', True, black)
        ticket_both_sign = smaller_font.render('TICKET BOOTH', True, black)

        sign_text = [pretzel_vendor_sign, balloon_pop_sign]

        #booth rects for collision
        booth1 = pygame.Rect(width/4 - 90, height / 4 - 70, 110, 80) 
        booth2 = pygame.Rect(width/4 - 245, height / 2 + 34, 110, 80) #balloon
        booth3 = pygame.Rect(width/2 - 50, height / 4 - 4, 110, 80) #pretzel
        booth4 = pygame.Rect(width/3 + 15, height / 2 + 156, 110, 80) #ticket
        booth5 = pygame.Rect(width/2 + 60, height / 2 + 35, 110, 80)
        booth6 = pygame.Rect(width/2 + 415, height / 2 + 156, 110, 80)
        booth7 = pygame.Rect(width/2 + 540, height / 4 - 4, 60, 80)

        booths = [booth1, booth2, booth3, booth4, booth5, booth6, booth7]

        
        sign_clicked = False
        show_prompt = False
        press_yes = False
        press_no = False

        #Petzel Vendor
        pretzel_vendor = font.render('Would you like a pretzel?', True, white)
        select = font.render('Press y or n', True, white)
        pretzel_response = font.render('Dont have any money!? Get out of my line!', True, white)
        pretzel_response2 = font.render('Why are you here?! Get out of my line!', True, white)

        #costume
        ticket_booth = font.render('Cool Costume!', True, white)


        run = True
        while run:
            self.screen.blit(background, (0,0))
            
            mouse = pygame.mouse.get_pos()
            key_pressed = pygame.key.get_pressed()

            #check if sign is clicked
            if sign_clicked:
                if booth3.collidepoint(mouse):
                    show_prompt = True
                if show_prompt:
                    self.screen.blit(pretzel_vendor, (width/4, height/4))
                    self.screen.blit(select, (width/4, height/4 + 15))
                    
                    if key_pressed[pygame.K_y]:
                        show_prompt = False
                        press_yes = True
                    if press_yes:
                        self.screen.blit(pretzel_response, (width/4, height/4 + 30))
                    elif key_pressed[pygame.K_n]:
                        show_prompt = False
                        press_no = True
                    if press_no:
                        self.screen.blit(pretzel_response2, (width/4, height/4 + 30))
                    

                elif booth4.collidepoint(mouse):
                    show_prompt = True
                if show_prompt:
                    self.screen.blit(ticket_booth, (width/4 + 100, height/4 + 100))
                    
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if booth3.collidepoint(mouse):
                            sign_clicked = True
                            show_prompt = True
                        if booth4.collidepoint(mouse):
                            sign_clicked = True
                            show_prompt = True

                '''
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if booth2.collidepoint(mouse):
                        balloon = Balloon()
                        balloon.run()
                '''

            self.player.update()
            self.player.handle_collision(booths)

            for sign in signs:
                pygame.draw.rect(self.screen, tan, sign)

            for text in sign_text:
                self.screen.blit(pretzel_vendor_sign, (width/2 - 40, height / 3 - 47))
                self.screen.blit(balloon_pop_sign, (width/4 - 240, height / 2 + 50))
                self.screen.blit(ticket_both_sign, (width/3 + 15, height / 2 + 172))

            
            '''
            for booth in booths:
                pygame.draw.rect(self.screen, black, booth)
            '''
            

            
            #draw player
            self.screen.blit(self.player.image, self.player.rect.topleft)

        
            pygame.display.update()
            self.clock.tick(60)


    def run(self):
        self.carnival_scene()