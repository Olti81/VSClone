# Vampire Survivors Clone - Made by ChatGPT & OTH

# Imports
import pygame
import sys
import random
import time
from audio import sound
from screens.screen import screen, font
from screens.deathscreen import death_screen
from screens.startscreen import start_screen
from vars import *
from constants import *

# pygame.init() - Initialize Pygame
pygame.init()



# Game sprites
player_image = pygame.image.load("assets\\player\\player.png")

# function - Spawn new enemy
def spawn_enemy():
    enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
    enemy_y = random.randint(0, SCREEN_HEIGHT - ENEMY_SIZE)
    enemies.append([enemy_x, enemy_y])

# function - Fire missile
def fire_missile(player_x, player_y, enemies):
    if not enemies:
        return  # No enemies to target

    # Find the nearest enemy
    nearest_enemy = min(enemies, key=lambda e: ((e[0] - player_x)**2 + (e[1] - player_y)**2)**0.5)
    
    # Calculate missile direction
    direction_x = nearest_enemy[0] - player_x
    direction_y = nearest_enemy[1] - player_y
    magnitude = (direction_x**2 + direction_y**2)**0.5
    direction_x, direction_y = direction_x / magnitude, direction_y / magnitude

    # Create a new missile
    missiles.append([player_x + PLAYER_SIZE/2, player_y + PLAYER_SIZE/2, direction_x, direction_y])

# function - Remove hit enemy
def remove_hit_enemies():
    global kill_count  # This allows us to modify the global kill_count variable
    global xp # This allows us to modify the global xp variable
    global xp_level # This allows us to modify the global xp_level variable
    global level # This allows us to modify the global level variable
    for missile in missiles:
        missile_rect = pygame.Rect(missile[0], missile[1], MISSILE_SIZE, MISSILE_SIZE)
        for enemy in enemies[:]:
            enemy_rect = pygame.Rect(enemy[0], enemy[1], ENEMY_SIZE, ENEMY_SIZE)
            if missile_rect.colliderect(enemy_rect):
                enemies.remove(enemy)
                missiles.remove(missile)
                kill_count += 1  # Increment the kill counter when an enemy is hit
                sound.explosion_sound.play() # Plays at 2x speed
                xp_orbs.append([enemy[0], enemy[1]]) 
                break

# Calculate XP required for next level
def calculate_xp_required():
  global xp_required
  xp_required = xp_required * 1.1
  return int(xp_required)

# Check for collision between player and enemy
def check_collision(player_rect, enemy_rect):
  if player_rect.colliderect(enemy_rect):
    return True # Return True if collision
  return False # No collision

def handle_player_hit():

    # Collision detected
    print("Collision!")
    enemies.clear()
    sound.death_sound.play()
    # Add a 1 second delay
    pygame.time.wait(1000)
    # Show Death Screen
    death_screen()

######################################################################
# SHOW THE STARTING SCREEN OF THE GAME
start_screen()

# game_loop_start
# MAIN GAME LOOP
while running:
    current_time = time.time() * 1000  # Current time in milliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for keys pressed
    keys = pygame.key.get_pressed()
    new_x = player_x
    new_y = player_y
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        new_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        new_x += PLAYER_SPEED
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        new_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        new_y += PLAYER_SPEED

    # Boundary checks to keep the player within the window
    player_x = max(0, min(SCREEN_WIDTH - PLAYER_SIZE, new_x))
    player_y = max(0, min(SCREEN_HEIGHT - PLAYER_SIZE, new_y))

    # When player levels up
    if xp >= xp_level:
        level += 1
        xp -= xp_level
        sound.xp_levelup_sound.play()
        
        # Increase XP required for next level
        xp_level = calculate_xp_required()

    # Fire missiles at a regular interval
    if current_time - last_missile_time > missile_fire_rate:
        fire_missile(player_x, player_y, enemies)
        last_missile_time = current_time

    # Spawn enemy periodically
    if len(enemies) < 10:  # Limit the number of enemies
        spawn_enemy()

    # Move enemies towards the player
    for enemy in enemies:
        if enemy[0] < player_x:
            enemy[0] += ENEMY_SPEED
        elif enemy[0] > player_x:
            enemy[0] -= ENEMY_SPEED
        if enemy[1] < player_y:
            enemy[1] += ENEMY_SPEED
        elif enemy[1] > player_y:
            enemy[1] -= ENEMY_SPEED

	#Remove enemies hit by missiles
    remove_hit_enemies()

# RENDER LOGIC

    # Fill the screen with background color
    screen.fill(BG_COLOR)
	
	# Draw Kill Counter
    kill_count_text = font.render(f'Kills: {kill_count}', True, (255, 255, 255))
    screen.blit(kill_count_text, (SCREEN_WIDTH - kill_count_text.get_width() - 10, 10))

    # Draw XP meter 
    xp_meter_rect = pygame.Rect(10, 10, xp/xp_level * XP_METER_WIDTH, XP_METER_HEIGHT)
    pygame.draw.rect(screen, XP_METER_COLOR, xp_meter_rect)

    # Draw Player level text
    level_text = font.render("LVL " + str(level), True, (125, 125, 0))  
    screen.blit(level_text, (10, 35))

    # Draw the player
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)

    # Draw enemies
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], ENEMY_SIZE, ENEMY_SIZE)
        pygame.draw.rect(screen, ENEMY_COLOR, enemy_rect)
        if check_collision(player_rect, enemy_rect):
            handle_player_hit()
        #collision = check_collision(player_rect, enemy_rect)
        #if collision:
        #    death_screen()

    # Update and draw missiles
    for missile in missiles[:]:
        missile[0] += missile[2] * MISSILE_SPEED
        missile[1] += missile[3] * MISSILE_SPEED
        missile_rect = pygame.Rect(missile[0], missile[1], MISSILE_SIZE, MISSILE_SIZE)
        pygame.draw.rect(screen, MISSILE_COLOR, missile_rect)

        # Remove missile if it goes off-screen
        if (missile[0] < 0 or missile[0] > SCREEN_WIDTH or
            missile[1] < 0 or missile[1] > SCREEN_HEIGHT):
            missiles.remove(missile)
        
    # Draw the XP orbs on the screen
    for orb in xp_orbs:
        pygame.draw.circle(screen, XP_ORB_COLOR, orb, XP_ORB_SIZE)
        # Calculate distance between orb and player
        dist = ((orb[0] - player_x)**2 + (orb[1] - player_y)**2)**0.5
        
        # Orb is within 100 pixels, move towards player
        if dist < 100: 
            if orb[0] < player_x:
                orb[0] += 1
            elif orb[0] > player_x:
                orb[0] -= 1

            if orb[1] < player_y:
                orb[1] += 1 
            elif orb[1] > player_y:
                orb[1] -= 1
    
    for orb in xp_orbs[:]:
        orb_rect = pygame.Rect(orb[0], orb[1], XP_ORB_SIZE, XP_ORB_SIZE) 
        if player_rect.colliderect(orb_rect):
            xp_orbs.remove(orb)
            xp += XP_INCREMENT
            sound.xp_pickup_sound.play()

	# Refresh the screen
    pygame.display.flip()

# Exiting the game and terminating the script 22
# Quit the game
pygame.quit()
sys.exit()