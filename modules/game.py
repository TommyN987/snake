import pygame
from pygame.locals import *
import time

from constants import Direction

from modules.apple import Apple
from modules.snake import Snake

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface, 5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
    
    def play(self):
        self.snake.walk(Direction.DOWN)
        self.apple.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.snake.move(Direction.UP)
                    if event.key == K_DOWN:
                        self.snake.move(Direction.DOWN)
                    if event.key == K_RIGHT:
                        self.snake.move(Direction.RIGHT)
                    if event.key == K_LEFT:
                        self.snake.move(Direction.LEFT)
                elif event.type == QUIT:
                    running = False
            
            self.play()

            time.sleep(.2)