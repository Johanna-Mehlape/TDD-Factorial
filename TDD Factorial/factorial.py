#factorial.py
"""python code to find a Factorial of a number"""
    
def factorial(n):
    """factorial function"""
    try: #to try the input and see if it is an integer
        n = int(n) #if it is an integer, it will print out its factorial
    except:#if it is not an integer, except will return an message
        print("Only integers have factorials")
        return "Only integers have factorials"

    
    if n < 0: 
        print("False")
        return False
    elif n == 0:
        return 1
    elif n == 1:
        return 1 
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    n = input("Please enter an integer > = 0 to find its Factorial : ")
    factorial(n)
    
