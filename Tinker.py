#testing tkinter
import tkinter as tk
#creating game window
window = tk.Tk()
window.geometry("300x300")
window.title('Word game')
window['background'] = "#301934"
greeting = tk.Label(text="Wonderful Word Game ",fg="white", bg="#301934")
greeting.pack(pady=10)
label = tk.Label(text="Welcome to Wonderful Word of the day, Guess a Word ",fg="white", bg="#301934")
label.pack(pady=10)
entry = tk.Entry()
entry.pack(pady=10)

GUESS = entry.get()
GUESS

#entry.delete(0, tk.END)
# think about frameing the window for second text box


#button = tk.Button( text='Click Me', width=25,height=5, fg='FFC0CB',bg='#FFFFFF')

window.mainloop()
