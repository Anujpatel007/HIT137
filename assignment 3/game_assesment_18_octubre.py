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
            player.score += ENEMY_POINTS
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

# Create player instance
player = Player()

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
collectibles = pygame.sprite.Group()

# Levels and Game Control
level = 1
total_levels = 3
game_over = False

# Function to draw the health and score UI
def draw_ui(player, screen):
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
    score_text = font.render(f'Score: {player.score}', True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))
    screen.blit(score_text, (10, 40))

    # Health bar
    bar_width = 200
    fill = (player.health / 100) * bar_width
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 70, fill, 20))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, 70, bar_width, 20), 2)

# Function to handle game over and restart
def display_game_over(screen):
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.wait(3000)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
        if event.type == KEYDOWN and event.key == K_SPACE and not game_over:
            bullet = Projectile(player.rect.right, player.rect.centery)
            bullets.add(bullet)
            all_sprites.add(bullet)

    # Update objects
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    bullets.update()
    collectibles.update()

    # Add enemies and collectibles based on level
    if level <= total_levels and random.random() < 0.01 * level:
        new_enemy = Enemy()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)

    if level <= total_levels and random.random() < 0.005:
        collectible_type = random.choice(["health", "life"])
        new_collectible = Collectible(random.randint(50, SCREEN_WIDTH - 50), SCREEN_HEIGHT - 50, collectible_type)
        collectibles.add(new_collectible)
        all_sprites.add(new_collectible)

    # Check if bullets hit enemies
    for bullet in bullets:
        enemy_hit = pygame.sprite.spritecollideany(bullet, enemies)
        if enemy_hit:
            enemy_hit.take_damage(bullet.damage)
            bullet.kill()

    # Check if player collects items
    for collectible in pygame.sprite.spritecollide(player, collectibles, False):
        player.collect(collectible)

    # Check if enemies collide with player
    if pygame.sprite.spritecollideany(player, enemies):
        player.take_damage(10)

    # Check for game over
    if player.lives <= 0:
        display_game_over(screen)
        running = False

    # Draw background and all sprites
    screen.blit(background_image, (0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    # Draw UI
    draw_ui(player, screen)

    # Update display
    pygame.display.flip()

    # Ensure the game runs at 30 frames per second
    clock.tick(30)

# Quit the game
pygame.quit()
