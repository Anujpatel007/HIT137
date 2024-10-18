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

# Resize images
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
player_image = pygame.transform.scale(player_image, (100, 150))
enemy_image = pygame.transform.scale(enemy_image, (100, 100))
bullet_image = pygame.transform.scale(bullet_image, (20, 20))
health_boost_image = pygame.transform.scale(health_boost_image, (50, 50))
extra_life_image = pygame.transform.scale(extra_life_image, (70, 70))
boss_image = pygame.transform.scale(boss_image, (120, 120))

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = player_image
        self.rect = self.surf.get_rect(midbottom=(100, SCREEN_HEIGHT - 100))
        self.health = 100
        self.lives = PLAYER_LIVES
        self.vel_y = 0
        self.on_ground = True
        self.score = 0
        
    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)
        if pressed_keys[K_j] and self.on_ground:   #To make the Kangaroo Jump
            self.vel_y = PLAYER_JUMP_STRENGTH
            self.on_ground = False
            
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0
            self.on_ground = True

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.lives -= 1
            if self.lives > 0:
                self.health = 100
            else:
                self.kill()
                
    def collect(self, collectible):
        if collectible.boost_type == "health":
            self.health = min(100, self.health + 20)
        elif collectible.boost_type == "life":
            self.lives += 1
        self.score += COLLECTIBLE_POINTS
        collectible.kill()
        
# Define the Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Projectile, self).__init__()
        self.surf = bullet_image
        self.rect = self.surf.get_rect(center=(x, y))
        self.damage = 10

    def update(self):
        self.rect.move_ip(10, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()
            
# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = enemy_image
        self.rect = self.surf.get_rect(center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100), SCREEN_HEIGHT - 50))
        self.speed = random.randint(1, 5)
        self.health = 30

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            Player.score += ENEMY_POINTS
            self.kill()
            
# Define the BossEnemy class
class BossEnemy(Enemy):
    def __init__(self):
        super(BossEnemy, self).__init__()
        self.surf = boss_image
        self.rect = self.surf.get_rect(midbottom=(SCREEN_WIDTH + 100, SCREEN_HEIGHT - 100))
        self.speed = 3
        self.health = 200
            
# Define the Collectible class
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y, boost_type="health"):
        super(Collectible, self).__init__()
        if boost_type == "health":
            self.surf = health_boost_image
        elif boost_type == "life":
            self.surf = extra_life_image
        self.rect = self.surf.get_rect(center=(x, y))
        self.boost_type = boost_type
        