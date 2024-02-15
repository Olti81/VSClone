from constants import *
import time

# DEFINED VARIABLES
running = True
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
enemies = []    # List to hold all active enemies on screen
missiles = []   # List to hold all active missiles on screen
xp_orbs = []    # List to hold the XP orbs on screen
last_missile_time = 0
missile_fire_rate = 1000  # Fire every 1000 milliseconds (1 second)
current_time = time.time() * 1000
kill_count = 0  # Initialize the kill counter
xp = 0          # Staring XP
xp_level = 100  # How much XP for one levelup
level = 0       # Starting level at 0
xp_required = 100 # XP required to reach next level