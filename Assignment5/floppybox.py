import pygame,sys

pygame.init()
screen = pygame.display.set_mode((400, 400))

while (1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(10, 10, 30, 20))
    pygame.draw.rect(screen, (255, 128, 0), pygame.Rect(50, 40, 30, 20))
    pygame.display.flip()