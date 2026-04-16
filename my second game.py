# Endless Runner Game in Python using Pygame
# Simple, beginner-friendly endless runner similar in concept to Mario/Subway Surfers
# You can expand this with new features later.

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner")

# Clock
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Player settings
player_size = 50
player_x = 100
player_y = HEIGHT - player_size - 20
player_velocity_y = 0
jump_strength = -15
gravity = 0.8
is_jumping = False

# Obstacle settings
obstacle_width = 30
obstacle_height = 60
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 20
obstacle_speed = 6

# Score
score = 0
font = pygame.font.SysFont(None, 36)


def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_size, player_size))


def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))


def show_score():
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))


def game_over_screen():
    text = font.render("Game Over! Press R to Restart", True, BLACK)
    screen.blit(text, (WIDTH // 2 - 180, HEIGHT // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False


running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                player_velocity_y = jump_strength
                is_jumping = True

    # Player movement
    player_velocity_y += gravity
    player_y += player_velocity_y

    if player_y >= HEIGHT - player_size - 20:
        player_y = HEIGHT - player_size - 20
        is_jumping = False

    # Obstacle movement
    obstacle_x -= obstacle_speed

    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH + random.randint(0, 300)
        score += 1

        # Increase difficulty
        if score % 5 == 0:
            obstacle_speed += 0.5

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if player_rect.colliderect(obstacle_rect):
        game_over_screen()

        # Reset game
        player_y = HEIGHT - player_size - 20
        obstacle_x = WIDTH
        obstacle_speed = 6
        score = 0

    # Draw everything
    draw_player(player_x, player_y)
    draw_obstacle(obstacle_x, obstacle_y)
    show_score()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
