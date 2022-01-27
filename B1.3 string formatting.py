# string formatting

name, age = input("Enter Name & Age: ").split()

print("Your name is {}.\nYour age is {}.".format(name, age))

# python version 3.6+
# another method.

print(f"Another method:\nYour name is {name}.\nYour age is {age}.")

