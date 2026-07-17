# A class is a blueprint. An object is one thing built from it.

class Dog:
    def __init__(self, name, age):   # constructor: runs when you build a Dog
        self.name = name             # self = Java's 'this'
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")


# Build two separate dogs from the same blueprint
rex = Dog("Rex", 3)      # no 'new' keyword in Python
luna = Dog("Luna", 5)

rex.bark()               # Rex says woof!
luna.bark()              # Luna says woof!
print(rex.name, rex.age) # Rex 3
