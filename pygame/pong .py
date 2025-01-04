import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Simple Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill the background with black
    WIN.fill(BLACK)

    # Draw game objects here

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
