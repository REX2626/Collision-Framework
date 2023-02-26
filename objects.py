import game
import pygame
from vector import Vector

class Square():
    def __init__(self, position: Vector, velocity: Vector, size: int) -> None:
        self.position = position
        self.velocity = velocity
        self.size = size

    def draw(self):
        pygame.draw.rect(game.WIN, (255, 0, 0), (float(self.position.x), float(self.position.y), self.size, self.size))