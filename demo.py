from typing import Any

import pygame
import sys, random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

snake_pos = [100, 100]
direction = [20,20]
food_pos = [random.randrange(0, 40) * 20, random.randrange(0, 30) * 20]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = [0, -20]
            elif event.key == pygame.K_DOWN:
                direction = [0, 20]
            elif event.key == pygame.K_LEFT:
                direction = [-20, 0]
            elif event.key == pygame.K_RIGHT:
                direction = [20, 0]

    snake_pos[0] += direction[0]
    snake_pos[1] += direction[1]

    if snake_pos[0] < 0 or snake_pos[0] >= 800 or snake_pos[1] < 0 or snake_pos[1] >= 600:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    if snake_pos == food_pos:
        food_pos = [random.randrange(0, 40) * 20, random.randrange(0, 30) * 20]

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (*snake_pos, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (*food_pos, 20, 20))
    pygame.display.flip()
    clock.tick(10)
