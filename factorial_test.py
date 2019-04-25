import pytest
import unittest
from factorial import factorial

def test_factorial_of_0(self):
    assert factorial(0) == 1
    
def test_positive_number(self):
    assert factorial(1) == 1

    assert factorial(5) == 120

    assert factorial(3) == 6

def test_negative_raises_error(self):
    with pytest.raises(AssertionError):
        factorial(-1)

def test_letters_raises_error(self):
    with pytest.raises(AssertionError):
        factorial("k")

def test_characters_raises_error(self):
    with pytest.raises(AssertionError):
        factorial("@")


if __name__ == '__main__':
    unittest.main()