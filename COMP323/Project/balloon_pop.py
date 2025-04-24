import pygame
import sys
from config import *
from spritesheet import *
import math

balloons = []
noBalloon = 10
red = (231, 76, 60)

class Balloon:
    def __init__(self, x, y, normal_sprites, pop_sprites):
        """Represents a single balloon in the game."""
        self.x = x
        self.y = y        
        self.normal_sprites = normal_sprites  # List of normal balloon frames
        self.pop_sprites = pop_sprites  # List of pop animation frames
        
        self.popped = False
        self.pop_index = 0  # Track animation frame
        self.rect = pygame.Rect(x, y, normal_sprites[0].get_width(), normal_sprites[0].get_height())

    def draw(self, screen):
        """Draws the balloon based on its state."""
        if self.popped:
            if self.pop_index < len(self.pop_sprites) - 1:
                self.pop_index += 1  # Progress through pop animation
            sprite = self.pop_sprites[self.pop_index]
        else:
            sprite = self.normal_sprites[self.pop_index % len (self.normal_sprites)]  # Default balloon frame

        screen.blit(sprite, (self.x, self.y))

    def onballoon(self, pos):
        '''
        if (x < pos[0] < x + normal_sprites[0].get_width()) and (y < pos[1] < y + normal_sprites[1].get_height()):
            return True
        else:
            return False
            '''
        return (self.rect.collidepoint(pos))
    

class BalloonGame:  
    def __init__(self):
        self.running = True
        self.won = True
        
    def runGame(player):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()  # Control game speed

        


        font = pygame.font.Font('freesansbold.ttf', 18)

        """Main game loop"""
        #load background
        background = pygame.image.load('balloonpopbg.png').convert_alpha()
        background = pygame.transform.scale(background, (1200, 750))
        

        #load sprite sheets
        balloon_spritesheet = SpriteSheet(pygame.image.load('balloonline.png').convert_alpha())
        pop_spritesheet = SpriteSheet(pygame.image.load('popAnimation.png').convert_alpha())


        #balloon sprites
        b_steps = 1  # Number of frames for the balloon animation
        p_steps = 1  # Number of frames for the pop animation


        normal_sprites = [balloon_spritesheet.get_sprite(i, 42, 52, 1.5, black) for i in range(b_steps)]
        pop_sprites = [pop_spritesheet.get_sprite(i, 42, 52, 1.5, black) for i in range(p_steps)]


        # Grid positioning
        grid_size = 4
        spacing_x = 69
        spacing_y = 70
        start_x = (width - (grid_size * spacing_x) + 10) // 2
        start_y = (height - (grid_size * spacing_y) -10) // 2

        #slider
        red_area = pygame.Rect(width/2 - 300, height - 100, 600, 50) 
        green_area = pygame.Rect(width/2 - 50, height - 100, 100, 50) 
        slider = pygame.Rect(width/2 - 10 , height - 98, 15, 46) 


        slider_speed = 8
        slider_direction = 1 
        slider_active = True  


        # Create balloons in a grid
        balloons = []


        for row in range(grid_size):
            for col in range(grid_size):
                x = start_x + col * spacing_x
                y = start_y + row * spacing_y
                balloons.append(Balloon(x, y, normal_sprites, pop_sprites))


        game_score = 0
        popped_count = 0
        max_pop = 3
        current_round = False

        # Game loop
        running = True


        screen.blit(background, (0, -75))


        while running:
            x = 575
            y = 600

            keys = pygame.key.get_pressed()

            screen.blit(background, (0, -75))  # clears previous drawings

            pygame.draw.rect(screen, red, red_area)
            pygame.draw.rect(screen, (50,205,50), green_area)
            pygame.draw.rect(screen, black, slider)



            #draw balloons
            for balloon in balloons:
                balloon.draw(screen)

            if slider_active:
                slider.x += slider_speed * slider_direction
                if slider.right >= red_area.right or slider.left <= red_area.left:
                    slider_direction *= -1
                current_round = False



            if not slider_active and not current_round:
                if slider.colliderect(green_area):
                    for balloon in balloons:
                        if not  balloon.popped and popped_count < max_pop:
                            balloon.popped = True
                            balloon.pop_index = 0 
                            game_score += 1
                            popped_count += 1
                            current_round = True
                            break 
            

            
            if keys[pygame.K_SPACE] and max_pop < 3:
                slider_active = False
        
            
            


            pygame.display.update()
            clock.tick(30)  

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and slider_active:
                        slider_active = False
                    elif event.key == pygame.K_SPACE and popped_count < 3:
                        slider_active = True
            
            if popped_count == max_pop:
                running = False
                won = True
        return won

            
                    
    
    def run(self):  
        self.runGame()
                                    




                                    

                                
                                    
                        