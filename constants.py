import pygame
from enum import Enum

pygame.init()

SIZE = 40
BACKGROUND_COLOR = (110, 110, 50)
FONT = pygame.font.SysFont('arial', 30)

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4