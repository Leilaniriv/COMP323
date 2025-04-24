#chapter 5
import pygame
import sys
from config import width, height

pygame.init()
screen = pygame.display.set_mode((width, height))  # Initialize the display

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

alien_image = pygame.image.load('alien.jpeg').convert_alpha()
alien_image = pygame.transform.scale(alien_image, (200, 200))  # Scale the alien image to 200x200 pixels
player = Player(alien_image, 100, 100)
priest_image = pygame.image.load('priest.jpeg').convert_alpha()
priest_image = pygame.transform.scale(priest_image, (200, 200))  # Scale the priest image to 200x200 pixels
priest = NPC(priest_image, 500, 300)  # Position priest at (300, 300)

def display_options(screen, option1, option2):
    font = pygame.font.Font(None, 36)
    color1 = (255,255,255) 
    color2 = (255,255,255)
    text1 = font.render(option1, True, color1)
    text2 = font.render(option2, True, color2)
    screen.blit(text1, (30, screen.get_height() - 80))
    screen.blit(text2, (30, screen.get_height() - 40))

def choose_option():
    option = 0
    if pygame.key.get_pressed()[pygame.K_1]:
        option = 1
    elif pygame.key.get_pressed()[pygame.K_2]:
        option = 2
    return option

def load_images():
    global background_img, alien_img
    background_img = pygame.image.load('church_background.jpeg').convert_alpha()
    # Scale the background to fit the screen dimensions
    background_img = pygame.transform.scale(background_img, (width, height))
    alien_img = pygame.image.load('cute_alien.png').convert_alpha()

def display_text(screen, text, color, x, y):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def display_priest():
    screen.blit(background_img, (0, 0))  # Draw the background
    screen.blit(priest.image, priest.rect)  # Draw the priest(player)
    player.update()
    screen.blit(player.image, player.rect)

def display_church():
    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, 0))  # Draw the scaled background
    display_text(screen, "You enter a building with a cross in its center...", (255, 255, 255), 30, screen.get_height() - 40)
   

def run_chapter5(screen):
    load_images()
    running = True
    clock = pygame.time.Clock()
    show_priest = False  # State to control when to display the priest
    priest_timer = 0  # Timer to delay showing the priest
    text_timer = 0  # Timer to control text display
    text_state = 0  # State to track which text to display
    selected_option = 0  # Track the selected option (1 or 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Escape key pressed. Exiting game...")
                    pygame.quit()
                    sys.exit()

        # Render the church scene
        display_church()

        # Update and render the player
        player.update()
        screen.blit(player.image, player.rect)

        # Handle priest display logic
        if not show_priest:
            priest_timer += clock.get_time()  # Increment timer
            if priest_timer > 5000:  # After 5 seconds, show the priest
                show_priest = True

        if show_priest:
            display_priest()

            # Increment text timer
            text_timer += clock.get_time()

            # Display text based on the current state
            if text_state == 0:
                display_text(screen, "You see a man with the same cross on his chest beckon you over to him", (255, 255, 255), 30, screen.get_height() - 40)
                if text_timer > 7000:  # After 5 seconds, move to the next text
                    text_state = 1
                    text_timer = 0  # Reset the timer
            elif text_state == 1:
                display_text(screen, "He says to you, 'Welcome to Nova's church, I am priest Solomon. I can sense your inner turmoil'", (255, 255, 255), 30, screen.get_height() - 40)
                if text_timer > 7000:
                    text_state = 2
                    text_timer = 0
            elif text_state == 2:
                display_text(screen, "You ask him who he is. He explains that he is what humans call a priest, a spiritual guide.", (255, 255, 255), 30, screen.get_height() - 60)
                if text_timer > 7000:
                    text_state = 3
                    text_timer = 0
            elif text_state == 3:
                # Display options only when in state 3
                display_options(screen, "Press 1: Ask for help", "Press 2: Brush him off")
                selected_option = choose_option()
                if selected_option != 0:
                    text_state = 4
                    text_timer = 0
            elif text_state == 4:
                # Render the result of the selected option
                if selected_option == 1:
                    display_text(screen, "You ask him for help. You thought you'd hate humans, but you feel conflicted.", (255, 255, 255), 30, screen.get_height() - 40)
                    if text_timer > 7000:
                        text_state = 5
                        text_timer = 0
                        selected_option = 0 #reset 
                elif selected_option == 2:
                    display_text(screen, "You brush him off, why would you trust a human? Yet his disappointment in you hurts.", (255, 255, 255), 30, screen.get_height() - 40)
                    if text_timer > 7000:
                        text_state = 5
                        text_timer = 0
                        selected_option = 0 #reset
            elif text_state == 5:
                display_text(screen, "The priests says,'Is it better to resist change for temporary comfort...", (255, 255, 255), 30, screen.get_height() - 40)
                if text_timer > 7000:
                    text_state = 6
                    text_timer = 0
            elif text_state == 6:
                display_text(screen, "or endure uncertainty for a chance at peace? Aren't you tired of violence my friend?'", (255, 255, 255), 30, screen.get_height() - 40)
                if text_timer > 7000:
                    text_state = 7
                    text_timer = 0
            elif text_state == 7:
                display_text(screen, "His words resonate with you, is he really your friend?", (255, 255, 255), 30, screen.get_height() - 40)
                if text_timer > 7000:
                    text_state = 8
                    text_timer = 0
            elif text_state == 8:
                display_options(screen, "Press 1: Thank you for his advice", "Press 2: Say he's foolish")
                selected_option = choose_option()
                if selected_option != 0:
                    text_state = 9
                    text_timer = 0
            elif text_state == 9:
                if selected_option == 1:
                    display_text(screen, "You thank him for his advice.He says,'Continue on the path you're on now and you won't feel regret.'", (255, 255, 255), 30, screen.get_height() - 40)
                    if text_timer > 7000:
                        text_state = 10
                        text_timer = 0
                        selected_option = 0 #reset
                elif selected_option == 2:
                    display_text(screen, "You say he's foolish.He says,'Tread lightly on the path you're taking, it will lead to nothing but regret.'", (255, 255, 255), 30, screen.get_height() - 40)
                    if text_timer > 7000: 
                        text_state = 10
                        text_timer = 0
                        selected_option = 0 #reset
            elif text_state == 10:
                display_text(screen, "The priests pulls a metal object from his pocket and hands it to you...", (255, 255, 255), 30, screen.get_height() - 40)
                if text_timer > 7000:
                    text_state = 11
                    text_timer = 0
            elif text_state == 11:
                display_text(screen, "He says,'something tells me this belongs to you. I hope you won't regret your decisions.'", (255, 255, 255), 30, screen.get_height() - 40)  # Fixed typo
                if text_timer > 7000: 
                    text_state = 12
                    text_timer = 0
            elif text_state == 12: 
                display_text(screen, "You've collected another piece of your ship. It's time to keep going.", (255, 255, 255), 30, screen.get_height() - 40)
                if text_timer > 7000:
                    text_state = 13
                    text_timer = 0
            elif text_state == 13:
                #go to chapter 6 put for now end loop
                pygame.quit()
                sys.exit()

        # Update the display
        pygame.display.flip()
        clock.tick(120)
             

run_chapter5(screen)