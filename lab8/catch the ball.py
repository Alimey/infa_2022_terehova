from random import randint

import pygame
from pygame.draw import *


pygame.init()

FPS = 100

screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS_CIRCLE = [BLUE, CYAN]
COLORS_RECT = [RED, YELLOW, MAGENTA]

def speed():
    ''' Задает начальную скорость шара, выдает списком скорость по x и по y  '''
    speed_x = randint(-10, -1)
    speed_y = randint(-10, -1)
    return [speed_x, speed_y]

def new_ball():
    ''' рисует новый шарик, возвращает его, его цвет, скорости по x и y'''
    
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(15, 30)
    color = COLORS_CIRCLE[randint(0, 1)]
    
    c = circle(screen, color, (x, y), r)
    speed_x, speed_y = speed()

    return [c, color, speed_x, speed_y]


def numb_of_balls(n=2):
    ''' Рисует определенное число шариков и возвращает их список '''
    
    balls = []
    for i in range(n):
        balls.append(new_ball())

    return balls


def click_ball(event, balls):
    '''
        Получает координаты клика и список шаров,
        возвращает bool значение: кликнули по шару или нет
    '''
    result = False
    x,y = event.pos

    for i in range(len(balls)):
        x_center = balls[i][0][0]+balls[i][0][2]/2
        y_center = balls[i][0][1]+balls[i][0][2]/2
        r = balls[i][0][2]/2
        if (x-x_center)**2 + (y-y_center)**2 <= r**2:
            result = True
            break
    if result:
        print('It\'s a ball!')
    else:
        print('It\'s not a ball.')
    return result


def reflection_up(ball):
    ''' Получает шар и отражает его от верхней стенки '''
    ball[0][1] = 1
    ball[3] = randint(1, 11)

def reflection_down(ball):
    ''' Получает шар и отражает его от нижней стенки '''
    ball[0][1] = 900-ball[0][2]-1
    ball[3] = randint(-10, -1)

def reflection_left(ball):
    ''' Получает шар и отражает его от левой стенки '''
    ball[0][0] = 1
    ball[2] = randint(1, 11)

def reflection_right(ball):
    ''' Получает шар и отражает его от правой стенки '''
    ball[0][0] = 1200-ball[0][2]-1
    ball[2] = randint(-10, -1)


def where_is_ball(ball):
    '''  Получает шар, возвращает bol значение: ударяется шар о стенку или нет '''
    result = False
    if (ball[0][0] >= 1200-ball[0][2]) | (ball[0][0] <= 0):
        result = True
    if (ball[0][1] >= 900-ball[0][2]) | (ball[0][1] <= 0):
        result = True
    return result
    
def wall(ball):
    ''' Получает шар, возвращает стенку, о которую шар ударяется '''
    wall = ''
    if ball[0][0] >= 1200-ball[0][2]:
        wall = 'r'
    if ball[0][0] <= 0:
        wall = 'l'
    if ball[0][1] >= 900-ball[0][2]:
        wall = 'd'
    if ball[0][1] <= 0:
        wall = 'u'
    return wall


def move_balls(balls):
    ''' Получает список шаров, перемещает их '''
    for i in range(len(balls)):
        if not where_is_ball(balls[i]):
            balls[i][0].move_ip(balls[i][2], balls[i][3])
        else:
            w = wall(balls[i])
            if w == 'r':
                reflection_right(balls[i])
            if w == 'l':
                reflection_left(balls[i])
            if w == 'u':
                reflection_up(balls[i])
            if w == 'd':
                reflection_down(balls[i])
                
        c_from_rect_x = balls[i][0][0]+balls[i][0][3]/2
        c_from_rect_y = balls[i][0][1]+balls[i][0][3]/2
        c_from_rect_r = balls[i][0][3]/2
        circle(screen, balls[i][1], (c_from_rect_x, c_from_rect_y), c_from_rect_r)


def new_rectangle():
    ''' Рисует прямоугольник, возвращает списком его, его цвет и скорости '''
    x = randint(100, 1100)
    y = randint(100, 900)
    a = randint(50, 300)
    b = randint(50, 100)
    color = COLORS_RECT[randint(0, 2)]
    
    r = pygame.Rect((x, y, a, b))
    rect(screen, color, (x, y, a, b), 0)
    speed_x, speed_y = speed()

    return [r, color, speed_x, speed_y]


def numb_of_rectangles(n=2):
    ''' Рисует определенное число произвольных прямоугольников, возвращает их список '''
    rects = []
    for i in range(n):
        rects.append(new_rectangle())

    return rects


def click_rect(event, rects):
    '''
        Получает координаты клика и список прямоугольников,
        возвращает bool значение: кликнули по прямоугольнику или нет
    '''
    result = False
    x,y = event.pos

    for i in range(len(rects)):
        if (x >= rects[i][0][0]) and (x <= rects[i][0][0]+rects[i][0][2]) and (y >= rects[i][0][1]) and (y <= rects[i][0][1]+rects[i][0][3]):
            result = True
            break
    if result:
        print('It\'s a rect! You loose 1 point.')
        
    return result

def print_rects(rects):
    ''' Рисует прямоугольники из rects '''
    for i in range(len(rects)):
        color_i = rects[i][1]
        x_i = rects[i][0][0]
        y_i = rects[i][0][1]
        a_i = rects[i][0][2]
        b_i = rects[i][0][3]
        rect(screen, color_i, (x_i, y_i, a_i, b_i), 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
balls = numb_of_balls(20)
rects = numb_of_rectangles(20)
score = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            cl_c = click_ball(event, balls)
            cl_r = click_rect(event, rects)
            if cl_c:
                score+=1
            if cl_r:
                score-=1
                rects = numb_of_rectangles(20)
            print('Your score: ', score, '\n')
    screen.fill((0,0,0))
    print_rects(rects)
    move_balls(balls)
    pygame.display.update()

pygame.quit()
