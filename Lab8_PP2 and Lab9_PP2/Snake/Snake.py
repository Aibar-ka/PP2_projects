import pygame
import sys
import copy
import random
import time

pygame.init()

scale = 10
score = 0
level = 0
SPEED = 10

food_x = 10
food_y = 10

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

background = (0, 0, 0)
snake_colour = (255, 137, 0)
food_colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
snake_head = (255, 247, 0)
font_colour = (255, 255, 255)
defeat_colour = (255, 0, 0)


class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def reset(self):
        self.x = 500 / 2 - scale
        self.y = 500 / 2 - scale
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def show(self):
        for i in range(self.length):
            if not i == 0:
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self):
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True

    def level(self):
        global level
        if self.length % 5 == 0:
            return True

    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(
                    self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    def update(self):
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i - 1])
            i -= 1
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale


class Food:
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, 500 / scale - 1) * scale
        food_y = random.randrange(1, 500 / scale - 1) * scale

    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))


def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, font_colour)
    display.blit(text, (scale, scale))


def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (90 - scale, scale))


def gameLoop():
    global score
    global level
    global SPEED

    snake = Snake(500 / 2, 500 / 2)
    food = Food()
    food.new_location()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if snake.y_dir == 0:
                    if event.key == pygame.K_w:
                        snake.x_dir = 0
                        snake.y_dir = -1
                    if event.key == pygame.K_s:
                        snake.x_dir = 0
                        snake.y_dir = 1

                if snake.x_dir == 0:
                    if event.key == pygame.K_a:
                        snake.x_dir = -1
                        snake.y_dir = 0
                    if event.key == pygame.K_d:
                        snake.x_dir = 1
                        snake.y_dir = 0

        display.fill(background)

        snake.show()
        snake.update()
        food.show()
        show_score()
        show_level()

        if snake.check_eaten():
            food.new_location()
            score += random.randint(1, 5)
            snake.grow()

        if snake.level():
            food.new_location()
            level += 1
            SPEED += 3
            snake.grow()

        if snake.death():
            score = 0
            level = 0
            font = pygame.font.SysFont(None, 100)
            text = font.render("Game Over!", True, defeat_colour)
            display.blit(text, (50, 200))
            pygame.display.update()
            time.sleep(3)
            snake.reset()

        if snake.history[0][0] > 500:
            snake.history[0][0] = 0
        if snake.history[0][0] < 0:
            snake.history[0][0] = 500

        if snake.history[0][1] > 500:
            snake.history[0][1] = 0
        if snake.history[0][1] < 0:
            snake.history[0][1] = 500

        pygame.display.update()
        clock.tick(SPEED)


gameLoop()