# Practice: Number Guessing Game
#
# 1. Set a secret number (hardcode it, e.g. secret = 7)
# 2. Ask the user to guess a number
# 3. Tell them if their guess is too high, too low, or correct
# 4. Keep looping until they guess correctly
# 5. Once correct, print how many guesses it took
#
# Hints:
# - Use a while loop that runs until the guess matches the secret number
# - Use a counter variable to track number of attempts
# - input() always returns a string - convert it to a number with int()


# First Attempt: 
secret = 7
attempts = 1
guess = int(input("Guess a number: "))

while guess != secret:
    if guess < secret:
        attempts += 1
        guess = int(input(f"{guess} is too low, guess again: "))
    elif guess > secret:
        attempts += 1
        guess = int(input(f"{guess} is too high, guess again: "))
print(f"correct. Attempts: {attempts}")