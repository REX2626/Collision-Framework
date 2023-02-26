import objects as _objects
import pygame

WIDTH = 1200
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

objects: set["_objects.Square"] = set()