import pygame
import sys
from nova_game import *


def load_images():
    # Load images for each scene
    global crash_img, alien_img, vehicle_img, tank_img
    crash_img = pygame.image.load(os.path.join(img_dir,'crash_img.png')).convert_alpha()
    alien_img = pygame.image.load(os.path.join(img_dir,'alien_img.png')).convert_alpha()
    vehicle_img = pygame.image.load(os.path.join(img_dir,'vehicle_img.png')).convert_alpha()
    tank_img = pygame.image.load(os.path.join(img_dir,'tank_img.png')).convert_alpha()

def display_crash_landing(screen):
    screen.fill((0, 0, 0)) 
    screen.blit(crash_img, (screen.get_width() // 2 - crash_img.get_width() // 2, screen.get_height() // 2 - crash_img.get_height() // 2))
    display_text(screen, "A mysterious object crashes on Earth...", (255, 255, 255), 30, screen.get_height() - 40)

def display_alien_unconscious(screen):
    screen.fill((0, 0, 0))
    screen.blit(alien_img, (screen.get_width() // 2 - alien_img.get_width() // 2, screen.get_height() // 2 - alien_img.get_height() // 2))
    display_text(screen, "The alien lies unconscious, unaware of its fate...", (255, 255, 255), 30, screen.get_height() - 40)

def display_transport_to_facility(screen):
    screen.fill((0, 0, 0))
    screen.blit(vehicle_img, (screen.get_width() // 2 - vehicle_img.get_width() // 2, screen.get_height() // 2 - vehicle_img.get_height() // 2))
    display_text(screen, "Taken to a secret government facility...", (255, 255, 255), 30, screen.get_height() - 40)

def display_alien_in_tank(screen):
    screen.fill((0, 0, 0))
    screen.blit(tank_img, (screen.get_width() // 2 - tank_img.get_width() // 2, screen.get_height() // 2 - tank_img.get_height() // 2))
    display_text(screen, "You wake up in a containment tank. Time to escape!", (255, 255, 255), 30, screen.get_height() - 40)

def display_text(screen, text, color, x, y):
    font = pygame.font.Font("ByteBounce.ttf", 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def run_prologue(screen):
    load_images()
    display_crash_landing(screen)
    pygame.display.update()
    pygame.time.wait(3000)  # Wait for 3 seconds
    display_alien_unconscious(screen)
    pygame.display.update()
    pygame.time.wait(3000)
    display_transport_to_facility(screen)
    pygame.display.update()
    pygame.time.wait(3000)
    display_alien_in_tank(screen)
    pygame.display.update()
    pygame.time.wait(3000)

