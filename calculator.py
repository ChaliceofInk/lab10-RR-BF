"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return (a + b)

def subtract(a, b):
    return (a - b)

def multiply(a, b): 
    return (a * b)

def divide(a, b): 
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return (b / a)   # raise ZeroDivisionError if a == 0 

def logarithm(a, b):
    try:
        value = math.log(a, b)
    except ValueError:
        print("Invalid Input! Did you use zero or negative inputs?")
    except:
        print("Unknown Error!")
    return value


def exponent(a, b):
    return a**b



