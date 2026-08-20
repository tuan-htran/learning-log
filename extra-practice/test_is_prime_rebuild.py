# test_is_prime.py
from is_prime_rebuild import is_prime

def test_small_numbers():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True

def test_even_numbers():
    assert is_prime(4) == False
    assert is_prime(100) == False

def test_odd_primes():
    assert is_prime(17) == True
    assert is_prime(29) == True

def test_odd_non_primes():
    assert is_prime(15) == False
    assert is_prime(21) == False

def test_negative_numbers():
    assert is_prime(-5) == False