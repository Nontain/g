from pygame import *
from Character import CharacterSprite
from Enemy import EnemySprite
from Wall import Wall

window = display.set_mode((1200, 800))
display.set_caption("Catch")

background = transform.scale(image.load("assets/background.jpg"), (1200, 800))
print("\t__\n__")
window.blit(background, (0,0))
# window.blit(background1, (250,250))

c1 = CharacterSprite('assets/Cave_Vines.webp', 100, 100, 1)
c2 = EnemySprite('assets/spider.webp', 100, 50, 0.5)

lavas = []
for i in range(8):
    lava = Wall("assets/lava.png",200+i*65,200)
    lavas.append(lava)



for i in range(8):
    lava = Wall("assets/lava.png",200+i*65,200)
    lavas.append(lava)


for i in range(8):
    lava3 = Wall("assets/lava.png",200+i*65,500)
    lavas.append(lava3)


for i in range(8):
    lava4 = Wall("assets/lava.png",400,200+i*65)
    lavas.append(lava4)


for i in range(8):
    lava8 = Wall("assets/lava.png",800,200+i*65)
    lavas.append(lava8)


clock = time.Clock()
FPS = 144
game = True 
while game:
    
    window.blit(background,(0, 0))
    # window.blit(background1,(0, 300))
    for e in event.get():
        if e.type == QUIT:
           game = False
    c1.update(window)
    c2.update(window)
    for lava in lavas:
        lava.update(window)
        if c1.collide(lava):
            c1.reset(window)
    c2.move_horizontal()
    if c1.collide(c2):
        print("Colision detected")
    c1.handle_events()
    
    display.update()
    clock.tick(FPS)