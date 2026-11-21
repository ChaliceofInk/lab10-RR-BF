import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
<<<<<<< HEAD
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("Input cannot be negative!")
    except:
        print("Unknown error!")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return (a + b)
=======


def mul(a, b):
    a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('Cannot divide by zero.')
    return a / b

def exp(a, b):
    return a ** b


>>>>>>> 14942cf7e3dff46deadbcca087963bd5ae539aaa

def subtract(a, b):
    return (a - b)

def logarithm(a, b):
    try:
        value = math.log(a, b)
    except ValueError:
        print("Invalid Input! Did you use zero or negative inputs?")
    except:
        print("Unknown Error!")
    return value

