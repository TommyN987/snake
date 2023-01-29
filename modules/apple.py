import pygame
import random

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
        self.y = random.randint(1, 20) * SIZE