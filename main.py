import sys
import math
import random
from time import perf_counter
from objects import Square, Immovable
import game
from fractions import Fraction
from vector import Vector
import pygame

from tests import multiple_at_once, three_joined, four_joined, five_joined, eleven_joined

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

def spawn_walls():
    game.objects.add(Immovable(Vector(0, -game.WIDTH), Vector(0, 0), game.WIDTH)) # top
    game.objects.add(Immovable(Vector(0, game.HEIGHT), Vector(0, 0), game.WIDTH)) # bottom
    game.objects.add(Immovable(Vector(-game.HEIGHT, 0), Vector(0, 0), game.HEIGHT)) # left
    game.objects.add(Immovable(Vector(game.WIDTH, 0), Vector(0, 0), game.HEIGHT)) # right

def overlap_x(object1: Square, object2: Square, time: Fraction):
    pos1 = object1.position.x + object1.velocity.x * time
    pos2 = object2.position.x + object2.velocity.x * time
    return not(pos1 > pos2 + object2.size or pos2 > pos1 + object1.size) # Check if not overlapping, then invert that

def overlap_y(object1: Square, object2: Square, time: Fraction):
    pos1 = object1.position.y + object1.velocity.y * time
    pos2 = object2.position.y + object2.velocity.y * time
    return not(pos1 > pos2 + object2.size or pos2 > pos1 + object1.size) # Check if not overlapping, then invert that

def add_to_group(list: list[set], object1, object2):
    """If there is already a group with one of the objects in, add the objects to it"""
    group = None
    for _group in list:
        if object1 in _group or object2 in _group:
            if group is None:
                _group.add(object1)
                _group.add(object2)
                group = _group
            else:
                group.update(_group)
                list.remove(_group)

    if group is None: # If no group found: add a new group
        list.append({object1, object2})

def corners_interesect(object1: Square, object2: Square):
    """
    Rotates obj1 and obj2 so that object2 has a rotation of 0

    Then check if any of the 4 corners of obj1 intersect obj2
    """
    # Rotate obj1 and obj2
    original_obj1_rotation = object1.rotation
    original_obj2_rotation = object2.rotation

    object1.rotation -= object2.rotation
    object2.rotation -= object2.rotation

    intersecting = False

    x, y, width, height = object2.position.x, object2.position.y, object2.size, object2.size

    # Top left corner
    if object1.tl().inside(x, y, width, height):
        intersecting = True

    # Top right corner
    elif object1.tr().inside(x, y, width, height):
        intersecting = True

    # Bottom left corner
    elif object1.bl().inside(x, y, width, height):
        intersecting = True

    # Bottom right corner
    elif object1.br().inside(x, y, width, height):
        intersecting = True

    # Correct rotation of obj1 and obj2
    object1.rotation = original_obj1_rotation
    object2.rotation = original_obj2_rotation

    return intersecting

def get_coll_objs():
    shortest_time = math.inf
    coll_objs_x = []
    coll_objs_y = []
    for object1 in game.objects:
        for object2 in game.objects:
            if object1 == object2:
                continue

            rel_vel = object1.velocity - object2.velocity

            dist_x = object2.position.x - object1.position.x - object1.size if object1.position.x < object2.position.x else object2.position.x - object2.size - object1.position.x
            dist_y = object2.position.y - object1.position.y - object1.size if object1.position.y < object2.position.y else object2.position.y - object2.size - object1.position.y

            # x
            if rel_vel.x and dist_x / rel_vel.x > 0:

                if overlap_y(object1, object2, dist_x / rel_vel.x):
                    if dist_x / rel_vel.x < shortest_time:
                        shortest_time = dist_x / rel_vel.x
                        coll_objs_x = [{object1, object2}]
                        coll_objs_y = []

                    elif dist_x / rel_vel.x == shortest_time:
                        add_to_group(coll_objs_x, object1, object2)

            # y
            if rel_vel.y and dist_y / rel_vel.y > 0:

                if overlap_x(object1, object2, dist_y / rel_vel.y):
                    if dist_y / rel_vel.y < shortest_time:
                        shortest_time = dist_y / rel_vel.y
                        coll_objs_y = [{object1, object2}]
                        coll_objs_x = []

                    elif dist_y / rel_vel.y == shortest_time:
                        add_to_group(coll_objs_y, object1, object2)

    return shortest_time, coll_objs_x, coll_objs_y

def collide_objs_x(coll_objs: set[Square]):
    """Swap the velocities of the sorted objects, with the reverse sorted objects"""
    sorted_group: list[Square] = sorted(coll_objs, key=lambda object: object.position.x)
    velocities = []

    # Immovable objects
    if isinstance(sorted_group[0], Immovable):
        del sorted_group[0]
        for object in sorted_group:
            object.velocity.x *= -1

    if isinstance(sorted_group[-1], Immovable):
        del sorted_group[-1]
        for object in sorted_group:
            object.velocity.x *= -1

    current_time = perf_counter()
    for object in sorted_group:
        object.last_collision_time = current_time
        velocities.append(object.velocity.x)

    for object, velocity in zip(sorted_group, reversed(velocities)):
        object.velocity.x = velocity

    #print("x")

def collide_objs_y(coll_objs: set[Square]):
    """Swap the velocities of the sorted objects, with the reverse sorted objects"""
    sorted_group: list[Square] = sorted(coll_objs, key=lambda object: object.position.y)
    velocities = []

    # Immovable objects
    if isinstance(sorted_group[0], Immovable):
        del sorted_group[0]
        for object in sorted_group:
            object.velocity.y *= -1

    if isinstance(sorted_group[-1], Immovable):
        del sorted_group[-1]
        for object in sorted_group:
            object.velocity.y *= -1

    current_time = perf_counter()
    for object in sorted_group:
        object.last_collision_time = current_time
        velocities.append(object.velocity.y)

    for object, velocity in zip(sorted_group, reversed(velocities)):
        object.velocity.y = velocity

    #print("y")

def update_objects(delta_time):
    while True:
        shortest_time, coll_objs_x, coll_objs_y = get_coll_objs()

        if shortest_time < delta_time:

            move_objects(shortest_time)
            delta_time -= shortest_time
            [collide_objs_x(group) for group in coll_objs_x]
            [collide_objs_y(group) for group in coll_objs_y]
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

def draw_objects():
    for object in game.objects:
        object.draw()

font = pygame.font.SysFont("bahnschrift", 24)
def draw_window(delta_time):
    fps = font.render(f"FPS: {int(1/delta_time)}", True, (255, 255, 255))
    game.WIN.blit(fps, (game.WIDTH - 100, fps.get_height()/2))

    pygame.display.update()
    game.WIN.fill((0, 0, 0))

spawn_walls()
spawn_squares(10)
#multiple_at_once()
#three_joined()
#four_joined()
#five_joined()
#eleven_joined()
game.objects.add(Immovable(Vector(550, 300), Vector(0, 0), 100))

delta_time = 1
while True:
    time1 = perf_counter()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    update_objects(delta_time)

    draw_objects()

    draw_window(delta_time)

    time2 = perf_counter()
    delta_time = Fraction(time2 - time1)
