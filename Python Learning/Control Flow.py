#Conditional Statements (if, elif, else)

age = 20

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")


'''
 Operator  | Meaning        Example 
| -------- | ---------------- | -------- |
| `==`     | Equal to         | `x == y` |
| `!=`     | Not equal to     | `x != y` |
| `>`      | Greater than     | `x > y`  |
| `<`      | Less than        | `x < y`  |
| `>=`     | Greater or equal | `x >= y` |
| `<=`     | Less or equal    | `x <= y` |
'''

'''| Operator | Description                  | Example            |
| -------- | ---------------------------- | ------------------ |
| `and`    | True if both conditions true | `x > 5 and x < 10` |
| `or`     | True if any condition true   | `x < 5 or x > 10`  |
| `not`    | Inverts the condition        | `not (x > 5)`      |'''


#while Loop
x = 0
while x < 5:
    print(x)
    x += 1

#for Loop
for i in range(5):     # 0 to 4
    print(i)

#Range
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(1, 10, 2) # 1, 3, 5, 7, 9

#Loop Control Statements
# break
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0, 1, 2

# continue
for i in range(5):
    if i == 3:
        continue
    print(i)  # Output: 0, 1, 2, 4


#Match Case
day = "Monday"

match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("Weekend coming")
    case _:
        print("Midweek day")

#Looping Through Strings and Lists
name = "Muneeb"
for letter in name:
    print(letter)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

Using enumerate() in a Loop
Access both index and value in a loop:
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
