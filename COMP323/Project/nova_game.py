
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
import pygame, sys, os

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
        self.image = pygame.Surface((30,30))
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 20
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speed_x = -1
        if key_state[pygame.K_RIGHT]:
            self.speed_x = 1
        if key_state[pygame.K_UP]:
            self.speed_y = -1
        if key_state[pygame.K_DOWN]:
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

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_sprite(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image


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

game_sprites = pygame.sprite.Group()
player = Player()
game_sprites.add(player)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()

    def gameLoop():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        
            screen.fill(white)
            game_sprites.draw(screen)
            pygame.display.flip()

            player.update()

Game.gameLoop()
pygame.quit()