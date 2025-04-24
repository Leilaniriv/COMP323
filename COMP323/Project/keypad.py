import pygame
from config import width, height

class KeypadGame:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.sequence = ['5', '3', '8', '6']
        self.images = [
            pygame.image.load("keypad.png").convert_alpha(), # blank
            pygame.image.load("keypad1.png").convert_alpha(),  # 5
            pygame.image.load("keypad2.png").convert_alpha(),  # 3
            pygame.image.load("keypad3.png").convert_alpha(),  # 8
            pygame.image.load("keypad4.png").convert_alpha(),  # 6
        ]
        self.images = [pygame.transform.scale(img, (400, 400)) for img in self.images]

        self.sounds = {
        'keypad':pygame.mixer.Sound('keypad.wav'),
        'beep':pygame.mixer.Sound('beep.mp3')
        }
        self.sounds['keypad'].set_volume(0.3)
        self.sounds['keypad'].play(loops=-1)
        self.sounds['beep'].play(loops=3)

    def flash_sequence(self):
        for img in self.images:
            font = pygame.font.Font('ByteBounce.ttf', 32)
            memorize = font.render("Memorize the digits!", True, (255, 255, 255))
            self.screen.blit(img, (width // 2 - 200, height // 2 - 200))
            self.screen.blit(memorize, (width // 2 - memorize.get_width() // 2, height // 2 - 250))  # above the keypad
            pygame.display.update()
            pygame.time.delay(500)  # show image
            self.screen.fill((0, 0, 0))
            pygame.display.update()

    def get_input(self):
        font = pygame.font.Font(None, 48)
        input_str = ""

        while True:
            self.screen.fill((0, 0, 0))
            prompt = font.render("Enter the 4-digit code:", True, (255, 255, 255))
            entry = font.render(input_str, True, (0, 255, 0))
            self.screen.blit(prompt, (width // 2 - 200, height // 2 - 100))
            self.screen.blit(entry, (width // 2 - 40, height // 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(input_str) == 4:
                        return input_str
                    elif event.key == pygame.K_BACKSPACE:
                        input_str = input_str[:-1]
                    elif event.unicode.isdigit() and len(input_str) < 4:
                        input_str += event.unicode

            self.clock.tick(60)

    def run(self):
        solved = False
        while not solved:
            self.flash_sequence()
            attempt = self.get_input()
            if list(attempt) == self.sequence:
                return True
            else:
                # show fail screen
                font = pygame.font.Font(None, 48)
                self.screen.fill((0, 0, 0))
                text = font.render("Incorrect. Try again.", True, (255, 0, 0))
                self.screen.blit(text, (width // 2 - 150, height // 2))
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.mixer.stop()
