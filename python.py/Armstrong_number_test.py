Num = int(input("Enter a number"))
digits = str(Num)
power = len(digits)
armstrong_sum = 0
for d in digits:
    armstrong_sum += int(d) ** power
if armstrong_sum == Num:
    print(Num, "is an Armstrong number")
else:
    print(Num, "is not an Armstrong number")
