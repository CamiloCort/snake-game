import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame


WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

pygame.time.delay(4000)