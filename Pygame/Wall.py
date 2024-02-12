from Character import CharacterSprite
from pygame import *


class Wall(CharacterSprite):
    def __init__(self, image_path, x, y, size=(65, 65)):
        super().__init__(image_path, x, y, 0,(65, 65))
        self.direction_x = 1