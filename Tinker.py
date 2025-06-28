#testing tkinter
#game code
#Clsses for Guesses
class Colour:
    def __init__(self):
        self.words = ("red", "green", "blue", "yellow", "magenta", "cyan")
        self.name = "Colour"
class City:
     def __init__(self):
         self.words = ("sydney", "paris", "instanbul", "newyork","london")
         self.name = "City"
import random
 # variables
categories = [Colour(), City()]
random_category = random.choice(categories)
ADWORD = random.choice(random_category.words)
GUESSES = random.choice([2,3,4,5,6,7,8,9,11,15])
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
window.font=("Arial", 20)
#top greeting
greeting = tk.Label(text="Wonderful Word Game ",fg="white", bg="#301934",font=("Arial", 20))
greeting.pack(pady=10)
# Game Welcome
welcome = tk.Label(text=f'''Welcome to Wonderful Word of the day, 
Today You Have {GUESSES} Guess 
Today's word is {len(ADWORD)}  letters long 
and is from the {random_category.name} Category
Guess a Word ''',
fg="white", bg="#301934")
welcome.pack(pady=10)
#entry 1
entry1 = tk.Entry()
entry1.pack(pady=10)

# Feedback label
feedback=tk.Label(window, text="", fg="yellow", bg="#301934", font=("Arial", 12))
feedback.pack(pady=5)

#checking Guess lenght and word
def check_guess():
    global guess_count
    guess = entry1.get().strip().lower()
    if len(guess) != len(ADWORD):
        feedback.config(text=f"That's not the right length! Try a {len(ADWORD)} letter word.")
        return
    guess_count += 1

    if guess == ADWORD:
        messagebox.showinfo("YOU WON!", f"You guessed the word '{ADWORD}' correctly!")
        window.destroy()  # Close the game window
    else:
        remaining = GUESSES - guess_count
        if remaining > 0:
            feedback.config(text=f"Wrong guess! You have {remaining} guesses left.")
        else:
            messagebox.showinfo("Game Over", f"Sorry, you've run out of guesses. The word was '{ADWORD}'.")
            window.destroy()
# Clear entry
entry1.delete(0, tk.END)
# Button to submit guess
submit_btn = tk.Button(window, text="Submit Guess", command=check_guess, font=("Arial", 14))
submit_btn.pack(pady=10)


window.mainloop()
