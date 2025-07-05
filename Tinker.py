#testing tkinter
#game code
#Clsses for Guesses
class Colour:
    def __init__(self):
        self.words = ("red", "green", "blue", "yellow", "magenta", "cyan")
        self.name = "Colour"


class City:
    def __init__(self):
        self.words = ("sydney", "paris", "instanbul", "newyork", "london")
        self.name = "City"

import random

# variables
categories = [Colour(), City()]
random_category = random.choice(categories)
ADWORD = random.choice(random_category.words)
GUESSES = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 11, 15])
guess_count = 0

import tkinter as tk

#creating game window
window = tk.Tk()
window.geometry("600x600")
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)
#title for entire window
window.title('Word game')
window['background'] = "#301934"
window.font = ("Arial", 20)
#top greeting
greeting = tk.Label(text="Wonderful Word Game ", fg="white", bg="#301934", font=("Arial", 20))
greeting.pack(pady=10)
# Game Welcome
welcome = tk.Label(text=f'''Welcome to Wonderful Word of the day, 
Today You Have {GUESSES} Guess 
Today's word is {len(ADWORD)}  letters long 
and is from the {random_category.name} Category
Guess a Word ''',fg="white", bg="#301934")
welcome.pack(pady=10)
# Entry widget
entry1 = tk.Entry(window, font=("Arial", 14))
entry1.pack(pady=10)
#entry 1


#fun feedback sayings
wrong_random = [
    "Ha! You’ll never crack this one—I’m unbeatable!",
    "Nice try, but this word is staying secret forever!",
    "Oops, wrong guess! I’m too clever for you today.",
    "Keep guessing, but victory is already mine!",
    "Nope! This word laughs at your attempts.",
    "Wrong again! I’m the undefeated word champion.",
    "So close, yet so far—better luck next time!",
    "Guess what? You’re not getting this word today!",
    "Try harder! This word is my fortress.",
    "Wrong guess! I’m winning, and you’re just guessing.",
]
won_random = [
    "Boom! You crushed it—champion status unlocked!",
    "Victory dance time! You nailed it!",
    "Winner, winner, you just scored a dinner!",
    "You did it! The word never stood a chance.",
    "Congrats! You’re officially a word wizard!",
    "High five! You beat the game like a pro.",
    "Game over for me, but a new legend is born—you!",
]
# Feedback label
feedback = tk.Label(window, text="", fg="yellow", bg="#301934", font=("Arial", 12))
feedback.pack(pady=5)

# Submit function
def submit_action(event=None):
    guess = entry1.get().strip().lower()
    if not guess:
        return  # ignore empty guesses
    check_guess()
    entry1.delete(0, tk.END)

# Submit button
submit_button = tk.Button(window, text="Submit", command=submit_action)
submit_button.pack(pady=10)

# Bind Enter key to submit_action
window.bind('<Return>', submit_action)

#checking Guess lenght and word
def check_guess():
    global guess_count
    guess = entry1.get().strip().lower()
    if len(guess) != len(ADWORD):
        feedback.config(text=f"That's not the right length! Try a {len(ADWORD)} letter word.")
        return
    guess_count += 1

    if guess == ADWORD:
        feedback.config(text=f'''{random.choice(won_random)}, 
        You guessed the word '{ADWORD}' correctly!''')
    else:
        remaining = GUESSES - guess_count
        if remaining > 0:
            feedback.config(text=f"""
            {random.choice(wrong_random)}
            Wrong guess! You have {remaining} guesses left.
            """)
        else:
            feedback.config(text=f'''Game Over", Sorry, you've run out of guesses. The word was '{ADWORD}',''')


# Clear entry
entry1.delete(0, tk.END)

window.mainloop()
