from factorial import factorial
import pytest

def test_factorial_of_0():
        result = factorial(0)
        assert result == 1
    
def test_positive_number():
        result = factorial(1)
        assert result == 1
        
        result = factorial(5)
        assert result == 120
        
        result = factorial(3)
        assert result == 6

def test_negative_raises_error():
        result = factorial(-3)
        assert result == False

def test_letters_raises_error():
        result = factorial("o")
        assert result == 'Only integers have factorials'

def test_characters_raises_error():
        result = factorial("@")
        assert result == 'Only integers have factorials'

