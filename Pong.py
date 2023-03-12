import pygame
import random

# Initialize Pygame
pygame.init()

# Create the game window
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the paddles and the ball
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_WIDTH = 10
BALL_HEIGHT = 10

# Set up the player paddle
player_paddle = pygame.Rect(0, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up the AI paddle
ai_paddle = pygame.Rect(WIDTH - PADDLE_WIDTH, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up the ball
ball = pygame.Rect(WIDTH/2 - BALL_WIDTH/2, HEIGHT/2 - BALL_HEIGHT/2, BALL_WIDTH, BALL_HEIGHT)

# Set up the ball's initial velocity
ball_velocity_x = 5 * random.choice([-1, 1])
ball_velocity_y = 5 * random.choice([-1, 1])

# Set up the game clock
clock = pygame.time.Clock()

# Set up the scoreboard
player_score = 0
ai_score = 0
font = pygame.font.Font(None, 50)

# Set up the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.y -= 5
    if keys[pygame.K_DOWN]:
        player_paddle.y += 5

    # Move the AI paddle
    if ball.y < ai_paddle.y + PADDLE_HEIGHT/2:
        ai_paddle.y -= 4.75
    if ball.y > ai_paddle.y + PADDLE_HEIGHT/2:
        ai_paddle.y += 4.75

    # Move the ball
    ball.x += ball_velocity_x
    ball.y += ball_velocity_y

    # Check for collision with the player paddle
    if ball.colliderect(player_paddle):
        ball_velocity_x = abs(ball_velocity_x)
    # Check for collision with the AI paddle
    if ball.colliderect(ai_paddle):
        ball_velocity_x = -abs(ball_velocity_x)
    # Check for collision with the top or bottom wall
    if ball.y <= 0 or ball.y >= HEIGHT - BALL_HEIGHT:
        ball_velocity_y = -ball_velocity_y
    # Check for collision with the left or right wall
    if ball.x <= 0:
        ai_score += 1
        ball_velocity_x = 5
        ball_velocity_y = 5 * random.choice([-1, 1])
        ball.x = WIDTH/2 - BALL_WIDTH/2
        ball.y = HEIGHT/2 - BALL_HEIGHT/2
    if ball.x >= WIDTH - BALL_WIDTH:
        player_score += 1
        ball_velocity_x = -5
        ball_velocity_y = 5 * random.choice([-1, 1])
        ball.x = WIDTH/2 - BALL_WIDTH/2
        ball.y = HEIGHT/2 - BALL_HEIGHT/2

    # Draw the paddles and the ball
    WINDOW.fill(BLACK)
    pygame.draw.rect(WINDOW, WHITE, player_paddle)
    pygame.draw.rect(WINDOW, WHITE, ai_paddle)
    pygame.draw.ellipse(WINDOW, WHITE, ball)
    
    # Draw the scoreboard
    player_text = font.render(str(player_score), True, WHITE)
    ai_text = font.render(str(ai_score), True, WHITE)
    player_rect = player_text.get_rect(center=(WIDTH/4, 50))
    ai_rect = ai_text.get_rect(center=(WIDTH*3/4, 50))
    WINDOW.blit(player_text, player_rect)
    WINDOW.blit(ai_text, ai_rect)

    # Update the game window
    pygame.display.update()

    # Set the game clock
    clock.tick(60)

