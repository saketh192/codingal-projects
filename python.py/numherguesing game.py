import random

number = random.randrange(1, 51)
heart = 0
while heart < 3:
    guess = int(input("Guess a number between 1 to 50"))
    if guess == number:
        print("you won !")
    if guess < number:
        print("Think higher than this")
    if guess > number:
        print("Think lower than this")

    heart += 1

    if heart == 3:
        print("Game over , You loose !")
