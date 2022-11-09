import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill('white')

circle(screen, 'yellow', (200, 200), 100, width = 0)
circle(screen, 'black', (200, 200), 100, width = 1)

circle(screen, 'red', (160, 170), 20, width = 0)
circle(screen, 'black', (160, 170), 20, width = 1)
circle(screen, 'black', (160, 170), 8.5, width = 0)

circle(screen, 'red', (250, 170), 15, width = 0)
circle(screen, 'black', (250, 170), 15, width = 1)
circle(screen, 'black', (250, 170), 7.5, width = 0)

rect(screen, 'black', (150, 250, 100, 20), width=0)

polygon(screen, 'black', [(80, 112),(84, 104),(190, 150),(186, 160)], width=0)
polygon(screen, 'black', [(309, 137),(306, 129),(220, 155),(224, 165)], width=0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
