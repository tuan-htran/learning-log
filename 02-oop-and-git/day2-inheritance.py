# Part 1: Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def make_sound(self):
        print("f{self.name} makes a sound")

class Dog(Animal):   # Dog inherits from Animal
    def make_sound(self):   # overriding the parent's method
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says Meow!")

dog = Dog("Rex")
dog.eat()           # inherited from Animal -> "Rex is eating"
dog.make_sound()    # overridden -> "Rex says Woof!"

cat = Cat("Whiskers")
cat.eat()           # inherrited -> "Whiskers is eating"
cat.make_sound()    # overridden -> "Whiskers says Meow!"

# Part 2: Polymorphism
animals = [Dog("Rex"), Cat("Whiskers")]

for animal in animals:
    animal.make_sound() # each one uses its own version automatically

# Part 3: Encapsulation
# This means restricting direct access to an object's internal data, 
# usually to protect it from being changed in invalid ways. 
# Python signals this with an underscore convention (it's not strictly enforced, just a strong convention):
class BankAccount:
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self._balance = balance # single underscore = "internal, please don't touch directly"
    
    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

account = BankAccount("Tuan", 100)
print(account.get_balance())    # 100 - accessed through a method, not directly

# Practice Exercises
# 1. Create a Shape base class with a method area() that returns 0
#    Create Rectangle and Circle subclasses that override area() correctly
#    (Rectangle needs width/height, Circle needs radius - pi is available via `import math`, math.pi)
print("\nPractice Exercise: ")
# First Attempt
# class Shape:  
#     def area(self):
#         return 0

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height

# import math
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius ** 2


# Improved Version:
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Base class for all shapes."""

    @abstractmethod
    def area(self) -> float:
        """Calculate and return the shape's area."""
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and Height must be positive")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2

# test it:
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.area():.2f}")