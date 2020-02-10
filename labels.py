import tkinter as tk

window = tk.Tk()

colored_label = tk.Label(text="I'm colored",
                         foreground='yellow',
                         background='black')
colored_label.pack()

html_label = tk.Label(text="I'm html",
                      background="#34A2FE")
html_label.pack()

shorthands_label = tk.Label(text='short hands',
                            fg='pink',
                            bg='orange')
shorthands_label.pack()

size_label = tk.Label(text='',
                      fg='white',
                      bg='black',
                      width=20,
                      height=15)
size_label.pack()

window.mainloop()
