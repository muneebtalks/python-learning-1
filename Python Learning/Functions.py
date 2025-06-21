# A function is a block of code that only runs when it’s called.
# You can pass data (parameters) into it, and it can return data.

def greet(name):
    print("Hello", name)

greet("Muneeb")

# Function with Return:
def add(a, b):
    return a + b

result = add(3, 5)
print("Sum:", result)


# Arguments

def subtract(a, b):
    return a - b

print("Subtraction" , subtract(10, 3))  # 7


def multiply(a, b):
    return a * b
print("Multiply", multiply(10, 3))

def divide(a, b):
    return a / b
print("Division", divide(10, 3))

#Default Arguments
def greet(name="Guest"):
    print("Hello", name)

greet()             # Hello Guest
greet("Muneeb")     # Hello Muneeb


def profile(name, age):
    print(name, "is", age, "years old")

profile(age=25, name="Ali")
profile("muneeb" , 7)


# Arbitrary Arguments
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4,5,6,7,8,9,10))

# Scope: Local vs Global Variables

x = 10  # Global

def example():
    x = 5  # Local
    print("Inside:", x)
example()
print("Outside:", x)
