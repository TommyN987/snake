import pygame

from constants import SIZE, Direction

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