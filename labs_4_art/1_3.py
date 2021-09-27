import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

rect(screen, (128, 128, 128), (0, 0, 600, 600))
#rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
#polygon(screen, (255, 255, 0), [(100,100), (200,10), (300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               #(300,100), (100,100)], 5)
circle(screen, (255, 255, 0), (300, 300), 150)
rect(screen, (0, 0, 0), (220, 380, 150, 25))
circle(screen, (255, 0, 0), (240, 240), 28)
circle(screen, (255, 0, 0), (360, 240), 20)
circle(screen, (0, 0, 0), (240, 240), 14)
circle(screen, (0, 0, 0), (360, 240), 10)
polygon(screen, (0, 0, 0), [(200,200), (250,250), (300, 350), (230, 230), (200, 200)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
