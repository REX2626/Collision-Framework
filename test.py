from fractions import Fraction
from pygame.math import Vector2

print(Vector2(Fraction(1), Fraction(2)) *  Fraction(0.5))

x = Vector2(Fraction(1), Fraction(2)) *  Fraction(0.5)
x.x = Fraction(x.x)

print(x)