import tkinter as tk

window = tk.Tk()
entry = tk.Entry(fg='yellow', bg='blue', width=10)
entry.pack()
text = tk.Text(fg='pink', bg='blue')
text.pack()

window.mainloop()