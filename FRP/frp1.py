import kandinsky as kd
import ion
import time

# Constants
WIDTH, HEIGHT = 320, 240  # Screen size
MARIO_SIZE = 10  # Mario's size
GRAVITY = 1
JUMP_POWER = -10
MOVE_SPEED = 5

ground_level = HEIGHT - 30

# Mario's starting position
mario_x = 50
mario_y = ground_level - MARIO_SIZE
mario_vy = 0

def draw_mario(x, y):
    kd.fill_rect(x, y, MARIO_SIZE, MARIO_SIZE, (255, 0, 0))  # Red square

def draw_background():
    kd.fill_rect(0, 0, WIDTH, HEIGHT, (135, 206, 235))  # Sky blue
    kd.fill_rect(0, ground_level, WIDTH, 30, (0, 255, 0))  # Ground (green)

while True:
    draw_background()
    draw_mario(mario_x, mario_y)
    
    # Movement
    if ion.keydown(ion.KEY_LEFT):
        mario_x = max(0, mario_x - MOVE_SPEED)  # Stay in bounds
    if ion.keydown(ion.KEY_RIGHT):
        mario_x = min(WIDTH - MARIO_SIZE, mario_x + MOVE_SPEED)
    
    # Jumping
    if ion.keydown(ion.KEY_OK) and mario_y == ground_level - MARIO_SIZE:
        mario_vy = JUMP_POWER
    
    # Gravity
    mario_vy += GRAVITY
    mario_y += mario_vy
    
    # Ground collision
    if mario_y >= ground_level - MARIO_SIZE:
        mario_y = ground_level - MARIO_SIZE
        mario_vy = 0
    
    time.sleep(0.05)
