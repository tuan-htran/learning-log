# 1. Double every number
numbers = [1, 2, 3, 4, 5]
double = [n*2 for n in numbers]
print(double)

# 2. Filter for numbers greater than 10
numbers2 = [4, 15, 8, 23, 42, 6]
print([n for n in numbers2 if n > 10])

# 3. Get the length of each word in a list
words = ["hello", "hi", "goodbye"]
print([len(n) for n in words])

# 4. Uppercase every string in a list
names = ["tuan", "alex", "jamie"]
print([n.upper() for n in names])

# 5. Combine filter + transform
# Goal: square only the even numbers -> [4, 16, 36, 64, 100]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([n**2 for n in numbers if n % 2 == 0])