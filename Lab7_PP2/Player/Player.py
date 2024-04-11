import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

# Set up font
font = pygame.font.Font(None, 36)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load music files
music_files = [
    "music1.mp3",
    "music2.mp3",
]
current_track = 0

# Load and play the first track
pygame.mixer.music.load(music_files[current_track])
pygame.mixer.music.play()

# Flag to control playback
playing = True

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track])
                pygame.mixer.music.play()

    # Display current track info
    text = font.render(f"Playing: {os.path.basename(music_files[current_track])}", True, BLACK)
    text_rect = text.get_rect(center=(200, 150))
    screen.blit(text, text_rect)

    pygame.display.flip()

# Clean up
pygame.quit()
