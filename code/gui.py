

# imports 
import tkinter as tk
import customtkinter as ctk


class Gui(): 
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WeatherGPT")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        # quit whit escape key
        self.root.bind("<Escape>", lambda x: quit())

    def surface(self):
        pass

    
    def run(self):
        self.root.mainloop()


# __________ main code __________
if __name__ == "__main__":
    app = Gui()
    app.run()