num = 1
while num !=0:
    num = int(input("Enter a value: "))

    if num > 0:
        print(f"{num} es mayor a 0")
    elif num < 0:
        print(f"{num} es menor a 0")
    else:
        print(f"{num} es igual a 0")