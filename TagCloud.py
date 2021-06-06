class Animal:
    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Aves(Animal):
    def fly(self):
        print("fly")


m = Mammal()
a = Aves()
print(m.walk())
print(a.eat())
