from pygame import *

mixer.init()
mixer.music.load("blud.mp3") 
mixer.music.play()
kick = mixer.Sound("blud.mp3")
kick.play()
window = display.set_mode((700, 500))
display.set_caption("catch")
background = transform.scale(image.load("C:\\Users\\BB\\Documents\\GitHub\\PyQt\demos\\background.jpg"), (700, 250))

x1 = 100
y1 = 300
x2 = 300
y2 = 300
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
speed = 10
#game loop

run = True
clock = time.Clock()
FPS = 144
white = (255,255,255) 
while run:
    window.fill((white))
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

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