from tkinter import *
import random

# Main window
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.configure(bg="lightblue")

# Choices list
choices = ["Rock", "Paper", "Scissors"]


# Game logic
def play(user_choice):
    # Computer choice using random module
    computer_choice = choices[random.randint(0, 2)]

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text="Your Choice: "
        + user_choice
        + "\nComputer Choice: "
        + computer_choice
        + "\n\nResult: "
        + result
    )


# Heading
Label(
    root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="lightblue"
).pack(pady=20)

# Buttons
Button(root, text="Rock", width=15, command=lambda: play("Rock")).pack(pady=5)

Button(root, text="Paper", width=15, command=lambda: play("Paper")).pack(pady=5)

Button(root, text="Scissors", width=15, command=lambda: play("Scissors")).pack(pady=5)

# Result display
result_label = Label(root, text="", font=("Arial", 12), bg="lightblue")
result_label.pack(pady=20)

root.mainloop()
