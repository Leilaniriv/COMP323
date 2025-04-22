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

        self.alien_img = pygame.image.load("aliens.png").convert_alpha()
        self.alien_img = pygame.transform.scale(self.alien_img, (64, 90))

        self.player_rect = pygame.Rect(100, height // 2, 64, 90)
        self.player_speed = 4

        self.lasers = [
            pygame.Rect(300, 50, 15, 300),
            pygame.Rect(450, 400, 15, 300),
            pygame.Rect(600, 100, 15, 300),
            pygame.Rect(750, 350, 15, 300),
            pygame.Rect(900, 200, 15, 300),
            pygame.Rect(1050, 100, 15, 300),
        ]
        self.laser_speeds = [2, -2, 3, -3, 2, -3]

        self.exit_zone = pygame.Rect(1100, 0, 100, height)
        self.hit_text = None
        self.hit_timer = 0

    def run(self):
        running = True
        font = pygame.font.Font('freesansbold.ttf', 18)

        while running:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and self.player_rect.top > 0:
                self.player_rect.y -= self.player_speed
            if keys[pygame.K_s] and self.player_rect.bottom < height:
                self.player_rect.y += self.player_speed
            if keys[pygame.K_a] and self.player_rect.left > 0:
                self.player_rect.x -= self.player_speed
            if keys[pygame.K_d] and self.player_rect.right < width:
                self.player_rect.x += self.player_speed

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

            # Draw player
            self.screen.blit(self.alien_img, self.player_rect.topleft)

            # Collision detection
            for laser in self.lasers:
                if self.player_rect.colliderect(laser):
                    self.hit_text = font.render("Hit by laser!", True, (255, 255, 255))
                    self.hit_timer = pygame.time.get_ticks()
                    self.player_rect.x, self.player_rect.y = 100, height // 2
                    break

            if self.player_rect.colliderect(self.exit_zone):
                print("Reached desert!")  # replace with scene switch
                return("desert")

            # Show "hit" text
            if self.hit_text and pygame.time.get_ticks() - self.hit_timer < 2000:
                self.screen.blit(self.hit_text, (width // 2 - 100, 50))
            elif self.hit_text:
                self.hit_text = None

            pygame.display.flip()
            self.clock.tick(60)
