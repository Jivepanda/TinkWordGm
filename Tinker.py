#testing tkinter
#game code
#Clsses for Guesses
import random

class Colour:
    def __init__(self):
        self.words = ("red", "green", "blue", "yellow", "magenta", "cyan")
        self.name = "Colour"
class City:
     def __init__(self):
         self.words = ("sydney", "paris", "instanbul", "newyork","london")
         self.name = "City"

 # Create category
categories = [Colour(), City()]
# Randomly select  category
random_category = random.choice(categories)
# Randomly select a word from the selected category
ADWORD = random.choice(random_category.words)
#randowm guess count
GUESSES = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])


import tkinter as tk
#creating game window
window = tk.Tk()
window.geometry("600x600")
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)
#title for entire window
window.title('Word game')
window['background'] = "#301934"
#top greeting
greeting = tk.Label(text="Wonderful Word Game ",fg="white", bg="#301934")
greeting.pack(pady=10)
# Game Welcome
welcome = tk.Label(text=f'''Welcome to Wonderful Word of the day, 
Today You Have {GUESSES} Guess 
Today's word is {len(ADWORD)}  letters long 
Guess a Word ''',
fg="white", bg="#301934")
welcome.pack(pady=10)
#entry 1
entry1 = tk.Entry()
entry1.pack(pady=10)

GUESS = entry1.get()
GUESS

#entry.delete(0, tk.END)
# think about frameing the window for second text box


#button = tk.Button( text='Click Me', width=25,height=5, fg='FFC0CB',bg='#FFFFFF')

window.mainloop()
