from pygame import *

x1 = 100
y1 = 300
x2 = 300
y2 = 300
speed = 10
#game loop

run = True
clock = time.Clock()
FPS = 144
white = (255,255,255) 
while run:



    for e in event.get():
        if e.type == QUIT:
            run = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed
    if keys_pressed[K_m]:
        kick.play()
    display.update()
    clock.tick(FPS)
