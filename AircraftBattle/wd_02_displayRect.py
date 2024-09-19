# author ChunLin Ren
# 2024.09.16

import pygame

pygame.init()
hero_rect = pygame.Rect(100, 500, 120, 125)

print("hero's original position %d %d" % (hero_rect.x, hero_rect.y))
print("hero's size %d %d" % (hero_rect.width, hero_rect.height))

print("%d %d" % hero_rect.size)

pygame.quit()