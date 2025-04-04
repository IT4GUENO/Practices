#Square
for x in range(4):
    print("*" *4)
#Triangle
for x in range(1, 5):
    print("*" *x)
#Square border
m = 5 #The for does not take the 5
for x in range(m):
    if x == 0 or x == m-1:
        print("**********")
    else:
        print("*        *")