import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

def add(a, b): 
    a + b

def sub(a, b):
    a - b

def mul(a, b):
    a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError('Cannot divide by zero.')
    return a / b

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError('The logarithm base must be positive and cannot be one.')
    if b <= 0:
        raise ValueError('The logarithm input must be positive.')
    return math.log(b, a)

def exp(a, b):
    return a ** b






