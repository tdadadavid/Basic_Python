# class Animal:
#     def __init__(self):
#         print("Animal Constructor")
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Mammal Constructor")
#         self.weight = 2

#     def walk(self):
#         print("walk")


# class Aves(Animal):
#     def fly(self):
#         print("fly")


# m = Mammal()
# a = Aves()
# print(m.weight)
# print(m.age)


# Multiple inheritance


class Swimmer:
    def swim(self):
        print("Swim")


class Flyer:
    def swim(self):
        print("Fly")


class Duck(Swimmer, Flyer):
    pass


duck = Duck()
duck.swim()
