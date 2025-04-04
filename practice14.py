number = 100000000

while True:
    flag = False
    for x in range(2, int(number/2)):
        if(number % x == 0):
            flag = True
            break #Breaks the first cycle

    if(flag == False):
        print(f"{number}")

    number = number + 1
