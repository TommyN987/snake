import pygame
from pygame.locals import *
import time

from constants import Direction, SIZE, BACKGROUND_COLOR, FONT

from modules.apple import Apple
from modules.snake import Snake

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        font = FONT
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = FONT
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

    def play_sound(self, sound_name):
        if sound_name == "crash":
            sound = pygame.mixer.Sound("assets/crash_sound.mp3")
        elif sound_name == "ding":
            sound = pygame.mixer.Sound("assets/ding_sound.mp3")

        pygame.mixer.Sound.play(sound)
    
    def play(self):
        self.snake.walk(Direction.DOWN)
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Snake eats apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()
        
        # Snake collides with itself
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "Collision occured"
        
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            self.play_sound("crash")
            raise "Hit the boundary error"

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move(Direction.UP)
                        if event.key == K_DOWN:
                            self.snake.move(Direction.DOWN)
                        if event.key == K_RIGHT:
                            self.snake.move(Direction.RIGHT)
                        if event.key == K_LEFT:
                            self.snake.move(Direction.LEFT)
                        if event.key == K_p:
                            pause = True
                elif event.type == QUIT:
                    running = False
            
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.25)