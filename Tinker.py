#testing tkinter
import tkinter as tk

window = tk.Tk()
#window.geometry("300x300")
#window.title('Todos')
#window['background'] = "#301934"
#greeting = tk.Label(text="To Dos",fg="white", bg="#301934")
#greeting.pack(pady=10)
#button = tk.Button( text='Click Me', width=25,height=5, fg='FFC0CB',bg='#FFFFFF')

label = tk.Label(text="Todos")
entry = tk.Entry()
label.pack()
entry.pack()
window.mainloop()
#
