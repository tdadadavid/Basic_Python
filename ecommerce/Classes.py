from collections import namedtuple

# instead of using this tideous format below
# we can use a namedtuple from the collections
# class...
# Note that namedtuple is immutable

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, o: object) :
#         return self.x == o.x and self.y == o.y


Point = namedtuple("Point", ["x", "y"])

# code is not noisy...Hurrray

point = Point(x=1, y=2)
point2 = Point(x=1, y=2)
print(point == point2)
