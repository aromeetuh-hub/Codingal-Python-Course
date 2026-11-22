import random
import tkinter as tk


CHOICES = ("rock", "paper", "scissors")
WINNING_CHOICES = (
    ("rock", "scissors"),
    ("paper", "rock"),
    ("scissors", "paper"),
)


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice, computer_choice) in WINNING_CHOICES:
        return "You win!"
    else:
        return "Computer wins!"


player_score = 0
computer_score = 0


def play_round(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(CHOICES)
    result = determine_winner(player_choice, computer_choice)

    player_choice_label.config(text="You chose: " + player_choice.title())
    computer_choice_label.config(
        text="Computer chose: " + computer_choice.title()
    )
    result_label.config(text=result)

    if result == "You win!":
        player_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    score_label.config(
        text="Score - You: " + str(player_score)
        + "  Computer: " + str(computer_score)
    )


def reset_score():
    global player_score, computer_score

    player_score = 0
    computer_score = 0
    player_choice_label.config(text="You chose: -")
    computer_choice_label.config(text="Computer chose: -")
    result_label.config(text="Choose rock, paper, or scissors!")
    score_label.config(text="Score - You: 0  Computer: 0")


def create_game():
    global player_choice_label, computer_choice_label
    global result_label, score_label

    window = tk.Tk()
    window.title("Rock Paper Scissors")
    window.geometry("420x390")
    window.resizable(False, False)
    window.config(bg="lightblue")

    title_label = tk.Label(
        window,
        text="Rock Paper Scissors",
        font=("Arial", 20, "bold"),
        bg="lightblue",
    )
    title_label.pack(pady=15)

    instruction_label = tk.Label(
        window,
        text="Choose your move:",
        font=("Arial", 12),
        bg="lightblue",
    )
    instruction_label.pack(pady=5)

    button_frame = tk.Frame(window, bg="lightblue")
    button_frame.pack(pady=10)

    for choice in CHOICES:
        choice_button = tk.Button(
            button_frame,
            text=choice.title(),
            width=10,
            font=("Arial", 11, "bold"),
            command=lambda selected_choice=choice: play_round(selected_choice),
        )
        choice_button.pack(side=tk.LEFT, padx=5)

    player_choice_label = tk.Label(
        window, text="You chose: -", font=("Arial", 12), bg="lightblue"
    )
    player_choice_label.pack(pady=5)

    computer_choice_label = tk.Label(
        window, text="Computer chose: -", font=("Arial", 12), bg="lightblue"
    )
    computer_choice_label.pack(pady=5)

    result_label = tk.Label(
        window,
        text="Choose rock, paper, or scissors!",
        font=("Arial", 14, "bold"),
        bg="lightblue",
    )
    result_label.pack(pady=10)

    score_label = tk.Label(
        window, text="Score - You: 0  Computer: 0", font=("Arial", 12), bg="lightblue"
    )
    score_label.pack(pady=5)

    reset_button = tk.Button(
        window,
        text="Reset Score",
        font=("Arial", 11),
        command=reset_score,
    )
    reset_button.pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    create_game()