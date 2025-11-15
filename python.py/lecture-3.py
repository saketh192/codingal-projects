# Activity-1
number = int(input("Enter a number"))
print("Number is :", number)
if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

    # Activity-2
weight = int(input("Enter your weight"))
height = int(input("Enter your height"))
BMI = weight / (height / 100) ** 2
print("your BMi is :", BMI)
if BMI <= 18.5:
    print("you are underweight")
elif BMI > 18.5 and BMI < 24.9:
    print("you are normal")
elif BMI >= 25 and BMI <= 29.9:
    print("you are overweight")
else:
    print("you are obesed")

    # Acitivity-3
num = int(input("Enter a number: "))

if num > 50:
    print("The number is greater than 50")

    if num % 2 == 0:
        print("It is even")
    else:
        print("It is odd")

else:
    print("The number is not greater than 50")

    # Activity-4
import datetime

current_datetime = datetime.datetime.now()
print("The current_time is :", current_datetime)
