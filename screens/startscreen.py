# START SCREEN
def start_screen():
    running = True
    while running:
        background_music.play(-1)
        screen.blit(background_image, (0, 0))  # Draw the background image

        # Define buttons
        start_button = pygame.Rect(100, 100, 200, 50)  # Adjust size and position as needed
        exit_button = pygame.Rect(100, 200, 200, 50)  # Adjust size and position as needed

        # Draw buttons
        pygame.draw.rect(screen, (0, 255, 0), start_button)  # Green start button
        pygame.draw.rect(screen, (255, 0, 0), exit_button)  # Red exit button
        border = 5 
        pygame.draw.rect(screen, (0, 0, 0), start_button, border)
        pygame.draw.rect(screen, (0, 0, 0), exit_button, border)

        # Render text surfaces
        start_text = button_font.render("START", True, (0, 0, 0))  # White text
        exit_text = button_font.render("EXIT", True, (0, 0, 0))  # White text

        # Get text position
        start_text_rect = start_text.get_rect(center=start_button.center)
        exit_text_rect = exit_text.get_rect(center=exit_button.center)

        # Draw text
        screen.blit(start_text, start_text_rect)
        screen.blit(exit_text, exit_text_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    background_music.stop()
                    boom_sound.play()
                    return  # Start the game
                elif exit_button.collidepoint(event.pos):
                    background_music.stop()
                    pygame.quit()
                    sys.exit()

        # Update the display
        pygame.display.update()
