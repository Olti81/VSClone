import sys
from audio import sound
from screens import screen
from assets import *
from vars import *
import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH

# Screen and display setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Vampire Survivors Clone')

# Fonts and text setup
pygame.font.init()  # Initialize font module
font = pygame.font.SysFont(None, 36)
button_font = pygame.font.SysFont(None, 40)  # Choose a font and size
death_font = pygame.font.SysFont(None, 64)

# Background image for start_screen()
background_image = pygame.image.load('assets\\genie.jpg')  # Replace with your image file
background_image = pygame.transform.scale(background_image, (1280, 1024))  # Scale to window size