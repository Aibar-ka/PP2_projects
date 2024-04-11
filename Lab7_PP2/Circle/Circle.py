import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 50
BALL_RADIUS = BALL_SIZE // 2
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
MOVE_DISTANCE = 20

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Initial ball position
ball_x = (WIDTH - BALL_SIZE) // 2
ball_y = (HEIGHT - BALL_SIZE) // 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - MOVE_DISTANCE, 0)
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + MOVE_DISTANCE, HEIGHT - BALL_SIZE)
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - MOVE_DISTANCE, 0)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + MOVE_DISTANCE, WIDTH - BALL_SIZE)

    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (ball_x + BALL_RADIUS, ball_y + BALL_RADIUS), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
