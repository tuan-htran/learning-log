# Part 1: Functions
def greet(name):
    print(f"Hello, {name}!")

greet("Tuan")
greet("Alex")

def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Tuan")           # Hello, Tuan!
greet("Tuan", "Hey")    # Hey, Tuan!

# Part 2: Scope
def my_function():
    x = 10  # local variable - only exists inside this function
    print(x)

my_function()
# print(x)    # ERROR - x doesn't exist out here

# Part 3: Error Handling (try/except)
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("That's not a valid number")
except ZeroDivisionError:
    print("You can't divide by zero.")

# Practice exercises
print("Practice Exercises:")
# 1. Write a function that takes a list of numbers and returns their average
def average(numbers):
    # your code here
    return sum(numbers)/len(numbers)

print(average([10, 20, 30]))  # should print 20.0


# 2. Write a function that checks if a number is prime, returns True/False
# Prime number is a number that has 2 divisor: 1 and itself
def is_prime(n):
    # your code here
    if n <= 1:
        return False
    if n <= 3:
        return True     # 2 and 3 are prime
    if n % 2 == 0:
        return False     # Eliminate even numbers (a prime)
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(8))   # False

# 3. Wrap this in a try/except so it doesn't crash on bad input
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("That's not a valid number")