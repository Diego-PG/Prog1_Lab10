# https://github.com/Diego-PG/Prog1_Lab10.git
# Partner 1: Diego Penuela-Gonzalez
# Partner 2: Michael Jaccoma

import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def logarithm(a, b):
    if a == 1 or a <= 0:
        raise ValueError
    return math.log(b, a)

def exponent(a, b):
    return a ** b