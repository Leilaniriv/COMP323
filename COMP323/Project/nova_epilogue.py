#epilogue 
import pygame
import sys
from nova_game import *

screen = pygame.display.set_mode((width, height))
pygame.init()

def load_images():
    global earth1, earth2, earth3, home, end_screen
    earth1 = pygame.image.load(os.path.join(img_dir,'bad_ending1.jpeg')).convert_alpha()
    earth1 = pygame.transform.scale(earth1, (width, height))
    earth2 = pygame.image.load(os.path.join(img_dir,'bad_ending2.jpeg')).convert_alpha()
    earth2 = pygame.transform.scale(earth2, (width, height))
    earth3 = pygame.image.load(os.path.join(img_dir,'bad_ending3.jpeg')).convert_alpha()
    earth3 = pygame.transform.scale(earth3, (width, height))
    home = pygame.image.load(os.path.join(img_dir,'good_ending.jpeg')).convert_alpha()
    home = pygame.transform.scale(home, (width, height))
    end_screen = pygame.image.load(os.path.join(img_dir,'nightsky.jpg')).convert_alpha()

def display_text(screen, text, color, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def show_earth(screen):
    screen.fill((0,0,0))
    screen.blit(earth1, (screen.get_width() // 2 - earth1.get_width() // 2, screen.get_height() // 2 - earth1.get_height() // 2))
    display_text(screen, "You found your ship and are heading to your home planet, earth looks so small from up here...", white, 30, screen.get_height() - 100)

def fire_laser(screen):
    screen.fill((0,0,0))
    screen.blit(earth2, (screen.get_width() // 2 - earth2.get_width() // 2, screen.get_height() // 2 - earth2.get_height() // 2))
    display_text(screen, "Humans are like ants to you, you want to forget about them...", white, 30, screen.get_height() - 100)

def explosion(screen):
    screen.fill((0,0,0))
    screen.blit(earth3, (screen.get_width() // 2 - earth3.get_width() // 2, screen.get_height() // 2 - earth3.get_height() // 2))
    display_text(screen, "You destroy their planet, what's a few more human lives to you...but you've got blood on your hands", white, 20, screen.get_height() - 100)

def display_home(screen):
    screen.fill((0,0,0))
    screen.blit(home, (screen.get_width() // 2 - home.get_width() // 2, screen.get_height() // 2 - home.get_height() // 2))
    display_text(screen, "You found your way back to Sally's house...", white, 30, screen.get_height() - 100)

def dinner(screen):
    screen.fill((0,0,0))
    screen.blit(home, (screen.get_width() // 2 - home.get_width() // 2, screen.get_height() // 2 - home.get_height() // 2))
    display_text(screen, "You and Sally watch TV while her grandma and brother make dinner. You feel at peace.", white, 30, screen.get_height() - 100) 

def end(screen):
    screen.fill((0,0,0))
    screen.blit(end_screen, (screen.get_width() // 2 - home.get_width() // 2, screen.get_height() // 2 - home.get_height() // 2))
    display_text(screen, "The End", white, screen.get_width() // 2 - 50, screen.get_height() // 2 - 20)
    pygame.display.update()
    pygame.time.wait(2000)  # Wait for 2 seconds before quitting
    pygame.quit()
    sys.exit()  

def run_good_ending(screen):
    load_images()
    display_home(screen)
    pygame.display.update()
    pygame.time.wait(3000)  # Wait for 3 seconds
    dinner(screen)
    pygame.display.update()
    pygame.time.wait(3000)  # Wait for 3 seconds
    end(screen)


def run_bad_ending(screen):
    load_images()
    show_earth(screen)
    pygame.display.update()
    pygame.time.wait(3000)  # Wait for 3 seconds
    fire_laser(screen)
    pygame.display.update()
    pygame.time.wait(3000)  # Wait for 3 seconds
    explosion(screen)
    pygame.display.update()
    pygame.time.wait(3000)  # Wait for 3 seconds
    end(screen)

#run_good_ending(screen)
run_bad_ending(screen)