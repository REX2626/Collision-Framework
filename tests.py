from vector import Vector
from objects import Square
import game



def multiple_at_once():
    game.objects.add(Square(Vector(200, 300), Vector(50, 0), size=50))
    game.objects.add(Square(Vector(500, 300), Vector(-50, 0), size=50))

    game.objects.add(Square(Vector(200, 500), Vector(50, 0), size=50))
    game.objects.add(Square(Vector(500, 500), Vector(-50, 0), size=50))

def multiple_joined():
    game.objects.add(Square(Vector(200, 300), Vector(50, 0), size=50))
    game.objects.add(Square(Vector(500, 300), Vector(0, 0), size=50))
    game.objects.add(Square(Vector(800, 300), Vector(-50, 0), size=50))