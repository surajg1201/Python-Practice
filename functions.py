# Function Definition
def greet(name):
    return f"Hello, {name}!"


# Function Call
message = greet("Alice")
print(message)

# Function with Default Parameters


def multiply(a, b=2):
    return a * b


# Function Calls
result1 = multiply(5)
result2 = multiply(5, 3)

print("Result 1:", result1)
print("Result 2:", result2)
