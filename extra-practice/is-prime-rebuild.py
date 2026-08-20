def is_prime(n: int) -> bool:
    if(n <= 1):         # 1 is not prime because it only has one factor (itself), 
        return False
    if(n <= 3):         # 2 and 3 is a prime.
        return True
    if(n % 2 == 0):     # Even numbers are not prime
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_user_input() -> int:
    """Prompt the user for an integer, re-asking on invalid input."""
    while True:
        try:
            value = int(input("Enter a number: "))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("That's not a valid number")

if __name__ == "__main__":
    user_input = get_user_input()
    result = "prime" if is_prime(user_input) else "not prime"
    print(f"{user_input} is {result}")