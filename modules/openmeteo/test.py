import tkinter as tk

class Gui(): 
    def init(self):
        self.root = tk.Tk()
        self.root.title("WeatherGPT")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)

        # quit whit escape key
        self.root.bind("<Escape>", lambda x: quit())

    def surface(self):
        greeting = tk.Label(text="Hello, Tkinter")
        greeting.pack()


    def run(self):
        self.surface()
        self.root.mainloop()


app = Gui()
app.run()