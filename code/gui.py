# imports 
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class Gui(): 
    def __init__(self):

        # root setup
        self.root = tk.Tk()
        self.root.title('WeatherGPT')
        self.root.geometry('1000x600')
        #self.root.resizable(False, False)

        # frame setup
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill='both', expand=True)

        self.page_1 = ctk.CTkFrame(self.main_frame)
        self.page_2 = ctk.CTkFrame(self.main_frame)
        self.page_3 = ctk.CTkFrame(self.main_frame)
        self.page_4 = ctk.CTkFrame(self.main_frame)
        self.page_5 = ctk.CTkFrame(self.main_frame)
        self.page_6 = ctk.CTkFrame(self.main_frame)
        
        self.pages = [self.page_1, self.page_2, self.page_3, self.page_4, self.page_5, self.page_6]
        self.count = 0

        # color theme
        style = ttk.Style(self.root)
        style.theme_use('aqua')

        # quit with escape key
        self.root.bind('<Escape>', lambda x: quit())

        self.color = {
            'd_blue':'#405D72',
            'blue':'#758694',
            'white':'#FFF8F3',
            'beage':'#F7E7DC'
        }

    # text field blueprint 
    def text_block(self, surface, text='', height=100, width=100, text_color='#FFF8F3', bg_color='#405D72', pack='top', pady=0, padx=0, font_size=18, fill=None):
        label = ctk.CTkLabel(
            master=surface, 
            text=text,
            text_color=text_color,
            width=width, 
            height=height, 
            fg_color=bg_color, 
            font=('Helvetica', font_size),
            corner_radius=20)
        
        label.pack(
            side=pack, 
            padx=padx, 
            pady=pady,
            fill=fill)
        
        return label
    
    # button blueprint
    def button(self,surface, text='', height=100, width=100, text_color='#FFF8F3', bg_color='#405D72', pack='top', pady=0, padx=0, font_size=18, command=None, fill=None):
        button = ctk.CTkButton(
            master=surface,
            text=text,
            width=width,
            height=height,
            corner_radius=20,
            fg_color=bg_color,
            text_color=text_color,
            font=('Helvetica', font_size),
            command=command
        )

        button.pack(
            side=pack, 
            padx=padx, 
            pady=pady,
            fill=fill)
        
        return button

    def frame_1(self, surface):
        ...

    def frame_2(self, surface):
        ...
    
    def frame_3(self, surface):
        titel = self.text_block(
            surface=surface,
            text='How does it work?', 
            fill='x',
            padx=40, 
            pady=20,
            height=70,
            width=1000)
        
        text = self.text_block(
            surface=surface,
            text='Explanation', 
            fill='x', 
            padx=40, 
            pady=0, 
            height=400,
            width=1000)
        
        api = self.button(
            surface=surface,
            text='API key?', 
            pack='left',
            padx=40, 
            pady=10,
            height=70,
            width=250,
            command= lambda: self.show_frame(3))
        
        details = self.button(
            surface=surface,
            text='Technical details', 
            pack='left',
            padx=40, 
            pady=10,
            height=70,
            width=250,
            command= lambda: self.show_frame(4))
        
        next = self.button(
            surface=surface,
            text='Next', 
            pack='left',
            padx=40, 
            pady=10,
            height=70,
            width=250,
            command=self.next_frame)

    def frame_4(self, surface):
        ... 

    def frame_5(self, surface):
        ...

    def frame_6(self, surface):
        ...

    def surface(self):
        # frame_1 -> Start page
        # frame_2 -> What is WeatherGPT?
        # frame_3 -> Explanation
        # frame_4 -> API Key
        # frame_5 -> Technical details
        # frame_6 -> main frame 

        self.frame_3(self.page_1)
        self.show_frame(0)

    def show_frame(self, index):
        for i, page in enumerate(self.pages):
            if i == index:
                page.pack(fill='both', expand=True)
            else:
                page.pack_forget()

    def next_frame(self):
        if self.count < len(self.pages) - 1:
            self.count += 1
            self.show_frame(self.count)

    def previous_frame(self):
        if self.count < len(self.pages) - 1:
            self.count -= 1
            self.show_frame(self.count)

    def run(self):
        self.surface()
        self.root.mainloop()


if __name__ == "__main__":
    app = Gui()
    app.run()