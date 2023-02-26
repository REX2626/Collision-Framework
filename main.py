import sys
import math
import random
from time import perf_counter
from objects import Square
import game
import pygame
from fractions import Fraction
from vector import Vector

pygame.init()

def spawn_squares(n):
    for i in range(n):
        x = True
        while x:
            position = Vector(random.randint(100, game.WIDTH-100), random.randint(100, game.HEIGHT-100))
            velocity = Vector(random.randint(-200, 200), random.randint(-200, 200))
            x = False
            for object in game.objects:
                if not(position.x > object.position.x + object.size or object.position.x > position.x + 50) and not(position.y > object.position.y + object.size or object.position.y > position.y + 50):
                    x = True
                    break
        print(i)
        game.objects.add(Square(position, velocity, size=50))

def overlap_x(object1: Square, object2: Square, time: Fraction):
    pos1 = object1.position.x + object1.velocity.x * time
    pos2 = object2.position.x + object2.velocity.x * time
    return not(pos1 > pos2 + object2.size or pos2 > pos1 + object1.size) # Check if not overlapping, then invert that

def overlap_y(object1: Square, object2: Square, time: Fraction):
    pos1 = object1.position.y + object1.velocity.y * time
    pos2 = object2.position.y + object2.velocity.y * time
    return not(pos1 > pos2 + object2.size or pos2 > pos1 + object1.size) # Check if not overlapping, then invert that

def get_coll_objs():
    shortest_time = math.inf
    coll_objs_x = None
    coll_objs_y = None
    for object1 in game.objects:
        for object2 in game.objects:
            if object1 == object2:
                continue
            
            rel_vel = object1.velocity - object2.velocity

            dist_x = object2.position.x - object1.position.x - object1.size if object1.position.x < object2.position.x else object2.position.x - object2.size - object1.position.x
            dist_y = object2.position.y - object1.position.y - object1.size if object1.position.y < object2.position.y else object2.position.y - object2.size - object1.position.y
            
            # x
            if rel_vel.x and dist_x / rel_vel.x > 0:

                if dist_x / rel_vel.x < shortest_time and overlap_y(object1, object2, dist_x / rel_vel.x):
                    shortest_time = dist_x / rel_vel.x 
                    coll_objs_x = object1, object2
                    coll_objs_y = None

            # y
            if rel_vel.y and dist_y / rel_vel.y > 0:

                if dist_y / rel_vel.y < shortest_time and overlap_x(object1, object2, dist_y / rel_vel.y):
                    shortest_time = dist_y / rel_vel.y
                    coll_objs_y = object1, object2
                    coll_objs_x = None

    return shortest_time, coll_objs_x, coll_objs_y

def collide_objs_x(coll_objs: tuple[Square, Square]):
    object1, object2 = coll_objs
    object1.colour = (0, 255, 0)
    object2.colour = (0, 255, 0)
    object1.velocity.x, object2.velocity.x = object2.velocity.x, object1.velocity.x
    #print("x")

def collide_objs_y(coll_objs: tuple[Square, Square]):
    object1, object2 = coll_objs
    object1.colour = (0, 255, 0)
    object2.colour = (0, 255, 0)
    object1.velocity.y, object2.velocity.y = object2.velocity.y, object1.velocity.y
    #print("y")

def update_objects(delta_time):
    for object in game.objects:
        object.colour = (255, 0, 0)

    while True:
        shortest_time, coll_objs_x, coll_objs_y= get_coll_objs()

        #print(float(delta_time))
        if shortest_time < delta_time:
            move_objects(shortest_time)
            #if coll_objs_x: print("positions:", coll_objs_x[0].position, coll_objs_x[1].position)
            #if coll_objs_y: print("positions:", coll_objs_y[0].position, coll_objs_y[1].position)
            delta_time -= shortest_time
            if coll_objs_x: collide_objs_x(coll_objs_x) 
            if coll_objs_y: collide_objs_y(coll_objs_y)
            """draw_objects()
            draw_window()
            x = True
            while x:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        x = False

                    if event.type == pygame.QUIT:
                        sys.exit(0)"""

        else:
            break

    move_objects(delta_time)

def move_objects(delta_time):
    for object in game.objects:
        object.position += object.velocity * delta_time

        # Check if object has hit the left of right wall
        if object.position.x < 0 or object.position.x > game.WIDTH - object.size:
            object.velocity.x *= -1
            if object.position.x < 0: object.position.x = 0
            else: object.position.x = game.WIDTH - object.size

        # Check if object has hit the top or bottom wall
        if object.position.y < 0 or object.position.y > game.HEIGHT - object.size:
            object.velocity.y *= -1
            if object.position.y < 0: object.position.y = 0
            else: object.position.y = game.HEIGHT - object.size

def draw_objects():
    for object in game.objects:
        object.draw()

def draw_window():
    pygame.display.update()
    game.WIN.fill((0, 0, 0))

spawn_squares(5)

delta_time = 1
while True:
    time1 = perf_counter()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    update_objects(delta_time)

    draw_objects()

    draw_window()

    time2 = perf_counter()
    delta_time = Fraction(time2 - time1)