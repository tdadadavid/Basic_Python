# Data structures in Python

# practicing Dictionaries

points = {"x": 0, "y": 30, "z": 50}
points["p"] = 33
print(points)

if "m" in points:
    print(points["g"])


print(points.get("g"))
del points["y"]
print(points)

for key, value in points.items():
    print(key, value)
