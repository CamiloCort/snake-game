import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame, sys
from pygame.math import Vector2
pygame.init()


WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

CELL_SIZE = 40
slab_color_1 = (100, 201, 125)
slab_color_2 = (125, 201, 100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    even_iteration = True # This is a variable to apply a color in one iteration and another one in the next one, between 2 colors
    for row in range(20):
        for column in range(20):
            slab_pos = Vector2(row*CELL_SIZE, column*CELL_SIZE)
            slab = pygame.Rect(slab_pos.x, slab_pos.y, CELL_SIZE, CELL_SIZE)
            if even_iteration:
                pygame.draw.rect(WIN, slab_color_1, slab)
                even_iteration = False
            else:
                pygame.draw.rect(WIN, slab_color_2, slab)
                even_iteration = True
        
    pygame.display.update()
    
    clock.tick(60)
