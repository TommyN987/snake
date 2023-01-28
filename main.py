import pygame
from pygame.locals import *
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Snake:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load('assets/block.jpg').convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((110, 110, 50))

        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move(self, direction: Direction):
        if direction == Direction.UP:
            self.y -= 10
        elif direction == Direction.DOWN:
            self.y += 10
        elif direction == Direction.RIGHT:
            self.x += 10
        elif direction == Direction.LEFT:
            self.x -= 10
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface)
        self.snake.draw()

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

if __name__ == '__main__':
    game = Game()
    game.run()