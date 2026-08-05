# Part 1: Lists
fruits = ["apple", "banana", "mango"]

print(fruits[0])            # "apple" - indexing starts at 0
print(fruits[1])            # "mango" - negative index counts from the end

fruits.append("grape")      # adds to the end
fruits.remove("banana")     # removes by value
print(len(fruits))          # number of items

for fruit in fruits:
    print(fruit)

# Part 2: Tuples
# Like lists, but immutable — once created, you can't change them. Useful for fixed data like coordinates.
point = (3, 4)
print(point[0])  # 3
# point[0] = 5   # this would ERROR - tuples can't be modified

# Part 3: Dictionaries
# Key-value pairs — like a real-world dictionary where you look up a word (key) to get a definition (value).
person = {
    "name": "Tuan",
    "age": 30,
    "city": "San Francisco"
}

print(person["name"])       # "Tuan"
person["age"] = 31          # update a value
person["job"] = "Engineer"  # add a new key

for key, value in person.items():
    print(f"{key}: {value}")

# Part 4: Sets
# Unordered collections of unique values — duplicates get dropped automatically.
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3} - duplicates removed automatically

numbers.add(4)
print(numbers)

# Sets are handy when you need to check membership quickly or eliminate duplicates from a list:
my_list = [1, 2, 2, 3, 3, 3]
unique = set(my_list)
print(unique)   # {1, 2, 3}

# Practice exercises
# 1. Given a list of numbers, return a new list with only the even numbers
def get_evens(numbers):
    # Comprehension version
    return [n for n in numbers if n % 2 == 0]
    
    # Attempts:
    # evens = []
    # for even_number in numbers:
    #     if even_number % 2 == 0:
    #         evens.append(even_number)
    # return evens

print(get_evens([1, 2, 3, 4, 5, 6]))  # should print [2, 4, 6]


# 2. Given a dictionary of student names -> grades, print each name and grade
grades = {"Alice": 90, "Bob": 85, "Charlie": 78}
for key, value in grades.items():
    print(f"{key}: {value}")


# 3. Given a list with duplicates, return a list of unique values (order doesn't matter)
def remove_duplicates(items):
    # Order matter:
    return list(dict.fromkeys(items))
    # Order does not matter:
    # return list(set(items))

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # should print something like [1, 2, 3, 4, 5]