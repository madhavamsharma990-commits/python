import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Load Background Image
# Ensure 'background.png' is in the same folder as your script
background = pygame.image.load('background.png')

# Game Loop
running = True
while running:
    # Draw the background at the top-left corner (0,0)
    # This should be the first thing drawn in the loop
    screen.blit(background, (0, 0))
    
    # ... rest of your player/enemy drawing code ...
    
    pygame.display.update()
from pygame import mixer

# Load Background Sound
# .wav or .mp3 files work best
mixer.music.load('background.wav')

# Play the music
# The '-1' means the music will play on an infinite loop
mixer.music.play(-1)
# Load a short sound effect
bullet_sound = mixer.Sound('laser.wav')

# Inside your event loop (e.g., when the spacebar is pressed):
bullet_sound.play()
