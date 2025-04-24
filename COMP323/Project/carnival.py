import pygame
import sys
from spritesheet import *
from config import*
from nova_game import Player
from balloon_pop import *

class Carnival:
    def __init__(self,player):
        pygame.mixer.init()
        self.player = player
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()

        self.sounds = {
        'carnival':pygame.mixer.Sound('carnival.wav')
        }

        self.sounds['carnival'].set_volume(0.3)
        self.sounds['carnival'].play(loops=-1)


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
        admission_booth_sign = font.render('ADMISSION', True, black)
        pretzel_vendor_sign = font.render('PRETZELS', True, black)
        balloon_pop_sign = smaller_font.render('BALLOON POP', True, black)
        ticket_both_sign = smaller_font.render('TICKET BOOTH', True, black)

        sign_text = [pretzel_vendor_sign, balloon_pop_sign, ticket_both_sign]

        #booth rects for collision
        booth1 = pygame.Rect(width/4 - 90, height / 4 - 70, 110, 80) 
        booth2 = pygame.Rect(width/4 - 245, height / 2 + 34, 110, 80) #balloon
        booth3 = pygame.Rect(width/2 - 50, height / 4 - 4, 110, 80) #pretzel
        booth4 = pygame.Rect(width/3 + 15, height / 2 + 156, 110, 80) #ticket
        booth5 = pygame.Rect(width/2 + 60, height / 2 + 35, 110, 80)
        booth6 = pygame.Rect(width/2 + 415, height / 2 + 156, 110, 80)
        booth7 = pygame.Rect(width/2 + 540, height / 4 - 4, 60, 80)

        booths = [booth1, booth2, booth3, booth4, booth5, booth6, booth7]

        
        #Admission / booth 1
        admission_sign_clicked = False
        admission_prompt = False

        admission_booth = font.render('Get your tickets here!', True, white)

        #Petzel Vendor / booth3
        pretzel_sign_clicked = False
        pretzel_prompt = False
        pretzel_response_yes = False
        pretzel_response_no = False

        pretzel_vendor = font.render('Would you like a pretzel?', True, white)
        select = font.render('Press y or n', True, white)
        pretzel_response = font.render('Don\'t have any money!? Get out of my line!', True, white)
        pretzel_response2 = font.render('Why are you here?! Get out of my line!', True, white)

        #ticket booth / booth4
        ticket_sign_clicked = False
        ticket_prompt = False

        ticket_booth = font.render('Cool Costume!', True, white)


        run = True
        while run:
            self.screen.blit(background, (0,0))
            
            mouse = pygame.mouse.get_pos()
            key_pressed = pygame.key.get_pressed()

            if booth1.collidepoint(mouse) and admission_sign_clicked:
                if admission_prompt:
                    self.screen.blit(admission_booth, (width/4 - 200, height/4 - 100))
                    

            #check if sign is clicked
            if booth3.collidepoint(mouse) and pretzel_sign_clicked:
                #pretzel_prompt = True
                if pretzel_prompt:
                    self.screen.blit(pretzel_vendor, (width/4 + 100, height/4 - 100))
                    self.screen.blit(select, (width/4 + 100, height/4 - 85))
                
                    if key_pressed[pygame.K_y]:
                        pretzel_response_yes = True
                    
                    elif key_pressed[pygame.K_n]:
                        pretzel_response_no = True

                if pretzel_response_yes:
                        self.screen.blit(pretzel_response, (width/4 + 100, height/4 -70)) 
                elif pretzel_response_no:
                    self.screen.blit(pretzel_response2, (width/4 + 100, height/4 - 70))

            if booth4.collidepoint(mouse) and ticket_sign_clicked:
                #ticket_sign_clicked = True
                if ticket_prompt:
                    self.screen.blit(ticket_booth, (width/4 + 100, height/4 + 300))
                
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if booth1.collidepoint(mouse):
                            admission_sign_clicked = True
                            admission_prompt = True
                        if booth2.collidepoint(mouse):
                            balloon = BalloonGame()
                            balloon.run()
                        if booth3.collidepoint(mouse):
                            pretzel_sign_clicked = True
                            pretzel_prompt = True
                            pretzel_response_yes = False
                            pretzel_response_no = False
                        if booth4.collidepoint(mouse):
                            ticket_sign_clicked = True
                            ticket_prompt = True


            self.player.update()
            self.player.handle_collision(booths)

            for sign in signs:
                pygame.draw.rect(self.screen, tan, sign)

            for text in sign_text:
                self.screen.blit(pretzel_vendor_sign, (width/2 - 40, height / 3 - 47))
                self.screen.blit(balloon_pop_sign, (width/4 - 240, height / 2 + 50))
                self.screen.blit(ticket_both_sign, (width/3 + 15, height / 2 + 172))
                self.screen.blit(admission_booth_sign, (width/4 - 90, height / 4 - 50))

            
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