import game
from vector import Vector
import math
import pygame

class Square():
    """Position is the centre of the square"""
    def __init__(self, position: Vector, velocity: Vector, size: int, rotation=0) -> None:
        self.position = position
        self.velocity = velocity
        self.size = size
        self.rotation = rotation
        self.colour = (255, 0, 0)

    def draw(self):
        if type(self) == Square: self.rotation += 0.5
        surf1 = pygame.Surface((self.size, self.size), flags=pygame.SRCALPHA)
        pygame.draw.rect(surf1, self.colour, (0, 0, self.size, self.size))
        surf2 = pygame.transform.rotate(surf1, self.rotation)
        game.WIN.blit(surf2, (float(self.position.x)-(surf2.get_width()-surf1.get_width())/2, float(self.position.y)-(surf2.get_height()-surf1.get_height())/2))



class Immovable(Square):
    def __init__(self, position: Vector, velocity: Vector, size: int) -> None:
        super().__init__(position, velocity, size)
        self.colour = (0, 0, 255)