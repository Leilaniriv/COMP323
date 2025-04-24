import pygame
from spritesheet import *
from carnival import *
import sys
from nova_game import player


class Desert:
    def __init__(self, player):
        pygame.init()
        self.player = player
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def carnival_prompt(self):
        mouse = pygame.mouse.get_pos()
        font = pygame.font.Font('freesansbold.ttf', 18)

        #creates carnival prompt
        prompt = font.render('Would you like to visit the Carnival?', True, white)
        option1 = font.render('Yes', True, white)
        option2 = font.render('Definitely', True, white)

        optionbar = pygame.Rect(width/4, height / 2 + 200, 600, 100)
        option1_button = pygame.Rect(width/4 + 138, height / 2 + 240, 55, 40)
        option2_button = pygame.Rect(width/4 + 380, height / 2 + 240, 120, 40)

        pygame.draw.rect(self.screen, black, optionbar)
        pygame.draw.rect(self.screen, light, option1_button)
        pygame.draw.rect(self.screen, light, option2_button)

        self.screen.blit(prompt, (width/4 + 110, height/2 + 220))
        self.screen.blit(option1, (width/4 + 150 , height/2 + 250))
        self.screen.blit(option2, (width/4 + 400, height/2 + 250))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if option1_button.collidepoint(mouse) or option2_button.collidepoint(mouse):
                    #change to carnival scene
                    carnival = Carnival(player)
                    carnival.run()
                    #return("carnival")





    def desertescape(self):
        background = pygame.image.load('desert_background.jpeg').convert_alpha()
        background = pygame.transform.scale(background,(1200,750))

        carnival_sign = pygame.image.load('carnival_sign.png').convert_alpha()
        carnival_sign = pygame.transform.scale(carnival_sign, (100,120))

        font = pygame.font.Font("ByteBounce.ttf", 32)
        sign_instruction = font.render('Click the sign for more information', True, white)



        sign_clicked = False
        show_prompt = False

        run = True
        while run:
            mouse = pygame.mouse.get_pos()

            self.screen.blit(background, (0,0))
            self.screen.blit(sign_instruction, (width/4 + 50, height/4 + 50))



            #carnival sign
            carnival_sign_rect = pygame.Rect(width/2 + 300, height/2 - 35, 100, 70)
            #pygame.draw.rect(self.screen,black, carnival_sign_rect)
            self.screen.blit(carnival_sign, (width/2 + 300, height/2 - 40))

            #check if sign is clicked
            if carnival_sign_rect.collidepoint(mouse) and sign_clicked:
                show_prompt = True
            if show_prompt:
                self.carnival_prompt()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if carnival_sign_rect.collidepoint(mouse):
                            sign_clicked = True
                            show_prompt = True

            #import player movement and animation
            player.update()
            self.screen.blit(player.image, player.rect)

            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        self.desertescape()

def display_text(screen, text, color, x, y):
    font = pygame.font.Font("ByteBounce.ttf", 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def desertText1(screen):
    screen.fill((0, 0, 0))
    display_text(screen, "That was close...", (255, 255, 255), 30, screen.get_height() - 40)

def desertText2(screen):
    screen.fill((0, 0, 0))
    display_text(screen, "Let\'s go look at that sign", (255, 255, 255), 30, screen.get_height() - 40)


def run_desert_text(screen):
    desertText1(screen)
    pygame.display.update()
    pygame.time.wait(3000)
    desertText2(screen)
    pygame.display.update()
    pygame.time.wait(3000)

