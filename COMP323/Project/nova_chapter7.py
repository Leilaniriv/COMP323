#chapter 7 
#chapter 7 
import pygame
import sys
import random  # Import random for generating random positions
from nova_game import *


pygame.init()
screen = pygame.display.set_mode((width, height))
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

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x  # Use the provided x position
        self.rect.centery = y  # Use the provided y position
        self.speed_x = 0
        self.speed_y = 0
        self.last_fired = 0  # Track the last time the player fired
        self.fire_cooldown = 500  # Cooldown in milliseconds (e.g., 500ms)

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_a]:
            self.speed_x = -3
        if key_state[pygame.K_d]:
            self.speed_x = 3
        if key_state[pygame.K_w]:
            self.speed_y = -3
        if key_state[pygame.K_s]:
            self.speed_y = 3

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
        # Fire projectiles with a cooldown
        current_time = pygame.time.get_ticks()
        if current_time - self.last_fired >= self.fire_cooldown:
            projectile = Projectile(self.rect.right, self.rect.centery)  # Fire from the right side of the alien
            game_sprites.add(projectile)  # Add to game_sprites group
            projectiles.add(projectile)  # Add to projectiles group
            self.last_fired = current_time  # Update the last fired time

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

game_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

class NPC(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image  # Load the image
        self.rect = self.image.get_rect()
        self.rect.centerx = x  # Use the provided x position
        self.rect.centery = y  # Use the provided y position
        self.speed_x = 2
        self.speed_y = 2
        self.hit_count = 0 

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > width or self.rect.left < 0:
            self.speed_x = -self.speed_x

        self.rect.y += self.speed_y
        if self.rect.bottom > height or self.rect.top < 0:
            self.speed_y = -self.speed_y
    
    def check_collision(self, projectiles):
        # Check for collisions with projectiles
        hits = pygame.sprite.spritecollide(self, projectiles, True)  # Remove projectiles on collision
        self.hit_count += len(hits)  # Increment hit count
        if self.hit_count >= 5:  # Stop movement after 10 hits
            self.speed_x = 0
            self.speed_y = 0
            return True  # Indicate that the agent has been hit 10 times
        return False
    
    def fire(self):
        # Fire projectiles from the left side of the alien
        projectile = Projectile(self.rect.left, self.rect.top)
        game_sprites.add(projectile)
        projectiles.add(projectile)


class Chapter_7: 

    def choice(self, which_choice):
        chosen = " "
        if which_choice == 1:
            chosen = "bad_ending"
        elif which_choice == 2: 
            chosen = "good_ending"
        return chosen
    

    def __init__(self, player, npc_1, npc_2, npc_3):
        self.player = player
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.lab_bg = pygame.image.load("/COMP323/Project/assets/lab_background.png").convert_alpha()
        self.lab_bg = pygame.transform.scale(self.lab_bg, (width, height))

        self.sully_image = pygame.image.load('/COMP323/Project/assets/sully.jpeg').convert_alpha()
        self.sully_image = pygame.transform.scale(self.sully_image, (200, 200))
        
    
    def display_agents(self, npc_1, npc_2, npc_3):
        # Draw all agents
        self.screen.blit(self.lab_bg, (0, 0))  # Draw the background
        self.screen.blit(npc_1.image, npc_1.rect)  # Draw npc_1
        self.screen.blit(npc_2.image, npc_2.rect)  # Draw npc_2
        self.screen.blit(npc_3.image, npc_3.rect)  # Draw npc_3
        self.screen.blit(self.player.image, self.player.rect)  # Draw the player

    def display_sully(self):
        # Draw Sully (CIA agent)
        self.screen.blit(self.sully_image, (300, 300))

    def run_chapter7(self, choice):
        player = self.player
        running = True
        text_state = 0
        text_timer_start = pygame.time.get_ticks()  # Start the text timer
        show_agents = False
        show_sully = False  # Flag to track if Sully should be displayed

        while running: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    running = False

            # Draw the background
            self.screen.blit(self.lab_bg, (0, 0))  # Ensure the background is drawn first

            # Update and render the player
            player.update()  # Call the player's update method for movement
            self.screen.blit(player.image, player.rect)  # Draw the player sprite

            # Update and draw projectiles
            game_sprites.update()  # Update all projectiles
            game_sprites.draw(self.screen)  # Draw all projectiles on the screen

            # Handle firing logic
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                player.fire()  # Fire projectiles with cooldown

            # Display Sully if the flag is set
            if show_sully:
                self.display_sully()  # Keep Sully on the screen

            # Handle text display logic
            elapsed_time = pygame.time.get_ticks() - text_timer_start
            if text_state == 0:
                display_text(self.screen, "You find yourself back where your journey started...how will it end?", (255, 255, 255), 50, screen.get_height() - 100)
                if elapsed_time > 7000:
                    text_state = 1
                    text_timer_start = pygame.time.get_ticks()  # Reset the text timer when transitioning states

            elif text_state == 1:
                if choice == "good_ending":
                    display_text(self.screen, "You spared the agent. You realize the weight of a human life", (255, 255, 255), 50, screen.get_height() - 100)
                elif choice == "bad_ending":
                    display_text(self.screen, "You killed the agent. The weight of a human life means nothing to you.", (255, 255, 255), 50, screen.get_height() - 100)
                if elapsed_time > 7000:
                    text_state = 2
                    text_timer_start = pygame.time.get_ticks()

            elif text_state == 2:
                display_text(screen, "You hear voices outside the lab and then several agents walk in", (255, 255, 255), 30, screen.get_height() - 100)
                if elapsed_time > 7000:
                    text_state = 3
                    text_timer_start = pygame.time.get_ticks()
                    show_agents = True
            
            elif text_state == 3 and show_agents:
                if choice == "good_ending":
                    display_text(screen, "The agents walk in with agent Sully.", (255, 255, 255), 50, screen.get_height() - 100)
                elif choice == "bad_ending":
                    display_text(screen, "The agents walk in with rageful eyes. They seek vengeance for Sully.", (255, 255, 255), 30, screen.get_height() - 100)
                pygame.display.flip()  # Ensure the screen is updated
                if elapsed_time > 7000:  # Add a delay before transitioning
                    text_state = 4
                    text_timer_start = pygame.time.get_ticks()
                    show_sully = True  # Set the flag to keep Sully on the screen

            elif text_state == 4:
                display_text(self.screen, "Press space to fire at the agents until they are all hit 5 times.", (255, 255, 255), 30, screen.get_height() - 100)
                npc_1.update()
                npc_2.update()
                npc_3.update()
                self.screen.blit(npc_1.image, npc_1.rect)
                self.screen.blit(npc_2.image, npc_2.rect)
                self.screen.blit(npc_3.image, npc_3.rect)

                # Check collisions for all agents
                all_hit = (
                    npc_1.check_collision(projectiles) and
                    npc_2.check_collision(projectiles) and
                    npc_3.check_collision(projectiles)
                )

                if all_hit:
                    display_text(self.screen, "All agents defeated!", (255, 255, 255), 30, screen.get_height() - 150)
                    text_state = 5
                    text_timer_start = pygame.time.get_ticks()

            elif text_state == 5:
                display_text(self.screen, "You have defeated all the agents. What will you do next?", (255, 255, 255), 30, screen.get_height() - 100)
                if elapsed_time > 7000:
                    text_state = 6
                    text_timer_start = pygame.time.get_ticks()

            elif text_state == 6:
                display_options(screen, "Press 1: Spare the three agents (good ending only)", "Press 2: Kill the three agents (bad ending only)")
                selected_option = choose_option()
                if selected_option != 0:
                    if selected_option == 1 and choice == "good_ending":
                        display_text(screen, "You spare the agents. You've accepted you won't kill people.", (255, 255, 255), 50, screen.get_height() - 100)
                    elif selected_option == 2 and choice == "bad_ending":
                        display_text(screen, "You kill the agents. Their lives mean nothing to you.", (255, 255, 255), 30, screen.get_height() - 100)
                    text_state = 7
                    text_timer_start = pygame.time.get_ticks()

            elif text_state == 7:
                if selected_option == 1:
                    display_text(self.screen, "Sully looks at the agents and sighs...", (255, 255, 255), 50, screen.get_height() - 100)
                    if elapsed_time > 7000:
                        text_state = 8
                        text_timer_start = pygame.time.get_ticks()
                elif selected_option == 2:
                    display_text(screen, "You walk through the bloodshed and leave the lab to find your ship...", (255, 255, 255), 30, screen.get_height() - 100)
                    if elapsed_time > 7000:
                        text_state = 8
                        text_timer_start = pygame.time.get_ticks()
                
            elif text_state == 8:
                if selected_option == 1:
                    display_text(screen, "Sully asks you, 'if you were to leave this lab with your ship, where would you go?", (255, 255, 255), 30, screen.get_height() - 100)
                    if elapsed_time > 7000:
                        text_state = 9
                        text_timer_start = pygame.time.get_ticks()
                elif selected_option == 2:
                    pygame.quit()
                    sys.exit()
            
            elif text_state == 9:
                display_text(screen, "You're first instinct is to say your home planet, but really what you want is to go eat dinner with Sally and her family.", (255, 255, 255), 30, screen.get_height() - 100)
                if elapsed_time > 7000:
                    text_state = 10
                    text_timer_start = pygame.time.get_ticks()

            elif text_state == 10:
                display_text(screen, "Sully sighs, 'I wish I could treat you as a foreign creature, but you've treated me with respect...", (255, 255, 255), 30, screen.get_height() - 100)
                if elapsed_time > 7000:
                    text_state = 11
                    text_timer_start = pygame.time.get_ticks()
            
            elif text_state == 11: 
                display_text(screen, "He continues,'I owe you my life, so leave your ship and we won't come after you anymore.'", (255, 255, 255),30, screen.get_height() - 100)
                if elapsed_time > 7000:
                    text_state = 12
                    text_timer_start = pygame.time.get_ticks()

            elif text_state == 12:
                display_text(screen, "You've spent your whole journey trying to get your ship back to go home, but now you'd rather go back to Sally's house...", (255, 255, 255), 30, screen.get_height() - 100)
                if elapsed_time > 7000:
                    pygame.quit()
                    sys.exit()

            # Update the display
            pygame.display.flip()
            self.clock.tick(60)

# Initialize the player and NPCs
good_ending = "good_ending"
alien_image = pygame.image.load('alien.jpeg').convert_alpha()
alien_image = pygame.transform.scale(alien_image, (200, 200))  # Scale the alien image to 100x100 pixels
player = Player(alien_image, 100, 100)

npc_image = pygame.image.load("npc_agent.jpeg").convert_alpha()  # Load the NPC image
npc_image = pygame.transform.scale(npc_image, (200, 200))  # Scale the NPC image to 200x200 pixels
npc_1 = NPC(npc_image, 100, 200)
npc_2 = NPC(npc_image, 200, 200)  # Create another NPC with the same image
npc_3 = NPC(npc_image, 300, 200)  # Create a third NPC with the same image


# Run Chapter 7
chapter7 = Chapter_7(player, npc_1, npc_2, npc_3)
chapter7.run_chapter7(good_ending)