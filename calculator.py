# https://github.com/ChaliceofInk/lab10-RR-BF.git
# Partner 1: Russell Richter
# Partner 2: Brendan Fries
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    if a < 0:
        raise ValueError("Input cannot be negative.")
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return (a + b)


def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('Cannot divide by zero.')
    return a / b

def exp(a, b):
    return a ** b



def subtract(a, b):
    return (a - b)

def logarithm(a, b):
    try:
        value = math.log(a, b)
    except ValueError:
        raise ValueError("Invalid Input! Did you use zero or negative inputs?")
    except:
        print("Unknown Error!")
    return value

