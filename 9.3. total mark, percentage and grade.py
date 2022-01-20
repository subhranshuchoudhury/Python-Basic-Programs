#question: input 4 subject mark. calculate their total mark, percentage and grade and show these in output.
# total mark is 400 and each of 100


a = int(input("English Mark: "))
b = int(input("Science Mark: "))
c = int(input("Math Mark: "))
d = int(input("IT Maek: "))

if a <= 100 and b <= 100 and c <= 100 and d <= 100:
    totalmarkofstd: float = a + b + c + d
    percentage: float = (totalmarkofstd / 400) * 100
    print("_____________________\nTotal Mark: ", totalmarkofstd, "\nPercentage: ", percentage)
    if 45 < percentage < 50:
        print("You got C grade.")
    elif 0 < percentage < 45:
        print("result: Fail.")
    elif 50 < percentage < 80:
        print("You got B grade.")
    elif 80 < percentage <= 100:
        print("You got A grade.")
else:
    print("\n____________________\nIndividual mark cannot exceed 100.\nPlease recheck and re-enter your marks.")
