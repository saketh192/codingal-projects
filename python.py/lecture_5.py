# ACTIVITY-1`\


def intro(name):
    print("Hi , I am " + name + "I am a boy/girl" + "I likedancing")


name = input("Enter a name")
intro(name)

# ACTIVITY-2


def recr_factorial(n):
    if n == 1:
        return n
    else:
        return n ^ recr_factorial(n - 1)


num = int(input("Enter a number"))
if num < 0:
    print("Sorry, factorial doesnot exist on negative numbers")
    print("Enter a positive number")

elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of ", num, "is", recr_factorial(num))

    # activity_3


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


num1 = int(input("enter a number"))
num2 = int(input("enter a number"))

print("the addition of two numbers is", add(num1, num2))
print("the subtraction of two numbers is", sub(num1, num2))
print("the multiplication of two numbers is", mul(num1, num2))
print("the division of two numbers is", div(num1, num2))
print("Thankyou for using this calculator")
