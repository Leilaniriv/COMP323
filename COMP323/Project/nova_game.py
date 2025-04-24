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


        # Animate if moving
        if self.speed_x != 0 or self.speed_y != 0:
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.frame = (self.frame + 1) % len(self.an_list[self.action])
                self.frame_counter = 0
        else:
            self.frame = 0

        self.image = self.an_list[self.action][self.frame]

    def handle_collision(self, platforms):
        self.on_ground = False
        self.on_wall = False

        #horizontally
        self.rect.x += self.speed_x
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.speed_x > 0:
                    self.rect.right = platform.left
                elif self.speed_x < 0:
                    self.rect.left = platform.right

        #vertically 
        self.rect.y += self.speed_y
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.speed_y > 0:
                    self.rect.bottom = platform.top
                elif self.speed_y < 0:
                    self.rect.top = platform.bottom

        if self.rect.right > width: 
            self.rect.right = width 
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height


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

