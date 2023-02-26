import sys
import random
from time import perf_counter
from objects import Square
import game
import pygame
from fractions import Fraction
from vector import Vector

pygame.init()

def spawn_squares(n):
    for _ in range(n):
        position = Vector(random.randint(100, game.WIDTH-100), random.randint(100, game.HEIGHT-100))
        velocity = Vector(random.randint(-100, 100), random.randint(-100, 100))
        game.objects.add(Square(position, velocity, size=50))

def move_objects(delta_time):
    for object in game.objects:
        object.position += object.velocity * delta_time

        # Check if object has hit the left of right wall
        if object.position.x < 0 or object.position.x > game.WIDTH - object.size:
            object.velocity.x *= -1

        # Check if object has hit the top or bottom wall
        if object.position.y < 0 or object.position.y > game.HEIGHT - object.size:
            object.velocity.y *= -1

def draw_objects():
    for object in game.objects:
        object.draw()

def draw_window():
    pygame.display.update()
    game.WIN.fill((0, 0, 0))

spawn_squares(2)

delta_time = 1
while True:
    time1 = perf_counter()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    move_objects(delta_time)

    draw_objects()

    draw_window()

    time2 = perf_counter()
    delta_time = Fraction(time2 - time1)