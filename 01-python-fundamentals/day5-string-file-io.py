# Part 1: String manipulation

text = "  Hello, World!  "

print(text.strip())        # removes leading/trailing whitespace -> "Hello, World!"
print(text.lower())        # "  hello, world!  "
print(text.upper())        # "  HELLO, WORLD!  "
print(text.replace("World", "Python"))  # "  Hello, Python!  "

sentence = "the quick brown fox"
words = sentence.split()   # splits into a list by whitespace -> ['the', 'quick', 'brown', 'fox']
print(words)

joined = "-".join(words)   # joins list back into a string -> "the-quick-brown-fox"
print(joined)

print(len("hello"))        # 5
print("hello"[1:4])        # slicing -> "ell"

# Part 2: File I/O - reading and writing files

# Writing to a file
with open("data.txt", "w") as f:
    f.write("Hello, this is line 1\n")
    f.write("This is line 2\n")

# Reading a file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# Reading line by line
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())  # strip() removes the trailing newline

# Practice

# 1. Take a sentence and count how many words it has
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(len(words))

# 2. Take a sentence and reverse the order of the words
# "the quick brown fox" -> "fox brown quick the"
sentence2 = "the quick brown fox"
reverse_sentence = " ".join(sentence2.split()[::-1])
print(reverse_sentence)


# 3. Write a program that writes your name and 3 facts about yourself to a
#    file called "about_me.txt", then reads it back and prints it
with open("about_me.txt", "w") as f:
    f.write("I am motivated to learn\n")
    f.write("I made some mistakes in my relationship\n")
    f.write("I want to become a better person\n")

with open("about_me.txt", "r") as f:
    content = f.read()
    print(content)

# Improved version
facts = [
    "I am motivated to learn\n",
    "I made some mistakes in my relationship\n",
    "I want to become a better person\n"
]

with open("about_me2.txt", "w") as f:
    f.writelines(facts)

with open("about_me2.txt", "r") as f:
    content = f.read()
    print(content)