import pygame
from pygame import mixer

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load Assets
background = pygame.image.load('background.png')

# Load and Play Background Music
mixer.music.load('background.wav')
mixer.music.play(-1)

# Load Sound Effect
bullet_sound = mixer.Sound('laser.wav')

running = True
while running:
    # Set the background image
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Example: Play sound when a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_sound.play()

    pygame.display.update()
from pygame import mixer
mixer.music.load('background.wav') 

mixer.music.play(-1)
bullet_sound = mixer.Sound('laser.wav')

