import pygame
from spritesheet import *
from carnival import *
import sys
from nova_game import player
from SpaceShip import SpaceshipPart


class Desert:
    def __init__(self, player):
        pygame.init()
        self.player = player
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.spaceship_part = SpaceshipPart(width//2, height//2, 1)
        self.show_prompt = False
        self.prompt_timer = 0
        self.prompt_font = pygame.font.Font('ByteBounce.ttf', 32)


        

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

        font = pygame.font.Font(None, 24)
        for i in range(4):
            color = (0, 255, 0) if self.player.collected_parts[i] else (255, 0, 0)
            text = font.render("Part 1", True, color)
            self.screen.blit(text, (10, 10 + i*30))

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
            if not self.spaceship_part.collected:
                self.screen.blit(self.spaceship_part.image, self.spaceship_part.rect)
                
                # Check for click
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1 and self.spaceship_part.rect.collidepoint(mouse):
                            self.spaceship_part.collected = True
                            self.show_prompt = True
                            self.prompt_timer = pygame.time.get_ticks()

            # Show prompt for 2 seconds
            if self.show_prompt:
                prompt_text = self.prompt_font.render("You found a piece of your spaceship!", True, white)
                text_rect = prompt_text.get_rect(center=(width//2, height//2))
                
                # Semi-transparent background for text
                prompt_bg = pygame.Surface((text_rect.width + 20, text_rect.height + 20), pygame.SRCALPHA)
                prompt_bg.fill((0, 0, 0, 150))
                self.screen.blit(prompt_bg, (text_rect.x - 10, text_rect.y - 10))
                
                self.screen.blit(prompt_text, text_rect)
                
                # Hide after 2 seconds
                if pygame.time.get_ticks() - self.prompt_timer > 2000:
                    self.show_prompt = False
            



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

