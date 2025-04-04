def add(x, y):
    return x + y
def subtract (x, y):
    return x - y
def multiply (x, y):
    return x * y
def divide (x, y):
    return x / y

while True:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    x =add(a, b)
    print(f"The sum is: {x}")
    x =subtract(a, b)
    print(f"The Subtraction is: {x}")
    x =multiply(a, b)
    print(f"The multiplication is: {x}")
    x =divide(a, b)
    print(f"The division is: {x}")
