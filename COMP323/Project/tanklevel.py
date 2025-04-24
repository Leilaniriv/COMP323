import pygame
from config import width, height, black, white
from spritesheet import SpriteSheet
from laserhallway import LaserHallway
from keypad import KeypadGame



class LevelTank:
    def __init__(self, player):
        pygame.mixer.init()
        self.player = player
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        
        self.sounds = {
            'tank':pygame.mixer.Sound('tanklevel.wav'),
            'broken':pygame.mixer.Sound('broken.wav')
            
        }
        self.sounds['tank'].set_volume(0.3)
        self.sounds['tank'].play(loops=-1)

        # Load backgrounds
        self.intact_bg = pygame.image.load("lab_background.png").convert_alpha()
        self.broken_bg = pygame.image.load("broken_tank.png").convert_alpha()
        self.intact_bg = pygame.transform.scale(self.intact_bg, (width, height))
        self.broken_bg = pygame.transform.scale(self.broken_bg, (width, height))


        sprite = pygame.image.load('aliens.png').convert_alpha()
        sprite_sheet = SpriteSheet(sprite)

        # Animation setup
        self.an_list = []
        an_steps = [10, 10]
        step_counter = 0
        for animation in an_steps:
            temp_list = []
            for _ in range(animation):
                temp_list.append(sprite_sheet.get_sprite(step_counter, 32, 45, 3, black))
                step_counter += 1
            self.an_list.append(temp_list)

        self.action = 0
        self.frame = 0
        self.frame_delay = 20
        self.frame_counter = 0

        # Tank escape control
        self.hold_start = None
        self.hold_required = 3000
        self.is_broken = False
        self.done = False
        self.puzzle_solved = False

        # Object positions
        self.door_rect = pygame.Rect(800, 150, 150, 160)
        self.keypad_rect = pygame.Rect(1030, 190, 50, 50)


        # Player spawn point
        self.player.rect.centerx = width // 2
        self.player.rect.bottom = height - 100

    def update(self):
        keys = pygame.key.get_pressed()
        moving = False

        # Movement after tank breaks
        if self.is_broken:
            self.screen.blit(self.broken_bg, (0, 0))
            pygame.draw.rect(self.screen, (255, 0, 0), self.door_rect, 3)

            # Movement controls
            if keys[pygame.K_a] and self.player.rect.left > 0:
                self.player.rect.x -= 2
                self.action = 1
                moving = True
            elif keys[pygame.K_d] and self.player.rect.right < width:
                self.player.rect.x += 2
                self.action = 0
                moving = True

            if keys[pygame.K_w] and self.player.rect.top > 0:
                self.player.rect.y -= 2
                moving = True
            elif keys[pygame.K_s] and self.player.rect.bottom < height:
                self.player.rect.y += 2
                moving = True

            # Animate player
            if moving:
                self.frame_counter += 1
                if self.frame_counter >= self.frame_delay:
                    self.frame = (self.frame + 1) % len(self.an_list[self.action])
                    self.frame_counter = 0
            else:
                self.frame = 0

            # Draw alien
            self.screen.blit(self.an_list[self.action][self.frame], self.player.rect)

            # Keypad interaction
# Keypad interaction
            if self.player.rect.colliderect(self.keypad_rect):
                font = pygame.font.Font("ByteBounce.ttf", 32)
                self.screen.blit(font.render("Press E to use keypad", True, white), (self.player.rect.x - 30, self.player.rect.y - 20))
                if keys[pygame.K_e] and not self.puzzle_solved:
                    from keypad import KeypadGame
                    keypad = KeypadGame(self.screen)
                    self.puzzle_solved = keypad.run()


            # Door interaction
            if self.player.rect.colliderect(self.door_rect):
                font = pygame.font.Font("ByteBounce.ttf", 32)
                if self.puzzle_solved:
                    self.done = True
                else:
                # Draw glowing border around keypad
                    pygame.draw.rect(self.screen, (255, 255, 0), self.keypad_rect, 4)  # yellow border

                    # Prompt
                    msg = "Solve the keypad puzzle to escape!"
                    text = font.render(msg, True, white)
                    self.screen.blit(text, (self.player.rect.x - 40, self.player.rect.y - 20))


        # Initial phase: tank intact
        else:
            self.screen.blit(self.intact_bg, (0, 0))

            # Animate idle alien
            if keys[pygame.K_a]:
                self.action = 1
            elif keys[pygame.K_d]:
                self.action = 0
            else:
                self.frame = 0

            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.frame = (self.frame + 1) % len(self.an_list[self.action])
                self.frame_counter = 0

            self.screen.blit(self.an_list[self.action][self.frame], self.player.rect)

            # Prompt
            font = pygame.font.Font("ByteBounce.ttf", 32)
            prompt = font.render("Hold SPACE to break the glass...", True, white)
            self.screen.blit(prompt, (width // 2 - 150, height - 40))

            # Break tank
            if keys[pygame.K_SPACE]:
                if self.hold_start is None:
                    self.hold_start = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - self.hold_start >= self.hold_required:
                    self.is_broken = True
                    self.sounds['broken'].play()
            else:
                self.hold_start = None


        pygame.display.update()
        self.clock.tick(60)

    def run(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.update()
        pygame.mixer.stop()
        if self.done:
            hallway = LaserHallway(self.player)
            next_scene = hallway.run()

            if next_scene == "desert":
                from desert import Desert
                desert_scene = Desert(self.player)
                desert_scene.run()

    #def reset(self):
     #   self.hold_start = None
      #  self.done = False
       # self.is_broken = False
        #self.puzzle_solved = False
        #self.player.rect.centerx = width // 2
        #self.player.rect.bottom = height - 100

