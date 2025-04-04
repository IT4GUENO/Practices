a = int(input("Add the first number: "))
b = int(input("Add the second number: "))

if a > b:
    print(f"{a} is greather than {b}")
    #Even or odd
    if a % 2 == 0:
        print("Is even")
    else:
        print("Is odd")

elif a < b:
    print(f"{a} is less than {b}")
    if b % 2 == 0:
        print("Is even")
    else:
        print("Is odd")
else:
    print("The numbers are equals")