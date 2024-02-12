from Character import CharacterSprite
from pygame import *

class EnemySprite(CharacterSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction_x = 1
        
    def move_horizontal(self):
        if self.rect.x <= 0:
            self.direction_x = 1
        elif self.rect.x >= 635:
            self.direction_x = -1
        self.rect.x += self.speed * self.direction_x