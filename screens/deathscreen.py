from screens.screen import screen, death_font
from screens.startscreen import start_screen
import time
from vars import *
import pygame


# DEATH SCREEN
def death_screen():
    running = True
    start_time = time.time()
    while running:
        # Fill screen with RED
        screen.fill((255, 0, 0))
        # Render Text
        death_text = death_font.render("YOU HAVE DIED", True, (255, 255, 255))  # Death Text
        # Get text position
        death_text_rect = death_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        # Draw Text
        screen.blit(death_text, death_text_rect)
        pygame.display.update()
        if time.time() - start_time > 15:
            running = False
            start_screen()
        pygame.time.wait(100) # Pause for 100 ms each loop