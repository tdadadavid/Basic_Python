# Class: is the blueprint of an object
# Object: an instance of a class

from ast import Str


class Point:
    def draw(self):
        print("Drawn!")


point = Point()
print(type(point))
print(isinstance(point, Str))
