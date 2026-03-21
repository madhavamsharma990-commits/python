import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Custom Event - Change Sprite Color")

# 1. Define a Custom Event
# We add 1 to USEREVENT to ensure it's a unique ID
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# 2. Create the Sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        # Generate a random RGB color
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(new_color)

# 3. Create two sprites and add them to a group
sprite1 = MySprite((255, 0, 0), 150, 175) # Red Sprite
sprite2 = MySprite((0, 0, 255), 300, 175) # Blue Sprite
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# 4. Set a timer to trigger the custom event every 2000ms (2 seconds)
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 5. Check if our custom event was triggered
        if event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.change_color()

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
