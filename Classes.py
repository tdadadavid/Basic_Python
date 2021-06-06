# Class: is the blueprint of an object
# Object: an instance of a class

from ast import Str


class Point:
    default_color = "Pink"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Drawning points ({self.x} , {self.y})")

    def __str__(self):
        return f"({self.x} , {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)


point = Point(1, 2)
point2 = Point(1, -2)
print(point + point2)
