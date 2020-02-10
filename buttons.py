import tkinter as tk

window = tk.Tk()

button = tk.Button(text='Click me!',
                   height=10,
                   width=10,
                   fg='yellow',
                   bg='white')
button.pack()
window.mainloop()