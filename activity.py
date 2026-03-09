import pygame

import random

# Constants for easier adjustments

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400

MOVEMENT_SPEED = 5

FONT_SIZE = 72

# Initialize Pygame

pygame.init()

# Load and transform the background image

background_image = pygame.transform.scale(pygame.image.load("img.jpg"),(SCREEN_WIDTH, SCREEN_HEIGHT))

# Load font once at the beginning

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)