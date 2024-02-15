import pygame

# SOUND INIT
pygame.mixer.init()

background_music = pygame.mixer.Sound("audio\\background.flac")
background_music.set_volume(0.2) # Optional volume 0 to 1
explosion_sound = pygame.mixer.Sound("audio\\explosion.wav")
explosion_sound.set_volume(0.2) # Optional volume 0 to 1
xp_pickup_sound = pygame.mixer.Sound("audio\\xp_pickup.wav")
xp_pickup_sound.set_volume(0.2) # Optional volume 0 to 1
xp_levelup_sound = pygame.mixer.Sound("audio\\xp_levelup.wav")
xp_levelup_sound.set_volume(0.8) # Optional volume 0 to 1
boom_sound = pygame.mixer.Sound("audio\\boom.wav")
boom_sound.set_volume(0.5) # Optional volume 0 to 1
death_sound = pygame.mixer.Sound("audio\\death.wav")
death_sound.set_volume(1) # Optional volume 0 to 1