#chapters 3 and 4
import pygame
import sys
from config import white, width, height

def load_images():
    global town_img, home_img
    town_img = pygame.image.load('town.jpeg').convert_alpha()
    home_img = pygame.image.load('home_background.jpeg').convert_alpha()

def meet_grandma(screen):
    screen.fill((0, 0, 0))

def eat_dinner(screen):
    screen.fill((0, 0, 0))

def go_to_bed(screen):
    screen.fill((0,0,0))

def awaken(screen):
    screen.fill((0, 0, 0))

def agent_appears(screen):
    screen.fill((0, 0, 0))

def grandma_convo(screen):
    screen.fill((0,0,0))

def arrive_at_town(screen):
    screen.fill((0,0,0))

def contemplate(screen):
    screen.fill((0, 0, 0))

def agent_appears2(screen):
    screen.fill((0, 0, 0))

def distraction(screen):
    screen.fill((0, 0, 0))

def display_text(screen, text, color, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def run_chapter3_4(screen):
    load_images()
    meet_grandma(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    eat_dinner(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    go_to_bed(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    awaken(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    agent_appears(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    grandma_convo(screen)
    pygame.display.update()
    pygame.time.wait(3000)
    arrive_at_town(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    contemplate(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    agent_appears2(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    distraction(screen)
    pygame.display.update()
    pygame.time.wait(3000)



