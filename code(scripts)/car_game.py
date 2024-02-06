##Run the code th play the game

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
CAR_WIDTH, CAR_HEIGHT = 30, 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Load images
car_img = pygame.image.load("/Users/mohammadelmasri/Desktop/MOE350/code(scripts)/red_car.png").convert_alpha()
car_img = pygame.transform.scale(car_img, (CAR_WIDTH, CAR_HEIGHT))
car_rect = car_img.get_rect(center=(WIDTH // 2, HEIGHT - 50))

enemy_img = pygame.image.load("/Users/mohammadelmasri/Desktop/MOE350/code(scripts)/blue_car.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (CAR_WIDTH, CAR_HEIGHT))
car_rect = enemy_img.get_rect(center=(WIDTH // 2, HEIGHT - 50))
# Clock to control the frame rate
clock = pygame.time.Clock()

# Game variables
speed = 5
car_speed = 0
enemy_speed = 5
enemies = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_rect.left > 0:
        car_speed = -speed
    elif keys[pygame.K_RIGHT] and car_rect.right < WIDTH:
        car_speed = speed
    else:
        car_speed = 0

    # Move the car
    car_rect.x += car_speed

    # Spawn enemies
    if random.randint(1, 100) < 5:
        enemy_x = random.randint(0, WIDTH - CAR_WIDTH)
        enemy_rect = enemy_img.get_rect(center=(enemy_x, 0))
        enemies.append(enemy_rect)

    # Move and remove enemies
    for enemy_rect in enemies:
        enemy_rect.y += enemy_speed
        if enemy_rect.y > HEIGHT:
            enemies.remove(enemy_rect)

    # Check collisions with enemies
    for enemy_rect in enemies:
        if car_rect.colliderect(enemy_rect):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), 2)
    screen.blit(car_img, car_rect)
    for enemy_rect in enemies:
        screen.blit(enemy_img, enemy_rect)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)
