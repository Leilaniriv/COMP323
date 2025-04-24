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



class Throwable:
    """
    Spawn a throwable object
    """
    def __init__(self, x, y, angle = 75, speed=15):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('dart.png').convert_alpha()
        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = angle

        #rotated = pygame.transform.rotate(self.image, self.angle)
        #new_rect = rotated.get_rect(center=(x, y))

        
        angle_rad = math.radians(angle)

        self.vx = speed * math.cos(angle_rad)  #horizontal velocity
        self.vy = -speed * math.sin(angle_rad)  #vertical velocity (negative because it moves up)
        self.active = True

        self.gravity = 0.5  # Gravity to simulate realistic falling motion
        

    def update(self):
        """
        Move the throwable in an arc-like trajectory.
        """
        self.vy += self.gravity  #apply gravity to vertical velocity
        self.rect.x += self.vx  #move horizontally
        self.rect.y += self.vy  #move vertically

        # Remove dart if it goes off the screen
        if self.rect.y > height or self.rect.x > width or self.rect.x < 0:
            self.active = False
            screen.blit(background, (0, -75))

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated.get_rect(center=(self.x, self.y))
        screen.blit(rotated, new_rect.topleft)

 
    


class Launcher:
    def __init__(self, x, y, angle = -75):
        self.x = x
        self.y = y
        self.angle = angle
        self.original_image = pygame.image.load('dart.png').convert_alpha()  # or use a shape
        self.rect = self.original_image.get_rect(center=(x, y))

    def draw(self, screen, x = 300, y= 400):
        background = pygame.image.load('balloonpopbg.png').convert_alpha()
        background = pygame.transform.scale(background, (1200, 750))
        screen.blit(background, (0, -75))
        screen.blit(self.original_image, (x, y))
        

class BalloonGame:  
    def runGame(player):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        clock = pygame.time.Clock()  # Control game speed

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

        # Create balloons in a grid
        balloons = []
        throwables = []


        for row in range(grid_size):
            for col in range(grid_size):
                x = start_x + col * spacing_x
                y = start_y + row * spacing_y
                balloons.append(Balloon(x, y, normal_sprites, pop_sprites))


        game_score = 0
        # Game loop
        running = True


        screen.blit(background, (0, -75))


        launcher = Launcher(x, y)

        dart = Throwable(x,y)


        last_fired = 0
        firing_delay = 400

        angle = 75

        '''
        #add button for dart throw
        font = pygame.font.Font('freesansbold.ttf', 25)
        throw = font.render('Throw', True, black)
        throw_button = pygame.Rect(width/4 - 135, height/2 - 30, 150, 90)
        pygame.draw.rect(screen, white, throw_button)
        screen.blit(throw, (width/4 - 100, height/2))
        '''

        while running:
            x = 575
            y = 600

            screen.blit(background, (0, -75))  # clears previous drawings


            launcher.draw(screen,x,y)

            #draw balloons
            for balloon in balloons:
                balloon.draw(screen)

            

            for throwable in throwables[:]:
                throwable.update()
                if throwable.active == True: 
                    screen.blit(throwable.image, throwable.rect)
                if throwable.active == False:
                    throwables.remove(throwable)

                for balloon in balloons:
                    if balloon.rect.colliderect(throwable.rect) and not balloon.popped:
                        balloon.popped = True
                        balloon.pop_index = 0 
                        game_score += 1
                        throwables.remove(throwable)  # Remove the throwable after hitting a balloon
                        break 

                
                #pygame.display.update()
            


            pygame.display.update()
            clock.tick(30)  

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    

            
                moving = False
                #dart_width = width // 2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dart.angle = min(dart.angle + 5, 120)
                    
                    if event.key == pygame.K_RIGHT:
                        dart.angle = min(dart.angle - 5, 30)
            

                    if event.key == pygame.K_SPACE:
                        current_time = pygame.time.get_ticks()
                        if current_time - last_fired > firing_delay:
                            throwables.append(Throwable(x,y, angle, speed= 30))
                            last_fired = current_time
                        
                            if game_score == 3:
                                break
                        pygame.display.update()
                    
    
    def run(self):
        self.runGame()
                                    




                                    

                                
                                    
                        