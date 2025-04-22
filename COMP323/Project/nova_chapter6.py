#chapter 6
import pygame
import sys
from config import width, height
from spritesheet import SpriteSheet

pygame.init()
screen = pygame.display.set_mode((width, height))  # Initialize the display
black = (0,0,0)

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
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image  # Use the provided image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Chapter_6:
    def __init__(self, player, agent):
        self.player = player
        self.agent = agent
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.desert_bg = pygame.image.load("desert_background.jpeg").convert_alpha()
        self.desert_bg = pygame.transform.scale(self.desert_bg, (width, height))

        sprite = pygame.image.load('aliens.png').convert_alpha()
        sprite_sheet = SpriteSheet(sprite)

        # Animation setup
        self.an_list = []
        an_steps = [10, 10]
        step_counter = 0
        for animation in an_steps:
            temp_list = []
            for _ in range(animation):
                temp_list.append(sprite_sheet.get_sprite(step_counter, 32, 45, 3, black))
                step_counter += 1
            self.an_list.append(temp_list)

        self.action = 0
        self.frame = 0
        self.frame_delay = 20
        self.frame_counter = 0
    
    def display_agent(self):
        self.screen.blit(self.agent.image, self.agent.rect)  
       
    
    def update(self):
        keys = pygame.key.get_pressed()
        moving = False

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

            # Animate player
        if moving:
                self.frame_counter += 1
                if self.frame_counter >= self.frame_delay:
                    self.frame = (self.frame + 1) % len(self.an_list[self.action])
                    self.frame_counter = 0
        else:
                self.frame = 0

            # Draw alien
        self.screen.blit(self.an_list[self.action][self.frame], self.player.rect)
    

    def run(self):
        running = True
        show_agent = False
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

            # Handle agent display logic
            if not show_agent:
                # Calculate elapsed time
                elapsed_time = pygame.time.get_ticks() - agent_timer_start
                if elapsed_time > 5000:  # After 5 seconds, show the agent
                    show_agent = True

            if show_agent:
                self.display_agent()  # Render the agent

            # Update the display
            pygame.display.flip()
            self.clock.tick(60)

player = Player(pygame.image.load('aliens.png').convert_alpha(), width // 2, height // 2)
agent = NPC(pygame.image.load('agent.jpeg').convert_alpha(), 100, 100)
chapter6 = Chapter_6(player, agent)
chapter6.run()
