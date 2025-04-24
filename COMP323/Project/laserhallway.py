import pygame
import sys
from spritesheet import *
from config import width, height, black, white

class LaserHallway:
    def __init__(self, player):
        pygame.init()
        self.player = player
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.hallway_bg = pygame.image.load("laserhallway.png").convert_alpha()
        self.hallway_bg = pygame.transform.scale(self.hallway_bg, (width, height))
        
        self.player.rect.x = 100
        self.player.rect.y = height // 2
        self.player_speed = 4

        

        self.lasers = [
            pygame.Rect(300, 50, 15, 300),
            pygame.Rect(450, 400, 15, 300),
            pygame.Rect(600, 100, 15, 300),
            pygame.Rect(750, 350, 15, 300),
            pygame.Rect(900, 200, 15, 300),
            pygame.Rect(1050, 100, 15, 300),
        ]
        self.laser_speeds = [4, -4, 5, -5, 4, -5]

        self.exit_zone = pygame.Rect(1100, 0, 100, height)
        self.hit_text = None
        self.hit_timer = 0

    def run(self):
        running = True
        font = pygame.font.Font('ByteBounce.ttf', 42)

        while running:
            self.screen.blit(self.hallway_bg, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Player movement
            keys = pygame.key.get_pressed()
            moving = False
                        
            if keys[pygame.K_w] and self.player.rect.top > 0:
                self.player.rect.y -= self.player_speed
                moving = True

            if keys[pygame.K_s] and self.player.rect.bottom < height:
                self.player.rect.y += self.player_speed
                moving = True

            if keys[pygame.K_a] and self.player.rect.left > 0:
                self.player.rect.x -= self.player_speed
                self.player.action = 1  # Left animation
                moving = True

            if keys[pygame.K_d] and self.player.rect.right < width:
                self.player.rect.x += self.player_speed
                self.player.action = 0  # Right animation
                moving = True

            # Update player animation
            self.player.update()

            # Laser movement
            for i, laser in enumerate(self.lasers):
                laser.y += self.laser_speeds[i]
                if laser.top <= 0 or laser.bottom >= height:
                    self.laser_speeds[i] *= -1

            # Draw lasers
            for laser in self.lasers:
                pygame.draw.rect(self.screen, (255, 0, 0), laser)

            # Draw exit zone
            pygame.draw.rect(self.screen, (0, 0, 255), self.exit_zone)

            self.screen.blit(self.player.image, self.player.rect)

            # Collision detection
            for laser in self.lasers:
                if self.player.rect.colliderect(laser):
                    self.hit_text = font.render("Hit by laser!", True, (255, 255, 255))
                    self.hit_timer = pygame.time.get_ticks()
                    self.player.rect.x, self.player.rect.y = 100, height // 2
                    break

            if self.player.rect.colliderect(self.exit_zone):
                print("Reached desert!")  # replace with scene switch
                return("desert")

            # Show "hit" text
            if self.hit_text and pygame.time.get_ticks() - self.hit_timer < 2000:
                self.screen.blit(self.hit_text, (width // 2 - 100, 50))
            elif self.hit_text:
                self.hit_text = None

            pygame.display.flip()
            self.clock.tick(60)
