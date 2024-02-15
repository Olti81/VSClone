import pygame

# Game sprites
player_img = pygame.image.load("player\\player.png")
# Create scaled surface 
player_img = pygame.transform.scale(player_img, (50, 50))