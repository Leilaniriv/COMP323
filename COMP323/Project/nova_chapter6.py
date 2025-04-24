#chapter 6
import pygame
import sys
import random  # Import random for random movement
from config import width, height
from spritesheet import SpriteSheet
from config import width, height

pygame.init()
screen = pygame.display.set_mode((width, height))  # Initialize the display
black = (0,0,0)
    
def display_options(screen, option1, option2):
    font = pygame.font.Font(None, 36)
    color1 = (255,255,255) 
    color2 = (255,255,255)
    text1 = font.render(option1, True, color1)
    text2 = font.render(option2, True, color2)
    screen.blit(text1, (30, screen.get_height() - 80))
    screen.blit(text2, (30, screen.get_height() - 40))

def choose_option():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        return 1
    elif keys[pygame.K_2]:
        return 2
    return 0

def display_text(screen, text, color, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 5))  # Adjusted dimensions for horizontal movement
        self.image.fill((255, 0, 0))  # Red color for the projectile
        self.rect = self.image.get_rect()
        self.rect.left = x  # Start at the left side of the alien
        self.rect.centery = y  # Align vertically with the alien
        self.speed_x = -10  # Move left along the x-axis

    def update(self):
        self.rect.x += self.speed_x  # Update x position
        if self.rect.right < 0:  # Remove projectile if it goes off the left edge
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x  # Use the provided x position
        self.rect.centery = y  # Use the provided y position
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
    
    def fire(self):
        # Fire projectiles from the left side of the alien
        projectile = Projectile(self.rect.left, self.rect.top)
        game_sprites.add(projectile)
        projectiles.add(projectile)
        

game_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

class NPC(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image  # Use the provided image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.choice([-2, 2])  # Random initial horizontal speed
        self.speed_y = random.choice([-2, 2])  # Random initial vertical speed
        self.hit_count = 0  # Track the number of hits

    def update(self):
        # Move the agent randomly
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Reverse direction if hitting screen boundaries
        if self.rect.right > width or self.rect.left < 0:
            self.speed_x = -self.speed_x
        if self.rect.bottom > height or self.rect.top < 0:
            self.speed_y = -self.speed_y

    def check_collision(self, projectiles):
        # Check for collisions with projectiles
        hits = pygame.sprite.spritecollide(self, projectiles, True)  # Remove projectiles on collision
        self.hit_count += len(hits)  # Increment hit count
        if self.hit_count >= 30:  # Stop movement after 10 hits
            self.speed_x = 0
            self.speed_y = 0
            return True  # Indicate that the agent has been hit 10 times
        return False
    
    def fire(self):
        # Fire projectiles from the left side of the alien
        projectile = Projectile(self.rect.left, self.rect.top)
        game_sprites.add(projectile)
        projectiles.add(projectile)

class Chapter_6:
    def __init__(self, player, agent):
        self.player = player
        self.agent = agent
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.desert_bg = pygame.image.load("desert_background.jpeg").convert_alpha()
        self.desert_bg = pygame.transform.scale(self.desert_bg, (width, height))

   
    
    def display_agent(self):
        self.screen.blit(self.agent.image, self.agent.rect)  
       
    
    def update(self):
        keys = pygame.key.get_pressed()
        moving = False

        # Movement after tank breaks
       
        self.screen.blit(self.desert_bg, (0, 0))

            # Movement controls
        if keys[pygame.K_a] and self.player.rect.left > 0:
                self.player.rect.x -= 2
                self.action = 1
                moving = True
        elif keys[pygame.K_d] and self.player.rect.right < width:
                self.player.rect.x += 2
                self.action = 0
                moving = True

        if keys[pygame.K_w] and self.player.rect.top > 0:
                self.player.rect.y -= 2
                moving = True
        elif keys[pygame.K_s] and self.player.rect.bottom < height:
                self.player.rect.y += 2
                moving = True
    
    
    def display_agent(self, agent):
        self.screen.blit(self.agent.image, self.agent.rect)  

    def run(self):
        player = self.player
        agent = self.agent
        running = True
        show_agent = False
        text_state = 0
        agent_timer_start = pygame.time.get_ticks()  # Record the start time for the agent timer

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    running = False

            # Draw the background
            self.screen.blit(self.desert_bg, (0, 0))

            # Update and render the player
            self.update()
            player.update()
            self.screen.blit(player.image, player.rect)  # Draw the player sprite

            # Update and draw projectiles
            game_sprites.update()  # Ensure projectiles are updated
            game_sprites.draw(self.screen)  # Draw projectiles on the screen

            # Handle agent display logic
            if not show_agent:
                # Calculate elapsed time
                elapsed_time = pygame.time.get_ticks() - agent_timer_start
                if elapsed_time > 5000:  # After 5 seconds, show the agent
                    show_agent = True
                    text_timer_start = pygame.time.get_ticks()  # Start the text timer

            if show_agent:
                self.display_agent(agent)  # Render the agent

                # Handle text display logic
                elapsed_time = pygame.time.get_ticks() - text_timer_start
                if text_state == 0:
                    display_text(screen, "Once again you encounter agent Sully", (255, 255, 255), 50, screen.get_height() - 100)
                    if elapsed_time > 7000:  # After 7 seconds, move to the next text state
                        text_state = 1
                        text_timer_start = pygame.time.get_ticks()  # Reset the text timer
                elif text_state == 1:
                    display_text(screen, "He says,'I've finally caught up to you It's time to pay for the chaos you've caused'.", (255, 255, 255), 50, screen.get_height() - 100)
                    if elapsed_time > 7000:
                        text_state = 2
                        text_timer_start = pygame.time.get_ticks()
                elif text_state == 2:
                    display_options(screen, "Press 1: Try to reason with him", "Press 2: Provoke him")
                    selected_option = choose_option()  # Continuously check for key presses
                    if selected_option != 0:
                        text_state = 3  # Use assignment, not comparison
                        text_timer_start = pygame.time.get_ticks()
                elif text_state == 3:
                    if selected_option == 1:
                        display_text(screen, "You try to reason with him, he hesitates. He tells you it's his job to bring you in.", (255, 255, 255), 50, screen.get_height() - 100)
                        if elapsed_time > 7000:
                            text_state = 4
                            text_timer_start = pygame.time.get_ticks()
                            selected_option = 0  # Reset
                    elif selected_option == 2:
                        display_text(screen, "You provoke him. He's enraged and tells you that he will finish his job.", (255, 255, 255), 50, screen.get_height() - 100)
                        if elapsed_time > 7000:
                            text_state = 4
                            text_timer_start = pygame.time.get_ticks()
                            selected_option = 0  # Reset
                elif text_state == 4:
                    display_text(screen, "You tell him you will not go with him peacefully. He nods and pulls out his weapon.", (255, 255, 255), 50, screen.get_height() - 100)
                    if elapsed_time > 7000:
                        text_state = 5
                        text_timer_start = pygame.time.get_ticks()
                elif text_state == 5:
                    display_text(screen, "Press space to fire.", (255, 255, 255), 50, screen.get_height() - 100)
                    agent.fire()
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        self.player.fire()
                        # Start agent movement and collision detection after this point
                        agent.update()
                        if agent.check_collision(projectiles):
                            display_text(self.screen, "Agent defeated!", (255, 255, 255), 50, screen.get_height() - 150)
                            text_state = 6
                elif text_state == 6:
                    display_text(screen, "The agent lies defeated. You feel immense power over him, but Sally flashes in your mind.", (255, 255, 255), 50, screen.get_height() - 100)
                    if elapsed_time > 7000:
                        text_state = 7
                        text_timer_start = pygame.time.get_ticks()
                elif text_state == 7:
                    display_options(screen,"Press 1: Spare him", "Press 2: Kill him")
                    selected_option = choose_option()
                    if selected_option != 0:
                        text_state = 8  # Use assignment, not comparison
                        text_timer_start = pygame.time.get_ticks()
                elif text_state == 8:
                    if selected_option == 1:
                        display_text(screen, "You spare him, the priest's words echo in your mind. Agent Sully looks surprised.", (255, 255, 255), 50, screen.get_height() - 100)
                        if elapsed_time > 7000:
                            text_state = 9
                            text_timer_start = pygame.time.get_ticks()
                    elif selected_option == 2: 
                        display_text(screen, "You kill him, his body goes limp. You've reached the point of no return.", (255, 255, 255), 50, screen.get_height() - 100)
                        if elapsed_time > 7000:
                            text_state = 9
                            text_timer_start = pygame.time.get_ticks()
                elif text_state == 9:
                    display_text(screen, "His reinforcments arrive and take you back to the facility...", (255, 255, 255), 50, screen.get_height() - 100)
                    if elapsed_time > 7000:
                        pygame.quit()
                        sys.exit()
                        
            # Update the display
            pygame.display.flip()
            self.clock.tick(60)


agent = NPC(pygame.image.load('sully.jpeg').convert_alpha(), 100, 100)
agent.image = pygame.transform.scale(agent.image, (200, 200))  # Scale the agent image to 200x200 pixels

from nova_game import Player
player = Player()
player.rect.center = (100, 100)
chapter6 = Chapter_6(player, agent)
chapter6.run()