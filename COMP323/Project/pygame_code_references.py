import pygame, sys, os


# Initialize Pygame
pygame.init()
pygame.mixer.init()

game_dir = os.path.dirname(__file__)
assets_dir = os.path.join(game_dir, "assets")
img_dir = os.path.join(assets_dir, "images")

# Set up the display
winWidth = 800
winHeight = 600
FPS = 30

#variables
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Pygame Window")
clock = pygame.time.Clock()

#player sprite 
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill(CYAN)
        self.rect = self.image.get_rect()
        self.rect.centerx = winWidth / 2
        self.rect.bottom = winHeight - 20
        self.speed_x = 0
    
    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speed_x = -5
        if key_state[pygame.K_RIGHT]:
            self.speed_x = 5
        if key_state[pygame.K_UP]:
            self.speed_y = -5
        if key_state[pygame.K_DOWN]:
            self.speed_y= 5

        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y

        if self.rect.right > winWidth: 
            self.rect.right = winWidth 
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > winHeight:
            self.rect.bottom = winHeight
    
    def fire(self):
        projectile = Projectile(self.rect.centerx, self.rect.top)
        game_sprites.add(projectile)
        projectiles = pygame.sprite.Group()

    

class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,10))
        self.image.fill(RED)
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

    def __init__(self, x, y, color=(CYAN)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_x = 2
        self.speed_y = 2
    
    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > winWidth or self.rect.left < 0:
            self.speed_x = -self.speed_x

        self.rect.y += self.speed_y
        if self.rect.bottom > winHeight or self.rect.top < 0:
            self.speed_y = -self.speed_y

#define game quit and program exit
def gameExit():
    pygame.quit()
    sys.exit()

def textRender(surface, text, size, x, y):
    font = pygame.font.Font(font_match, size)
    text_surface = font.render(text, True, CYAN)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)
     
game_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
player = Player()
game_sprites.add(player)
font_match = pygame.font.match_font('arial')
# Create a group for NPCs
npcs = pygame.sprite.Group()

# Add NPCs to the group
npc1 = NPC(100, 100, color=(255, 0, 0))  # Red NPC
npc2 = NPC(300, 200, color=(0, 255, 0))  # Green NPC
npc3 = NPC(500, 400, color=(0, 0, 255))  # Blue NPC

npcs.add(npc1, npc2, npc3)


player_choices = {
    "option_1" : 0, 
    "option_2" : 0
}

# Main game loop
running = True
while running:
    #monitor fps and keep game running at set speed
    clock.tick(FPS)
    #'processing' inputs (events)
    for event in pygame.event.get():
        #check keyboard event -- keydown
        if event.type == pygame.KEYDOWN:
                
            #check for ESCAPE key to extit the game
            if event.key == pygame.K_ESCAPE:
                gameExit()
            
            if event.key == pygame.K_SPACE:
                player.fire()
            
            #option one has been chosen 
            if event.key == pygame.KSCAN_1:
                #change later
                player_choices["option_1"]  += 1
            
            if event.key == pygame.KSCAN_2:
                #change later
                player_choices["option_2"] += 1

    
                
    
    #'updating' the game

    #'rendering' to the window
    # Fill the screen with a color (e.g., white)
    screen.fill(WHITE)
    game_sprites.draw(screen)
    npcs.draw(screen)
    textRender(screen, str("Option 1: "), 16, winWidth / 4, 10)
    textRender(screen, str("Option 2: "), 16, winWidth /4 + 100,10 )

    # Update the display
    pygame.display.flip()

    player.update()
    game_sprites.update()
    projectiles.update()
    npcs.update()

# Quit Pygame
pygame.quit()