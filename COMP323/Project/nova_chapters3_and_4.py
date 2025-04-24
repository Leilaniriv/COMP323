#chapters 3 and 4
import pygame
import sys
from config import white, width, height

pygame.init()
screen = pygame.display.set_mode((width, height))

def load_images():
    global town_img, home_img
    town_img = pygame.image.load('town.jpeg').convert_alpha()
    home_img = pygame.image.load('home_background.jpeg').convert_alpha()

def display_text(screen, text, color, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def meet_grandma(screen):
    screen.fill((0, 0, 0))
    display_text(screen, "You meet Sally's grandma", white, 30, height - 40)


def eat_dinner(screen):
    screen.fill((0, 0, 0))
    display_text(screen, "You eat dinner with Sally and her grandma", white, 30, height - 40)

def go_to_bed(screen):
    screen.fill((0,0,0))
    display_text(screen, "They let you sleep on the couch", white, 30, height - 40)

def awaken(screen):
    screen.fill((0, 0, 0))
    display_text(screen, "You awaken feeling well rested, Granny sends you and Sally into town to mail a letter", white, 30, height - 40)

def agent_appears(screen):
    screen.fill((0, 0, 0))
    display_text(screen, "an agent appears at the door looking for you", white, 30, height - 40)

def grandma_convo(screen):
    screen.fill((0,0,0))
    display_text(screen, "granny smith sends him away ", white, 30, height - 40)

def arrive_at_town(screen):
    screen.fill((0,0,0))
    display_text(screen, "you arrive in the town with sally", white, 30, height - 40)

def contemplate(screen):
    screen.fill((0, 0, 0))
    display_text(screen, "you feel conflicted, are you feeling a connection with humans?", white, 30, height - 40)

def agent_appears2(screen):
    screen.fill((0, 0, 0))
    display_text(screen, "While in town, agent sully appears", white, 30, height - 40)

def distraction(screen):
    screen.fill((0, 0, 0))
    display_text(screen, "sally distracts him while you run into a nearby building", white, 30, height - 40)

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

run_chapter3_4(screen)


