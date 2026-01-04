
name = "Alice"
age = 25
height = 5.5
is_student = True


print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)


num1 = 10
num2 = 20
sum_numbers = num1 + num2
print(type(sum_numbers))

print("Sum of num1 and num2:", sum_numbers)


greeting = "Hello, " + name + "!"
print(greeting)
print(type(greeting))


fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print(type(fruits))


coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)
print(type(coordinates))


if age > 18:
    print(name, "is an adult.")
else:
    print(name, "is not an adult.")


print("Fruits using for loop:")
for fruit in fruits:
    print(fruit)


counter = 0
print("Counting using while loop:")
while counter < 5:
    print(counter)
    counter += 1


def greet_user(user_name):
    return "Hello, " + user_name + "!"


greeting_message = greet_user(name)
print(greeting_message)
