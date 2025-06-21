# A function calling itself is called recursion.
# It must have a base case to stop, otherwise it loops forever.
from operator import truediv


# Factorial Example:
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

# Fibonacci
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(9))

#Recursive Pitfall
#recursion limit
import sys
print(sys.getrecursionlimit())


# Function to check if a number is even or odd
def number(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(number(5))

# Recursive sum of natural numbers
def sum_n(n):
    # Base case: if n is 1, the sum is 1
    if n == 1:
        return 1
    # Recursive step: sum is n plus the sum of numbers up to n-1
    else:
        return n + sum_n(n - 1)
print(sum_n(9))
