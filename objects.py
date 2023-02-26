import game
import pygame
from pygame.math import Vector2

class Square():
    def __init__(self, position: Vector2, velocity: Vector2, size: int) -> None:
        self.position = position
        self.velocity = velocity
        self.size = size

    def draw(self):
        pygame.draw.rect(game.WIN, (255, 0, 0), (*self.position, self.size, self.size))