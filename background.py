import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LPINK = (255, 224, 229)  # Light Pink

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Survive Comp Dance")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 224, 229))  # Fill with black

    # Update the display
    pygame.display.flip()
    pygame.time.delay(50)  # Delay to control rectangle speed

# Quit Pygame
pygame.quit()
sys.exit()
