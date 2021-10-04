import pygame
from pygame.draw import *
import typing


def shift_points(
        points: typing.List[typing.Tuple[int, int]], 
        delta_x: int = 0, delta_y: int = 0) -> typing.List[typing.Tuple[int, int]]:
    """Shift all points in an array by a constant vector"""
    return [(x + delta_x, y + delta_y) for x, y in points]

pygame.init()
FPS = 30
# Fun fact: on some linux distributions, if you add pygame.FULLSCREEN below, it will break the whole system
# (shortcuts will stop working, you will only be ably to kill the process in another tty, but then the **system**
# screen resolution will change to the one that is written in set_mode)
# Like I said, fun
screen = pygame.display.set_mode((1500, 870))

rect(screen, (211, 211, 211), (0, 0, 1500, 870))
def person(s, delta_x, color_1, color_2, color_3):      
    """Draw a person"""
    # Polygons: (list of coordinates, fill color, [stroke color])
    polygons = [
            ([(244, 699), (286, 689), (210, 145), (168, 154)], (255, 228, 196)),
            ([(860, 698), (915, 160), (870, 158), (820, 678)], (255, 228, 196)),
            # Shirt
            ([(860, 698), (915, 160), (870, 158), (820, 678)], color_2),
            ([(774, 848), (716, 745), (785, 651), (887, 695), (881, 819)], color_2, (0, 0, 0)),
            ([(333, 843), (223, 828), (211, 709), (313, 651), (388, 735)],
                color_2, (0, 0, 0)),
            ([(550, 550), (525, 508), (575, 508)], (139, 69, 19), (139, 0, 0)),
            ([(400, 570), (550, 665), (700, 570)], (255, 25, 0), (139, 0, 0)),
            # Hair triangles
            ([(312, 350), (275, 275), (356, 281)], color_3, (0, 0, 0)),
            ([(338, 300), (319, 223), (408, 255)], color_3, (0, 0, 0)),
            ([(382, 266), (377, 184), (455, 225)], color_3, (0, 0, 0)),
            ([(424, 242), (430, 160), (500, 210)], color_3, (0, 0, 0)),
            ([(475, 220), (504, 145), (554, 210)], color_3, (0, 0, 0)),
            ([(533, 217), (558, 150), (613, 221)], color_3, (0, 0, 0)),
            ([(600, 227), (639, 157), (667, 227)], color_3, (0, 0, 0)),
            ([(653, 228), (725, 192), (721, 273)], color_3, (0, 0, 0)),
            ([(704, 249), (783, 230), (759, 308)], color_3, (0, 0, 0)),
            ([(746, 282), (827, 279), (790, 351)], color_3, (0, 0, 0))
        ]
    x = delta_x
    for polygon_data in polygons:
        polygon_data = list(polygon_data) + [None]
        polygon_data[0] = shift_points(polygon_data[0], delta_x)
        if polygon_data[1] is not None:
            polygon(s, polygon_data[1], polygon_data[0])
        if polygon_data[2] is not None:
            polygon(s, polygon_data[2], polygon_data[0], 1)
    circles = [
            ((550, 938), 296, color_2, None),
            ((550, 495), 280, (255, 228, 196), None),
            # Eyes
            ((460, 444), 58, color_1, (0, 0, 0)),
            ((637, 444), 58, color_1, (0, 0, 0)),
            ((641, 449), 17, (0, 0, 0), None),
            ((459, 449), 17, (0, 0, 0), None)
        ]
    for circle_data in circles:
        circle_data = list(circle_data)
        circle_data[0] = (circle_data[0][0] + delta_x, circle_data[0][1])
        if circle_data[2] is not None:
            circle(s, circle_data[2], circle_data[0], circle_data[1])
        if circle_data[3] is not None:
            circle(s, circle_data[3], circle_data[0], circle_data[1], 1)
    ellipses = [
            ((130, 37, 108, 129), (255, 228, 196), (255, 248, 220)),
            ((837, 45, 128, 134), (255, 228, 196), (255, 248, 220))
        ]


# draw people
person(screen, -150, (144, 238, 144), (0, 128, 0), (255, 255, 0))
person(screen, 550, (0, 191, 255), (255, 69, 0), (148, 0, 211))

# Background
rect(screen, (127, 255, 0), (2, 2, 1498, 110))
rect(screen, (0, 0, 0), (2, 2, 1498, 110), 1)


# Write text on top
f1 = pygame.font.Font(None, 140)
text1 = f1.render('PYTHON is REALLY AMAZING!', True, (0, 0, 0))
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
