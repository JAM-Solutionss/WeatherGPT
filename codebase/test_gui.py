import tkinter as tk

def callback(selection):
    print(selection)

root = tk.Tk()
options = tk.StringVar()
menu = tk.OptionMenu(root, options, 'a', 'b', 'c', command=callback)
menu.pack()
options.set('a')
root.mainloop()