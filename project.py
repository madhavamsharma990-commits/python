import pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic Game Screen")
# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Rectangle settings
rect_x = 50
rect_y = 50
rect_width = 100
rect_height = 100

# Font settings
font = pygame.font.SysFont(None, 55)
text = font.render('Hello Pygame', True, BLACK)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen
    screen.fill(WHITE)
    
    # Draw Rectangle
    pygame.draw.rect(screen, BLUE, [rect_x, rect_y, rect_width, rect_height])
    
    # Draw Text
    screen.blit(text, (200, 200))
    
    # Update display
    pygame.display.flip()

pygame.quit()