#Here I am starting with python basics


#Printing Output
print("Hello, World!")

#Variables and Data Types
name = "Muneeb"      # string
age = 25             # integer
height = 5.9         # float
is_student = True    # bool

#Input from User
name = input("Enter your name: ")
print("Hi", name)

#Type Conversion
a = int("5")
b = float("3.14")

#Basic Operators
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a % b)   # Modulo (remainder)
print(a // b)  # Floor Division
print(a ** b)  # Exponent

#String Operations
msg = "Hello"
print(msg.upper())
print(msg.lower())
print(len(msg))
print(msg[0])
print(msg[-1])

#Conditional Statements
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")

#Type Checking
x = 10
print(type(x))

#Functions
def greet(name):
    print("Hello", name)

greet("Muneeb")

#Dictionaries
person = {"name": "Muneeb", "age": 25}
print(person["name"])

#Importing Modules
import math
print(math.sqrt(25))   # 5.0

#File I/O (Basics)
# Writing to file
with open("demo.txt", "w") as f:
    f.write("Hello World")

# Reading from file
with open("demo.txt", "r") as f:
    content = f.read()
    print(content)

#Exception Handling
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero.")


