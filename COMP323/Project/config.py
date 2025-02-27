import pygame




black = (0,0,0)
white = (255,255,255)
light = (192,192,192)

# TITLE OF CANVAS 
pygame.display.set_caption("Nova")

width = 1200 
    
height = 750

TILESIZE = 32
#15 blocks high, 20 blocks wide represented by B. P represents player
# the dots represent empty space, the scattered B's represent obstacles
tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B.................B',
    'B...BB............B',
    'B.................B',
    'B.................B',
    'B.................B',
    'B.................B',
    'B........P........B',
    'B.................B',
    'B.................B',
    'B.................B',
    'B.................B',
    'B............B....B',
    'B.................B',
    'B.................B',
    'BBBBBBBBBBBBBBBBBBBB'
]