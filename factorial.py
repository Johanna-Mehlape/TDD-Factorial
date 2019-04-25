#factorial.py
"""python code to find a Factorial of a number"""
import pytest
import unittest
    
def factorial(n):
    """factorial function"""
        
    n = int(n)
    
    if n < 0: 
        raise ValueError, "There is no factorial for a negative number"
    if int(n) <> n:
        raise ValueError, "Only integers have factorials"
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Please enter an integer > = 0 to find its Factorial : "))
factorial = factorial(n)
print("The Factorial of %d = %d" %(n, factorial))