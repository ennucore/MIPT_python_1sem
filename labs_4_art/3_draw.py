import pygame
from pygame.draw import *

pygame.init()
pygame.font
FPS = 30
screen = pygame.display.set_mode((1500, 870))

rect(screen, (211, 211, 211), (0, 0, 1500, 870))
def person(x, e1, e2, e3, s1, s2, s3, h1, h2, h3):      
    polygon(screen, (255, 228, 196), [(244 + x, 699), (286 + x, 689), (210 + x, 145), (168 + x, 154), (244 + x, 699)])
    polygon(screen, (255, 228, 196), [(860 + x, 698), (915 + x, 160), (870 + x, 158), (820 + x, 678), (860 + x, 698)])
    circle(screen, (s1, s2, s3), (550 + x, 938), 296)
    polygon(screen, (s1, s2, s3), [(774 + x, 848), (716 + x, 745), (785 + x, 651), (887 + x, 695), (881 + x, 819), (774 + x, 848)])
    polygon(screen, (0, 0, 0), [(774 + x, 848), (716 + x, 745), (785 + x, 651), (887 + x, 695), (881 + x, 819), (774 + x, 848)], 1)
    polygon(screen, (s1, s2, s3), [(333 + x, 843), (223 + x, 828), (211 + x, 709), (313 + x, 651), (388 + x, 735), (333 + x, 843)])
    polygon(screen, (0, 0, 0), [(333 + x, 843), (223 + x, 828), (211 + x, 709), (313 + x, 651), (388 + x, 735), (333 + x, 843)], 1)
    circle(screen, (255, 228, 196), (550 + x, 495), 280)
    circle(screen, (e1, e2, e3), (460 + x, 444), 58)
    circle(screen, (0, 0, 0), (460 + x, 444), 58, 1)
    circle(screen, (e1, e2, e3), (637 + x, 444), 58)
    circle(screen, (0, 0, 0), (637 + x, 444), 58, 1)
    circle(screen, (0, 0, 0), (641 + x, 449), 17)
    circle(screen, (0, 0, 0), (459 + x, 449), 17)
    polygon(screen, (139, 69, 19), [(550 + x, 550), (525 + x, 508), (575 + x, 508), (550 + x, 550)])
    polygon(screen, (139, 0, 0), [(550 + x, 550), (525 + x, 508), (575 + x, 508), (550 + x, 550)], 1)
    polygon(screen, (255, 25, 0), [(400 + x, 570), (550 + x, 665), (700 + x, 570), (400 + x, 570)])
    polygon(screen, (139, 0, 0), [(400 + x, 570), (550 + x, 665), (700 + x, 570), (400 + x, 570)], 1)
    polygon(screen, (h1, h2, h3), [(312 + x, 350), (275 + x, 275), (356 + x, 281), (312 + x, 350)])
    polygon(screen, (0, 0, 0), [(312 + x, 350), (275 + x, 275), (356 + x, 281), (312 + x, 350)], 1)
    polygon(screen, (h1, h2, h3), [(338 + x, 300), (319 + x, 223), (408 + x, 255), (338 + x, 300)])
    polygon(screen, (0, 0, 0), [(338 + x, 300), (319 + x, 223), (408 + x, 255), (338 + x, 300)], 1)
    polygon(screen, (h1, h2, h3), [(382 + x, 266), (377 + x, 184), (455 + x, 225), (382 + x, 266)])
    polygon(screen, (0, 0, 0), [(382 + x, 266), (377 + x, 184), (455 + x, 225), (382 + x, 266)], 1)
    polygon(screen, (h1, h2, h3), [(424 + x, 242), (430 + x, 160), (500 + x, 210), (424 + x, 242)])
    polygon(screen, (0, 0, 0), [(424 + x, 242), (430 + x, 160), (500 + x, 210), (424 + x, 242)], 1)
    polygon(screen, (h1, h2, h3), [(475 + x, 220), (504 + x, 145), (554 + x, 210), (475 + x, 220)])
    polygon(screen, (0, 0, 0), [(475 + x, 220), (504 + x, 145), (554 + x, 210), (475 + x, 220)], 1)
    polygon(screen, (h1, h2, h3), [(533 + x, 217), (558 + x, 150), (613 + x, 221), (533 + x, 217)])
    polygon(screen, (0, 0, 0), [(533 + x, 217), (558 + x, 150), (613 + x, 221), (533 + x, 217)], 1)
    polygon(screen, (h1, h2, h3), [(600 + x, 227), (639 + x, 157), (667 + x, 227), (600 + x, 227)])
    polygon(screen, (0, 0, 0), [(600 + x, 227), (639 + x, 157), (667 + x, 227), (600 + x, 227)], 1)
    polygon(screen, (h1, h2, h3), [(653 + x, 228), (725 + x, 192), (721 + x, 273), (653 + x, 228)])
    polygon(screen, (0, 0, 0), [(653 + x, 228), (725 + x, 192), (721 + x, 273), (653 + x, 228)], 1)
    polygon(screen, (h1, h2, h3), [(704 + x, 249), (783 + x, 230), (759 + x, 308), (704 + x, 249)])
    polygon(screen, (0, 0, 0), [(704 + x, 249), (783 + x, 230), (759 + x, 308), (704 + x, 249)], 1)
    polygon(screen, (h1, h2, h3), [(746 + x, 282), (827 + x, 279), (790 + x, 351), (746 + x, 282)])
    polygon(screen, (0, 0, 0), [(746 + x, 282), (827 + x, 279), (790 + x, 351), (746 + x, 282)], 1)

    ellipse(screen, (255, 228, 196), (130 + x, 37, 108, 129))
    ellipse(screen, (255, 248, 220), (130 + x, 37, 108, 129), 1)
    ellipse(screen, (255, 228, 196), (837 + x, 45, 128, 134))
    ellipse(screen, (255, 248, 220), (837 + x, 45, 128, 134), 1)
x_1 = -150
x_2 = 550

person(x_1, 144, 238, 144, 0, 128, 0, 	255, 255, 0)
person(x_2, 0, 191, 255, 255, 69, 0, 148, 0, 211)

rect(screen, (127, 255, 0), (2, 2, 1498, 110))
rect(screen, (0, 0, 0), (2, 2, 1498, 110), 1)


f1 = pygame.font.Font(None, 140)
text1 = f1.render('PYTHON is REALLY AMAZING!', True,
                  (0, 0, 0))
screen.blit(text1, (10, 5))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
