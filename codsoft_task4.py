from tkinter import *
import random

# Scores
user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1

    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"Your Score: {user_score}    Computer Score: {computer_score}"
    )

def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_choice_label.config(text="Your Choice:")
    computer_choice_label.config(text="Computer Choice:")
    result_label.config(text="Result")
    score_label.config(text="Your Score: 0    Computer Score: 0")


# Main Window
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("700x500")
root.resizable(True, True)

# Heading
Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 20, "bold")
).pack(pady=15)

# Instructions
Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 12)
).pack()

# Buttons Frame
button_frame = Frame(root)
button_frame.pack(pady=20)

Button(
    button_frame,
    text="Rock",
    width=15,
    font=("Arial", 12),
    command=lambda: play("Rock")
).grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="Paper",
    width=15,
    font=("Arial", 12),
    command=lambda: play("Paper")
).grid(row=0, column=1, padx=10)

Button(
    button_frame,
    text="Scissors",
    width=15,
    font=("Arial", 12),
    command=lambda: play("Scissors")
).grid(row=0, column=2, padx=10)

# Choice Display
user_choice_label = Label(
    root,
    text="Your Choice:",
    font=("Arial", 14)
)
user_choice_label.pack(pady=10)

computer_choice_label = Label(
    root,
    text="Computer Choice:",
    font=("Arial", 14)
)
computer_choice_label.pack(pady=10)

# Result Display
result_label = Label(
    root,
    text="Result",
    font=("Arial", 18, "bold"),
    width=25,
    height=2,
    relief="solid"
)
result_label.pack(pady=20)

# Score Display
score_label = Label(
    root,
    text="Your Score: 0    Computer Score: 0",
    font=("Arial", 14, "bold")
)
score_label.pack(pady=10)

# Reset Button
Button(
    root,
    text="Reset Game",
    width=15,
    font=("Arial", 12),
    command=reset_game
).pack(pady=10)

# Exit Button
Button(
    root,
    text="Exit",
    width=15,
    font=("Arial", 12),
    command=root.destroy
).pack(pady=10)

root.mainloop()
