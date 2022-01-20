a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
c = int(input("enter 3rd number: "))

if (a < b < c) or (c < b < a):
    print("middle number is: ", b)
elif (b < a < c) or (c < a < b):
    print("middle number is: ", a)
elif (a < c < b) or (b < c < a):
    print("middle number is: ", c)
else:
    print("numbers cant be equal.")
