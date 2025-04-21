#chapter 4
import pygame
import sys
from config import white, width, height


pygame.init()
screen = pygame.display.set_mode((width, height))  # Initialize the display

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_x = 0
        self.speed_y = 0

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


# Initialize Player and NPC objects
player = Player(pygame.image.load('cute_alien.png').convert_alpha(), x=100, y=100)
npc = NPC(300, 200)

def load_images():
    #load images for this chapter
    global background_img, alien_img
    background_img = pygame.image.load('town.jpeg').convert_alpha()
    alien_img = pygame.image.load('cute_alien.png').convert_alpha()

def display_town_scene(screen):
    screen.fill((0,0,0))
    screen.blit(background_img, (screen.get_width() // 2 - background_img.get_width() // 2, screen.get_height() // 2 - background_img.get_height() // 2))
    display_text(screen, "You arrive in the town square.", (255, 255, 255), 30, screen.get_height() - 40)

def display_npc_conversation(screen, npc):
    screen.fill((0,0,0))

def display_player_action(screen, player):
    # Example of rendering the player
    screen.blit(player.image, (player.x, player.y))

def agent_appears(screen, npc, player):
    screen.fill((0,0,0))

def display_text(screen, text, color, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def run_chapter4(screen):
    print("Chapter 4 is running")
    load_images()
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape key pressed. Exiting game...")                   
                    pygame.quit() #pess Enter to end the chapter
                    sys.exit()  # Exit the chapter loop
                if event.key == pygame.K_RETURN:
                    print("Enter key pressed. Ending chapter...")
                    running = False
        

        # Render the town scene and update the display
        display_town_scene(screen)        
        player.update()
        screen.blit(player.image, player.rect)        
        pygame.display.flip()        
        clock.tick(60)        

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((width, height))  # Initialize the display
    print("About to run Chapter 4")
    run_chapter4(screen)  # Call Chapter 4

