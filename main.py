import pygame
from pygame.locals import *
from enum import Enum
import time
import random

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load('assets/apple.jpg').convert()
        self.x = 120
        self.y = 120
    
    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()
    
    def move(self):
        self.x = random.randint(1, 25) * SIZE
        self.y = random.randint(1, 25) * SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.image = pygame.image.load('assets/block.jpg').convert()
        self.direction = Direction.DOWN

        self.length = length
        self.x = [40]*length
        self.y = [40]*length

    def move(self, direction: Direction):
        self.direction = direction

    def walk(self, direction: Direction):
        # update body
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update head
        if self.direction == Direction.UP:
            self.y[0] -= SIZE
        if self.direction == Direction.DOWN:
            self.y[0] += SIZE
        if self.direction == Direction.RIGHT:
            self.x[0] += SIZE
        if self.direction == Direction.LEFT:
            self.x[0] -= SIZE
        
        self.draw()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((110, 110, 50))

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        
        pygame.display.flip()

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

if __name__ == '__main__':
    game = Game()
    game.run()