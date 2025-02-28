# author ChunLin Ren
# 2024.09.16
import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(150, 300, 102, 126)

while True:

    clock.tick(60)

    hero_rect.y -= 1
    if hero_rect.y < -hero_rect.height:
        hero_rect.y = 700

    screen.blit(hero, (0, 0))
    screen.blit(hero, hero_rect)

    pygame.display.update()

pygame.quit()
