import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 10

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Pong Game")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Paddle positions
player_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ai_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_speed = 5

# Ball settings
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([-4, 4])
ball_dy = random.choice([-4, 4])

# Score
player_score = 0
ai_score = 0
font = pygame.font.SysFont(None, 36)

def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (20, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - 30, ai_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    score_text = font.render(f"Player: {player_score}  AI: {ai_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    pygame.display.flip()

def ai_move():
    global ai_y
    if ai_y + PADDLE_HEIGHT / 2 < ball_y:
        ai_y += paddle_speed
    elif ai_y + PADDLE_HEIGHT / 2 > ball_y:
        ai_y -= paddle_speed
    ai_y = max(0, min(HEIGHT - PADDLE_HEIGHT, ai_y))

# Game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_y > 0:
        player_y -= paddle_speed
    if keys[pygame.K_s] and player_y < HEIGHT - PADDLE_HEIGHT:
        player_y += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Collision with top/bottom
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        ball_dy *= -1

    # Collision with paddles
    if (20 < ball_x - BALL_RADIUS < 30 and player_y < ball_y < player_y + PADDLE_HEIGHT) or \
       (WIDTH - 30 < ball_x + BALL_RADIUS < WIDTH - 20 and ai_y < ball_y < ai_y + PADDLE_HEIGHT):
        ball_dx *= -1

    # Score update
    if ball_x < 0:
        ai_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = random.choice([-4, 4])
        ball_dy = random.choice([-4, 4])
    elif ball_x > WIDTH:
        player_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx = random.choice([-4, 4])
        ball_dy = random.choice([-4, 4])

    ai_move()
    draw()

pygame.quit()
