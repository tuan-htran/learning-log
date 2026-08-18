# Week 2, Day 5: Intro to Testing with pytest

## Setup
# pytest is a package - install it inside your virtual environment
#   source venv/bin/activate
#   pip install pytest


## Part 1: Writing your first test
# Test files are named test_*.py, test functions are named test_*
# pytest automatically finds and runs anything matching that pattern

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# assert checks "is this condition true?"
# - True -> nothing happens, test passes
# - False -> test fails immediately, pytest reports it

# Run tests:
#   pytest test_examples.py


## Part 2: What a failing test looks like
# def test_add_broken():
#     assert add(2, 2) == 5  # deliberately wrong, to see a failure
#
# pytest shows a red FAILED with exactly what it expected vs what it got.
# (Deleted after seeing it fail once - was just for demonstration)


## Part 3: Testing real functions, including edge cases

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(1) == False   # edge case
    assert is_prime(2) == True    # edge case
    assert is_prime(17) == True
    assert is_prime(15) == False


## Part 4: Practice - average()

def average(numbers):
    return sum(numbers) / len(numbers)

def test_average():
    assert average([1, 2, 3]) == 2
    assert average([-1, 2, 3]) == 4 / 3
    assert average([1, 5, 9]) == 5
    assert average([10, 10, 10]) == 10


## Part 5: Practice - remove_duplicates()
# Lesson learned: assert average([1,2,3]) alone only checks "truthy",
# not the actual value - always compare against an exact expected value
# with ==

# Lesson learned: set() doesn't preserve order, so comparing directly
# with == against a list can be a "flaky test" - sometimes passes,
# sometimes fails, depending on set ordering that isn't guaranteed

def remove_duplicates(items):
    return list(set(items))

def test_remove_duplicates():
    result = remove_duplicates([1, 2, 2, 3, 4, 5, 6, 6])
    assert set(result) == {1, 2, 3, 4, 5, 6}  # order-independent comparison


## Professional version - solves the order problem at the source
# Using dict.fromkeys() instead of set() preserves original order,
# removing the need to work around it in tests at all

def remove_duplicates_pro(items: list) -> list:
    """Return a list of unique values, preserving original order."""
    return list(dict.fromkeys(items))

def test_remove_duplicates_removes_duplicates():
    result = remove_duplicates_pro([1, 2, 2, 3, 4, 5, 6, 6])
    assert set(result) == {1, 2, 3, 4, 5, 6}

def test_remove_duplicates_preserves_order():
    result = remove_duplicates_pro([3, 1, 2, 1, 3])
    assert result == [3, 1, 2]

def test_remove_duplicates_empty_list():
    assert remove_duplicates_pro([]) == []

def test_remove_duplicates_no_duplicates():
    assert remove_duplicates_pro([1, 2, 3]) == [1, 2, 3]