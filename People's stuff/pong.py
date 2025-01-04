import pygame


class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 7

    def draw(self):
        pygame.draw.rect(WIN, WHITE, (self.x, self.y, self.width, self.height))


    import pygame

    # Assuming these variables are defined elsewhere in the code
    # WIDTH = 800
    # HEIGHT = 600
    # BLACK = (0, 0, 0)
    # WHITE = (255, 255, 255)
    # FONT = pygame.font.Font('freesansbold.ttf', 32)
    # WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    class Ball:
        def __init__(self, x, y, radius, speed):
            self.x = x
            self.y = y
            self.radius = radius
            self.speed = speed
            self.x_vel = self.speed
            self.y_vel = self.speed

        def draw(self):
            pygame.draw.circle(WIN, WHITE, (self.x, self.y), self.radius)

# Create paddles and ball
paddle_a = Paddle(10, HEIGHT // 2 - 75, 10, 150)
paddle_b = Paddle(WIDTH - 20, HEIGHT // 2 - 75, 10, 150)
ball = Ball(WIDTH // 2, HEIGHT // 2, 10, 5)
def draw(score_a, score_b):
    WIN.fill(BLACK)
    paddle_a.draw()
    paddle_b.draw()
    ball.draw()

    score_text_a = FONT.render(str(score_a), True, WHITE)
    score_text_b = FONT.render(str(score_b), True, WHITE)

    WIN.blit(score_text_a, (WIDTH // 4 - 20, 20))
    WIN.blit(score_text_b, (3 * WIDTH // 4 - 20, 20))

    pygame.display.update()

def handle_collision():
    if ball.y + ball.radius >= HEIGHT or ball.y - ball.radius <= 0:
        ball.y_vel *= -1
    if ball.x - ball.radius <= paddle_a.x + paddle_a.width and paddle_a.y <= ball.y <= paddle_a.y + paddle_a.height:
        ball.x_vel *= -1
    if ball.x + ball.radius >= paddle_b.x and paddle_b.y <= ball.y <= paddle_b.y + paddle_b.height:
        ball.x_vel *= -1

def main():
    run = True
    clock = pygame.time.Clock()
    score_a = 0
    score_b = 0

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()   

        paddle_a.y += paddle_a.speed * (keys[pygame.K_w] - keys[pygame.K_s])
        paddle_b.y += paddle_b.speed * (keys[pygame.K_UP] - keys[pygame.K_DOWN])

        ball.move()
        handle_collision()

        if ball.x - ball.radius <= 0:
            score_b += 1
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball.x_vel *= -1
        if ball.x + ball.radius >= WIDTH:
            score_a += 1
            ball.x = WIDTH // 2
            ball.y = HEIGHT // 2
            ball.x_vel *= -1

        draw(score_a, score_b)

    pygame.quit()

if __name__ == "__main__":
    main()