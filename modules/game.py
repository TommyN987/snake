import pygame
from pygame.locals import *
import time

from constants import Direction, SIZE

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

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))
    
    def play(self):
        self.snake.walk(Direction.DOWN)
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

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