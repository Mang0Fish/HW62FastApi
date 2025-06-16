import math


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

def power(a: int, b: int):
    return a**b

def sqrt(a: int):
    return math.sqrt(a)

def is_prime(a: int):
    if a<= 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    for i in range(3, (a ** 0.5) + 1,2):
        if a % i == 0:
            return False
    return True

def factorial(a: int):
    if a < 0:
        raise ValueError("factorial not defined for negative numbers")
    result: int = 1
    for mul in range(2, a + 1):
        result *= mul
    return result








# testing:
# check all cases
# auto keep functionality working
# make QA life more simple
# keep bug fix working