from vector import Vector
from objects import Square
import game



def multiple_at_once():
    game.objects.add(Square(Vector(200, 300), Vector(50, 0), size=50))
    game.objects.add(Square(Vector(500, 300), Vector(-50, 0), size=50))

    game.objects.add(Square(Vector(200, 500), Vector(50, 0), size=50))
    game.objects.add(Square(Vector(500, 500), Vector(-50, 0), size=50))

def three_joined():
    game.objects.add(Square(Vector(200, 300), Vector(50, 0), size=50))
    game.objects.add(Square(Vector(500, 300), Vector(0, 0), size=50))
    game.objects.add(Square(Vector(800, 300), Vector(-50, 0), size=50))

def four_joined():
    game.objects.add(Square(Vector(200, 300), Vector(50, 0), size=50))
    game.objects.add(Square(Vector(350, 300), Vector(25, 0), size=50))
    game.objects.add(Square(Vector(600, 300), Vector(-25, 0), size=50))
    game.objects.add(Square(Vector(750, 300), Vector(-50, 0), size=50))

def five_joined():
    game.objects.add(Square(Vector(200, 300), Vector(50, 0), size=50))
    game.objects.add(Square(Vector(350, 300), Vector(25, 0), size=50))
    game.objects.add(Square(Vector(500, 300), Vector(0, 0), size=50))
    game.objects.add(Square(Vector(650, 300), Vector(-25, 0), size=50))
    game.objects.add(Square(Vector(800, 300), Vector(-50, 0), size=50))

def eleven_joined():
    game.objects.add(Square(Vector(0, 300), Vector(65, 0), size=50))
    game.objects.add(Square(Vector(125, 300), Vector(50, 0), size=50))
    game.objects.add(Square(Vector(250, 300), Vector(35, 0), size=50))
    game.objects.add(Square(Vector(375, 300), Vector(20, 0), size=50))
    game.objects.add(Square(Vector(500, 300), Vector(5, 0), size=50))

    game.objects.add(Square(Vector(575, 300), Vector(0, 0), size=50))

    game.objects.add(Square(Vector(1150, 300), Vector(-65, 0), size=50))
    game.objects.add(Square(Vector(1025, 300), Vector(-50, 0), size=50))
    game.objects.add(Square(Vector(900, 300), Vector(-35, 0), size=50))
    game.objects.add(Square(Vector(775, 300), Vector(-20, 0), size=50))
    game.objects.add(Square(Vector(650, 300), Vector(-5, 0), size=50))