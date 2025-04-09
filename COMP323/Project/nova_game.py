
"""
GAME NAME: NOVA

Our choice based decision game. Play as an alien that crashlands onto 
Earth and take a good or bad path.

Main Game Loop:
-Game states: intro screen, prolouge, chapters, epilouge, game over
-Game objects: player, NPCS, projectiles
-User interface: prompts, dialogue 
-Asset management: sprites, sounds, background layers

Features: 
-Arrow keys: move left, right, up, down
-Points: good and bad points tracked based on choices



Game structure: 
-Player class: 
-Background class: 
-NPC class: 
-Projectile class: 
-Level Manager:
"""


import pygame, sys, os

def gameExit():
    pygame.quit()
    sys.exit()

def gameLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit()
