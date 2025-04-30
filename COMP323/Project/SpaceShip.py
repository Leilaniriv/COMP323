import pygame
import sys
from nova_game import *

class SpaceshipPart(pygame.sprite.Sprite):
    def __init__(self, x, y, part_type):
        super().__init__()
        self.part_type = part_type
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0)]
        pygame.draw.polygon(self.image, (255, 0, 0), [[300, 300], [100, 400],[100, 300]])
        pygame.draw.circle(self.image, (255,255,255), (20,20), 15, 2)  # White outline
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.collected = False