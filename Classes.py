# Class: is the blueprint of an object
# Object: an instance of a class

from ast import Str


class Point:
    default_color = "Pink"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawning points ({self.x} , {self.y})")


point = Point(1, 2)
point.default_color = "Red"
print(point.default_color)
print(Point.default_color)
Point.draw(point)


another_point = Point(4, 5)
print("Another Point", another_point.default_color)
