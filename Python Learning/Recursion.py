# A function calling itself is called recursion.
# It must have a base case to stop, otherwise it loops forever.

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
    # Recursive step: a sum is n plus the sum of numbers up to n-1
    else:
        return n + sum_n(n - 1)
print(sum_n(9))


#Lambda Functions (Anonymous Functions)
# Normal function
def square(x):
    return x * x

# Lambda function
square = lambda x: x * x
print(square(5))

#Lambda Useful with map(), filter(), and reduce()
nums = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8, 10]

# Filter even numbers
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]
