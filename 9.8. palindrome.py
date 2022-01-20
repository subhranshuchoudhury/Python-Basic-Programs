# Armstrong Number Checking. if sum of cube of all digits are same as the original number then
# it is called armstrong number.

number = int(input("Enter Number: "))
save = number
rev: int = 0

while number > 0:
    rev = (rev*10 + number % 10)
    number = number // 10

if rev == save:
    print("Yes Palindrome.")
else:
    print("Not Palindrome.")
