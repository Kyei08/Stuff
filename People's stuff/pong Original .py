keys = pygame.key.get_pressed()
if keys[pygame.K_w]:
    left_paddle.y -= paddle_speed
if keys[pygame.K_s]:
    left_paddle.y += paddle_speed
if keys[pygame.K_UP]:
    right_paddle.y -= paddle_speed
if keys[pygame.K_DOWN]:
    right_paddle.y += paddle_speed   


# Move the ball
ball.x += ball_speed   

if ball.y <= 0 or ball.y >= height - ball_radius * 2:
    ball_speed = -ball_speed

# Check for paddle collisions
if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
    ball_speed = -ball_speed

# Check for scoring
if ball.x <= 0:
    # Right player scores
    pass
if ball.x >= width - ball_radius * 2:
    # Left player scores
    pass

# Draw the game objects
screen.fill(black)
pygame.draw.rect(screen, white, left_paddle)
pygame.draw.rect(screen, white, right_paddle)
pygame.draw.circle(screen, white, (ball.x + ball_radius, ball.y + ball_radius), ball_radius)

pygame.display.update()
