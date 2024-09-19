# author ChunLin Ren
# 2024.09.16

import pygame

pygame.init()
print("Game code")

clock = pygame.time.Clock()
i=0
while True:
    clock.tick(60)

    print(i)
    i += 1

pygame.quit()