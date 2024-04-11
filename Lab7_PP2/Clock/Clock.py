import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 700, 700
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Clock")

# Load images for clock face and hands
clock_face = pygame.image.load("clock_face.png")
minute_hand_img = pygame.image.load("minute_hand.png")
second_hand_img = pygame.image.load("second_hand.png")
clock_face_center = (clock_face.get_width() // 2, clock_face.get_height() // 2)
# Define colors
WHITE = (255, 255, 255)

def draw_clock():
    screen.fill(WHITE)
    screen.blit(clock_face, (0, 0))

def rotate_hand(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rect

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get current time
        current_time = time.localtime()
        seconds = current_time.tm_sec
        minutes = current_time.tm_min

        # Calculate rotation angles for hands
        second_angle = -seconds * 6  # Each second is 6 degrees
        minute_angle = -(minutes * 6 + seconds / 10)  # Each minute is 6 degrees, plus fine-tune for seconds

        # Draw clock face
        draw_clock()

        # Rotate and draw minute hand
        minute_hand, minute_rect = rotate_hand(minute_hand_img, minute_angle, clock_face_center)
        screen.blit(minute_hand, minute_rect)

        # Rotate and draw second hand
        second_hand, second_rect = rotate_hand(second_hand_img, second_angle, clock_face_center)
        screen.blit(second_hand, second_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()