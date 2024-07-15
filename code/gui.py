# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import tkinter as tk
# from tkinter import ttk
# import customtkinter as ctk

# from recieve_data import get_llm_response
# from modules.speech import create_audio




import sys, os

# Fügen Sie den relativen Pfad zu dem Verzeichnis 'code' und 'all_imports' hinzu
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)

from all_imports import ctk, tk, ttk


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

        self.pages = [ctk.CTkFrame(self.main_frame) for _ in range(6)]
        self.frames = [self.frame_1, self.frame_2, self.frame_3, self.frame_4, self.frame_5, self.frame_6]
        self.count = 0

        for page, frame in zip(self.pages, self.frames):
            frame(page)

        # color theme
        style = ttk.Style(self.root)
        style.theme_use('aqua')

        # quit with escape key
        self.root.bind('<Escape>', lambda x: quit())

        self.color = {
            'd_blue':'#405D72',
            'blue':'#758694',
            'white':'#FFF8F3',
            'beige':'#F7E7DC'
        }

        self.city = 'hamburg'

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
        
        label.pack(side=pack, padx=padx, pady=pady, fill=fill)
        return label
    
    # button blueprint
    def button(self, surface, text='', height=100, width=100, text_color='#FFF8F3', bg_color='#405D72', pack='top', pady=0, padx=0, font_size=18, command=None, fill=None):
        button = ctk.CTkButton(
            master=surface,
            text=text,
            width=width,
            height=height,
            corner_radius=20,
            fg_color=bg_color,
            text_color=text_color,
            font=('Helvetica', font_size),
            command=command)
        
        button.pack(side=pack, padx=padx, pady=pady, fill=fill)
        return button

    def frame_1(self, surface):
        ...

    def frame_2(self, surface):
        ...
    
    def frame_3(self, surface):
        title = self.text_block(
            surface, 
            text='How does it work?', 
            fill='x', 
            padx=40, 
            pady=20, 
            height=70, 
            width=1000)
        
        text = self.text_block(
            surface, 
            text='Explanation', 
            fill='x', 
            padx=40, 
            pady=0, 
            height=400, 
            width=1000)
        
        apt = self.button(
            surface, 
            text='API key?', 
            pack='left', 
            padx=40, pady=10, 
            height=70, 
            width=250, 
            command=lambda: self.show_frame(3))
        
        details = self.button(
            surface, 
            text='Technical details', 
            pack='left', 
            padx=40, 
            pady=10, 
            height=70, 
            width=250, 
            command=lambda: self.show_frame(4))
        
        next = self.button(
            surface, 
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
        title = self.text_block(
            surface, 
            text="WeatherGPT", 
            fill='x', 
            padx=40, 
            pady=20, 
            height=70, 
            width=1000)
        
        placeholder = self.text_block(
            surface, 
            text='placeholder', 
            fill='x', 
            padx=40, 
            pady=0, 
            height=250, 
            width=1000)
        
        llm_text = self.text_block(
            surface, 
            text='',#get_llm_response(), 
            pack='left',
            padx=40, 
            pady=0, 
            height=200, 
            width=600)
        
        #city = self.option_menu()

    def surface(self):
        # frame_1 -> Start page
        # frame_2 -> What is WeatherGPT?
        # frame_3 -> Explanation
        # frame_4 -> API Key
        # frame_5 -> Technical details
        # frame_6 -> main frame 

        self.show_frame(5)

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
        if self.count > 0:
            self.count -= 1
            self.show_frame(self.count)

    def city(self):
        return self.city

    def run(self):
        self.surface()
        self.root.mainloop()


if __name__ == "__main__":
    app = Gui()
    app.run()