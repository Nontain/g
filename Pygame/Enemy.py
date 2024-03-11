from Character import CharacterSprite
from pygame import *

class Enemy2Sprite(CharacterSprite):
    def __init__(self, player2_image, player2_x, player2_y, player2_speed):
        super().__init__(player2_image, player2_x, player2_y, player2_speed)
        self.direction_x = 1
        
    def move_horizontal(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.move(-self.speed, 0)
        if keys[K_RIGHT]:
            self.move(self.speed, 0)
        if keys[K_UP]:
            self.move(0, -self.speed)
        if keys[K_DOWN]:
            self.move(0, self.speed)
