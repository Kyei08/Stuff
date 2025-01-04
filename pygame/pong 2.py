import pygame

# ... (rest of the code from above)

# Create a ball object
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_radius = 10
ball_speed = 5
ball_dx, ball_dy = ball_speed, ball_speed

# Game loop
run = True
while run:
    # ... (rest of the code from above)

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with the screen edges
    if ball_x + ball_radius >= WIDTH or ball_x - ball_radius <= 0:
        ball_dx *= -1
    if ball_y + ball_radius >= HEIGHT or ball_y - ball_radius <= 0:
        ball_dy *= -1

    # Draw the ball
    pygame.draw.circle(WIN, WHITE, (ball_x, ball_y), ball_radius)

    # ... (rest of the code from above)