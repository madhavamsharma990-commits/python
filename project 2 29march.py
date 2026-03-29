import pygame
import random

# 1. Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader - Part 1")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 2. Define the Sprite Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(BLUE) # Player is Blue
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    def update(self):
        # Basic movement with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED) # Enemies are Red
        self.rect = self.image.get_rect()
        # Positioned randomly on the screen
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(50, SCREEN_HEIGHT // 2)

# 3. Create Sprite Groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Add one player
player = Player()
all_sprites.add(player)

# Add seven enemy sprites
for i in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# 4. Game Variables
score = 0
font = pygame.font.SysFont("Arial", 24)
running = True
clock = pygame.time.Clock()

# 5. Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Collision Detection
    # If player hits an enemy, increase score and reset enemy position
    hits = pygame.sprite.spritecollide(player, enemies, True)
    for hit in hits:
        score += 1
        # To keep 7 enemies, spawn a new one when one is hit
        new_enemy = Enemy()
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)

    # Drawing
    screen.fill((0, 0, 0)) # Black background
    all_sprites.draw(screen)
    
    # Display Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()