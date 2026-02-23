import pygame
import sys 
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Pygame Screen")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    screen.fill(BLUE)
    pygame.display.flip() 
pygame.quit()
sys.exit()