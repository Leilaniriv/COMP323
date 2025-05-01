#chapters 3 and 4
import pygame
import sys
from nova_game import *
from nova_chapter5 import run_chapter5

pygame.init()
screen = pygame.display.set_mode((width, height))
exit_zone = pygame.Rect(1100, 0, 100, height)



if pygame.event.get(pygame.QUIT):
    pygame.quit()
    sys.exit()

def load_images():
    global town_img, home_img, meet_sally_img, meet_grandma_img, sully_appears_img, in_town_img, sully_appears_again_img
    town_img = pygame.image.load(os.path.join(img_dir,'town.jpeg')).convert_alpha()
    town_img = pygame.transform.scale(town_img, (width, height))  # Scale to fit the screen
    home_img = pygame.image.load(os.path.join(img_dir,'home_background.jpeg')).convert_alpha()
    home_img = pygame.transform.scale(home_img, (width, height))  # Scale to fit the screen
    meet_sally_img = pygame.image.load(os.path.join(img_dir,'meet_sally_bg.jpeg')).convert_alpha()
    meet_sally_img = pygame.transform.scale(meet_sally_img, (width, height))  # Scale to fit the screen
    meet_grandma_img = pygame.image.load(os.path.join(img_dir,'granny.jpeg')).convert_alpha()
    meet_grandma_img = pygame.transform.scale(meet_grandma_img, (width, height))  # Scale to fit the screen
    sully_appears_img = pygame.image.load(os.path.join(img_dir,'sully_appears.jpeg')).convert_alpha()
    sully_appears_img = pygame.transform.scale(sully_appears_img, (width, height))  # Scale to fit the screen
    in_town_img = pygame.image.load(os.path.join(img_dir,'town_with_no_Sully.jpeg')).convert_alpha()
    in_town_img = pygame.transform.scale(in_town_img, (width, height))  # Scale to fit the screen
    sully_appears_again_img = pygame.image.load(os.path.join(img_dir,'town_with_sully.jpeg')).convert_alpha()
    sully_appears_again_img = pygame.transform.scale(sully_appears_again_img, (width, height))  # Scale to fit the screen


def display_text(screen, text, color, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def meet_sally(screen):
    screen.fill((0, 0, 0))
    screen.blit(meet_sally_img, (0, 0))  # Display the scaled image
    display_text(screen, "A small human walks up to you...", white, 20, screen.get_height() - 300)
    pygame.display.update()  # Update the screen
    pygame.time.wait(5000)
    display_text(screen, "She asks you,'Can you help me find my home?'", white, 20, screen.get_height() - 250)
    pygame.display.update()  # Update the screen
    pygame.time.wait(5000)
    display_text(screen, "You ask her what she is and she says she's Sally", white, 20, screen.get_height() - 200)
    pygame.display.update()  # Update the screen
    pygame.time.wait(5000)
    display_text(screen, "You need to find your ship, but you are tired and you can exploit Sally for resources...", white, 20, screen.get_height() - 150)
    pygame.display.update()  # Update the screen
    pygame.time.wait(5000)
    display_text(screen, "You decide to help her but it takes both of you two hours because neither of you know anything", white, 10, screen.get_height() -  100)
    pygame.display.update()  # Update the screen
    pygame.time.wait(5000)

def meet_grandma(screen):
    screen.fill((0, 0, 0))
    screen.blit(meet_grandma_img, (screen.get_width() // 2 - meet_grandma_img.get_width() // 2, screen.get_height() // 2 - meet_grandma_img.get_height() // 2))
    display_text(screen, "You meet Sally's grandma", white, 30, height - 40)


def eat_dinner(screen):
    screen.fill((0, 0, 0))
    screen.blit(meet_grandma_img, (screen.get_width() // 2 - meet_grandma_img.get_width() // 2, screen.get_height() // 2 - meet_grandma_img.get_height() // 2))
    display_text(screen, "You eat dinner with Sally and her grandma (not pictured)", white, 30, height - 40)

def go_to_bed(screen):
    screen.fill((0,0,0))
    screen.blit(meet_grandma_img, (screen.get_width() // 2 - meet_grandma_img.get_width() // 2, screen.get_height() // 2 - meet_grandma_img.get_height() // 2))
    display_text(screen, "They let you sleep on the couch (not pictured)", white, 30, height - 40)


def agent_appears(screen):
    screen.fill((0, 0, 0))
    screen.blit(sully_appears_img, (screen.get_width() // 2 - sully_appears_img.get_width() // 2, screen.get_height() // 2 - sully_appears_img.get_height() // 2))
    display_text(screen, "an agent appears at the door looking for you", white, 30, height - 40)


def grandma_convo(screen):
    screen.fill((0,0,0))
    screen.blit(sully_appears_img, (screen.get_width() // 2 - sully_appears_img.get_width() // 2, screen.get_height() // 2 - sully_appears_img.get_height() // 2))
    display_text(screen, "granny smith sends him away ", white, 30, height - 40)


def arrive_at_town(screen):
    screen.fill((0,0,0))
    screen.blit(in_town_img, (screen.get_width() // 2 - meet_grandma_img.get_width() // 2, screen.get_height() // 2 - in_town_img.get_height() // 2))
    display_text(screen, "you arrive in the town with sally to mail a letter for her granny", white, 30, height - 40)


def contemplate(screen):
    screen.fill((0, 0, 0))
    screen.blit(in_town_img, (screen.get_width() // 2 - in_town_img.get_width() // 2, screen.get_height() // 2 - in_town_img.get_height() // 2))
    display_text(screen, "you feel conflicted, are you feeling a connection with humans?", white, 30, height - 40)


def agent_appears2(screen):
    screen.fill((0, 0, 0))
    screen.blit(sully_appears_again_img, (screen.get_width() // 2 - sully_appears_again_img.get_width() // 2, screen.get_height() // 2 - sully_appears_again_img.get_height() // 2))
    display_text(screen, "While in town, agent sully appears", white, 30, height - 40)


def distraction(screen):
    screen.fill((0, 0, 0))
    screen.blit(sully_appears_again_img, (screen.get_width() // 2 - sully_appears_again_img.get_width() // 2, screen.get_height() // 2 - sully_appears_again_img.get_height() // 2))
    display_text(screen, "sally distracts him while you run into a nearby building", white, 30, height - 40)


def run_chapter3_4(screen):
    load_images()
    meet_sally(screen)
    meet_grandma(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    eat_dinner(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    go_to_bed(screen)
    pygame.display.update()
    pygame.time.wait(5000)
    #awaken(screen)
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
    pygame.draw.rect(screen, (0, 0, 255), exit_zone)  # Draw the blue rectangle




