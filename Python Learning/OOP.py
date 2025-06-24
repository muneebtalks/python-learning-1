# OOP allows you to structure code using classes and objects to model real-world things.

# Create a Class
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I’m {self.name} and I’m {self.age} years old.")

# Create object
p1 = Person("Muneeb", 22)
p1.greet()


# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.show_balance()
# print(acc.__balance) ❌ Will raise error (private)
