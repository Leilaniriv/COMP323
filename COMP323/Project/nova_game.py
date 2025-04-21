"""
GAME NAME: NOVA

Our choice based decision game. Play as an alien that crashlands onto 
Earth and take a good or bad path.

Main Game Loop:
-Game states: intro screen, prolouge, chapters, epilouge, game over
-Game objects: player, NPCS, projectiles
-User interface: prompts, dialogue 
-Asset management: sprites, sounds, background layers

Features: 
-Arrow keys: move left, right, up, down
-Points: good and bad points tracked based on choices



Game structure: 
-Player class: 
-Background class: 
-NPC class: 
-Projectile class: 
-Level Manager:
"""
import pygame
from spritesheet import *
import sys
from pygame.locals import *
from config import *
from prologue import run_prologue
from tanklevel import LevelTank

black = (0,0,0)
white = (255,255,255)
light = (192,192,192)

# TITLE OF CANVAS 
pygame.display.set_caption("Nova")

width = 1200 
    
height = 750

screen = pygame.display.set_mode((width, height))

TILESIZE = 32
#15 blocks high, 20 blocks wide represented by B. P represents player
# the dots represent empty space, the scattered B's represent obstacles
tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B.................B',
    'B...BB............B',
    'B.................B',
    'B.................B',
    'B.................B',
    'B.................B',
    'B........P........B',
    'B.................B',
    'B.................B',
    'B.................B',
    'B.................B',
    'B............B....B',
    'B.................B',
    'B.................B',
    'BBBBBBBBBBBBBBBBBBBB'
]


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Load sprite sheet and animation frames
        sprite = pygame.image.load('aliens.png').convert_alpha()
        sprite_sheet = SpriteSheet(sprite)

        self.an_list = []
        an_steps = [10, 10]  # Right, Left
        step_counter = 0
        for animation in an_steps:
            temp_list = []
            for _ in range(animation):
                temp_list.append(sprite_sheet.get_sprite(step_counter, 32, 45, 3, black))
                step_counter += 1
            self.an_list.append(temp_list)

        self.action = 0  # 0 = right, 1 = left
        self.frame = 0
        self.frame_delay = 20
        self.frame_counter = 0

        # Set first image and rect
        self.image = self.an_list[self.action][self.frame]
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 20

        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        key_state = pygame.key.get_pressed()

        if key_state[pygame.K_a]:
            self.speed_x = -1
            self.action = 1
        if key_state[pygame.K_d]:
            self.speed_x = 1
            self.action = 0
        if key_state[pygame.K_w]:
            self.speed_y = -1
        if key_state[pygame.K_s]:
            self.speed_y = 1

        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y

        if self.rect.right > width: 
            self.rect.right = width 
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

        # Animate if moving
        if self.speed_x != 0 or self.speed_y != 0:
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.frame = (self.frame + 1) % len(self.an_list[self.action])
                self.frame_counter = 0
        else:
            self.frame = 0

        self.image = self.an_list[self.action][self.frame]

class Block(pygame.sprite.Sprite): #tile map
    def __init__(self, game, x, y):
        self.game = game
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x* TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE


        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,10))
        self.image.fill(255, 0, 0)
        self.rect = self.image.get_rect()
        #weapon fired from front (top) of player sprite...
        self.rect.bottom = y
        self.rect.centerx = x
        #speed of projectile up the screen 
        self.speed_y = -10
    
    def update(self):
        #update y relative to speed of projectile on y-axis
        self.rect.y += self.speed_y
        #remove from game window - if it goes beyond bounding for y-axis at top...
        if self.rect.bottom < 0:
            self.kill()

class NPC(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_x = 2
        self.speed_y = 2
    
    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > width or self.rect.left < 0:
            self.speed_x = -self.speed_x

        self.rect.y += self.speed_y
        if self.rect.bottom > height or self.rect.top < 0:
            self.speed_y = -self.speed_y

game_sprites = pygame.sprite.Group()
player = Player()
game_sprites.add(player)
sally = NPC(100, 100)
game_sprites.add(sally)

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
    
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
                        pygame.time.wait(500)
                        run_prologue(self.screen)
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
        from tanklevel import LevelTank

        tanklevel = LevelTank(player)
        tanklevel.run()

        
        x = 500
        y = 400
        sprite_width = 32
        sprite_height = 32

        sprite = pygame.image.load('aliens.png').convert_alpha()
        sprite_sheet = SpriteSheet(sprite)
        an_list = []
        an_steps = [10,10]
        action = 0
        frame = 0
        frame_delay = 20
        frame_counter = 0
        step_counter = 0

        for animation in an_steps:
            temp_list = []
            for _ in range(animation):
                temp_list.append(sprite_sheet.get_sprite(step_counter, 32, 45, 3, black))
                step_counter += 1
            an_list.append(temp_list)

        running = True

        while running:

            mouse = pygame.mouse.get_pos()

            font = pygame.font.Font('freesansbold.ttf', 18)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

            background = pygame.image.load('desert_background.jpeg').convert_alpha()
            background = pygame.transform.scale(background,(1200,750))
            self.screen.blit(background, (0,0))

            #add carnival sign eventually
            carnival_sign = pygame.Rect(width/2 + 300, height/2 - 50, 150, 90)
            pygame.draw.rect(self.screen,black, carnival_sign)

            optionbar = pygame.Rect(width/4, height / 2 + 200, 600, 100)

            prompt = font.render('Would you like to visit the Carnival?', True, white)

            option1 = font.render('Yes', True, white)
            option2 = font.render('No', True, white)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                        sys.exit()
            

                if event.type == MOUSEBUTTONDOWN:
                    if carnival_sign.collidepoint(mouse):
                        pygame.draw.rect(self.screen, black, optionbar)
                        self.screen.blit(prompt, (width/4 + 110, height/2 + 220))
                        self.screen.blit(option1, (width/4 + 150 , height/2 + 250))
                        self.screen.blit(option2, (width/4 + 400, height/2 + 250))
                        pygame.display.update()
                        self.clock.tick(60)

            self.screen.blit(player.image, player.rect)
            pygame.display.update()
            self.clock.tick(90)
            player.update()
            sally.update()

game = Game()
game.Start_screen()
game.game_loop()
pygame.quit()
