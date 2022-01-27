# string formatting

name, age = input("Enter Name & Age: ").split()

print("Your name is {}.\nYour age is {}.".format(name, age))

# python version 3.6+
# another method.

print(f"Another method:\nYour name is {name}.\nYour age is {age}.")

# string formatting number input and show the avg in output

num1,num2,num3 = input("Enter Number with comma separated: ").split(",")

print((int(num1)+int(num2)+int(num3))/3)

