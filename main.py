import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame, sys, random
from pygame.math import Vector2
pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

CELL_SIZE = 40
darker_green = (171, 208, 94)
lighter_green = (179, 214, 101)
fruit_color = (255, 0, 0)
snake_color = (153, 118, 224)

class Fruit:
    def __init__(self):
        self.x = random.randint(0,WIDTH//CELL_SIZE)
        self.y = random.randint(0,HEIGHT//CELL_SIZE)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        self.rect = pygame.Rect(self.pos.x*CELL_SIZE, self.pos.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(WIN, fruit_color, self.rect)
        pygame.display.update()


class Snake:
    def __init__(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]
        self.direction = Vector2(1,0)
        
    def draw_snake(self):
        for block in self.body:
            body_block = pygame.Rect(block.x*CELL_SIZE, block.y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(WIN, snake_color, body_block)

    def move(self):
        for i, block in enumerate(self.body):
            self.body[i] = block + self.direction
        self.draw_snake()
        
        

# Creating the background
even_iteration = True # This is a variable to apply a color in one iteration and another one in the next one, between 2 colors
for row in range(WIDTH//CELL_SIZE):
    for column in range(HEIGHT//CELL_SIZE):
        slab_pos = Vector2(row*CELL_SIZE, column*CELL_SIZE)
        slab = pygame.Rect(slab_pos.x, slab_pos.y, CELL_SIZE, CELL_SIZE)
        if even_iteration:
            pygame.draw.rect(WIN, darker_green, slab)
            even_iteration = False
        else:
            pygame.draw.rect(WIN, lighter_green, slab)
            even_iteration = True
    
    if even_iteration:
        even_iteration = False
    else:
        even_iteration = True

# Creating the fruit
fruit = Fruit()
fruit.draw_fruit()

# Creating the snake
snake = Snake()
snake.draw_snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    snake.move()
    pygame.display.update()

    clock.tick(30)