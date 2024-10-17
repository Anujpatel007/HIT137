import pygame
import random
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, K_SPACE, K_j, KEYDOWN, QUIT,
)
# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Constants for game mechanics
GRAVITY = 0.5
PLAYER_JUMP_STRENGTH = -12
PLAYER_SPEED = 5
PLAYER_LIVES = 3
ENEMY_POINTS = 10
COLLECTIBLE_POINTS = 5