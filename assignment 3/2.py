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

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Game with Levels, Enemies, and Collectibles")

# Setup the clock
clock = pygame.time.Clock()

# Load images
background_image = pygame.image.load("background.png").convert()
player_image = pygame.image.load("player.png").convert_alpha()
enemy_image = pygame.image.load("enemy.png").convert_alpha()
bullet_image = pygame.image.load("bullet.png").convert_alpha()
health_boost_image = pygame.image.load("health_boost.png").convert_alpha()
extra_life_image = pygame.image.load("extra_life.png").convert_alpha()
boss_image = pygame.image.load("boss.png").convert_alpha()