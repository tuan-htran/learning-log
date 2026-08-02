age = 25

if age < 13:
    print("You're a kid")
elif age < 20:
    print("You're a teenager")
else:
    print("You're an adult")

temperature = 75
is_sunny = True 

if temperature > 70 and is_sunny:
    print("Great day for a walk")

# Loop through a range of numbers
for i in range(5):
    print(i)

# prints 0, 1, 2, 3, 4, 

# Loop through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
 
count = 0
while count < 5:
    print(count)
    count += 1  # same as: count = count + 1

# 1. FizzBuzz (classic beginner exercise)
# Print numbers 1-20. For multiples of 3, print "Fizz"
# For mutiples of 5, print "Buzz". For mutiples of both, print "FizzBuzz".
for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 2. Sum of numbers using a while loop
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Sum of 1-10: {total}")

# Practice
# 1. Write a loop that prints only even numbers from 1 to 20
for i in range (1,21):
    if i % 2 == 0:
        print(i)

# 2. Write an if/else that checks if a number is positive, negative, or zero
num = 0
if num == 0:
    print(f"{num} is zero")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is positive")
