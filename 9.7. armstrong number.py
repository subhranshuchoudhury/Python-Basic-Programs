# Armstrong Number Checking. if sum of cube of all digits are same as the original number then
# it is called armstrong number.

number = int(input("Enter Number: "))
save = number
addition: int = 0

while number > 0:
    addition += (number % 10) * (number % 10) * (number % 10)
    number = number // 10

if addition == save:
    print("It is a Armstrong number.")
else:
    print("It is not a Armstrong number.")


