import sys, os

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from all_imports import get_llm_response, get_API_response


class Gui(): 
    def __init__(self):
        # root setup
        self.root = tk.Tk()
        self.root.title('WeatherGPT')
        self.root.geometry('1000x600')
        #self.root.resizable(False, False)

        self.city_name = 'hamburg'

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

        # print(f"Initialized city_name: {self.city_name}")
        get_API_response(self)

    # text field blueprint 
    def text_block(self, surface, text='', height=100, width=100, text_color='#FFF8F3', bg_color='#405D72', pack='top', pady=0, padx=0, font_size=18, fill=None):
        label_frame = ctk.CTkFrame(
            master=surface, 
            width=width, 
            height=height, 
            fg_color=bg_color,
            corner_radius=20)
        
        label_frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
        label_frame.pack(
            side=pack, 
            padx=padx, 
            pady=pady, 
            fill=fill)

        label = ctk.CTkLabel(
            master=label_frame, 
            text=text,
            text_color=text_color,
            width=width-20,
            height=height-20,
            font=('Helvetica', font_size),
            wraplength=width-40,
            justify='left')
        
        label.pack(padx=10, pady=10)
        
        
        def adjust_font_size(event):
            new_font_size = max(8, min(event.width // 20, 18))
            label.configure(font=('Helvetica', new_font_size))
        
        label_frame.bind('<Configure>', adjust_font_size)

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
            text='Die Wetterdaten werden über die openmeteo API abgefragt und an die LLM API von groq weitergegeben. Die Antwort des LLM wird generiert und an der entsprechenden Stelle im GUI angezeigt. Die anderen Diagramme werden über die openmeteo API abgefragt und in die GUI eingebunden. Das Sprachmodul ist mithilfe von Google Text To Speech realisiert.', 
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
            pady=0, 
            height=70, 
            width=1000)
        

        # frames for the data 
        self.data_main_frame = ctk.CTkFrame(
            self.root, 
            height=250, 
            width=920,
            corner_radius=20)
        
        self.data_main_frame.pack(side='top', expand=True)

        self.data_pages = [ctk.CTkFrame(self.data_main_frame) for _ in range(6)]
        self.data_frames = [self.data_frame_1, self.data_frame_2, self.data_frame_3, self.data_frame_4, self.data_frame_5, self.data_frame_6]
        
        for page, frame in zip(self.data_pages, self.data_frames):
            frame(page)
        
        segmented_menu = ctk.CTkSegmentedButton(
            self.data_main_frame,
            values=['Temperature', 'Temperature diagram', '2', '2 diagram', '3', '3 diagram'],
            width=920,
            height=40,
            corner_radius=20,
            command=self.segmented_button_callback)
        
        segmented_menu.set('Temperature')
        segmented_menu.pack(side='top')
        self.show_frame(0, self.data_pages)
    

        
        llm_text = self.text_block(
            surface, 
            text=get_llm_response(self), 
            pack='left',
            padx=40, 
            pady=0, 
            height=200, 
            width=600)

    def data_frame_1(self, surface):
        self.text_block(surface,'test1', pack='bottom', width=920) 
    def data_frame_2(self, surface):
        self.text_block(surface,'test2', pack='bottom', width=920)
    def data_frame_3(self, surface):
        self.text_block(surface,'test3', pack='bottom', width=920)
    def data_frame_4(self, surface):
        self.text_block(surface,'test4', pack='bottom', width=920)
    def data_frame_5(self, surface):
        self.text_block(surface,'test5', pack='bottom', width=920)
    def data_frame_6(self, surface):
        self.text_block(surface,'test6', pack='bottom', width=920)

    def surface(self):
        # frame_1 -> Start page
        # frame_2 -> What is WeatherGPT?
        # frame_3 -> Explanation
        # frame_4 -> API Key
        # frame_5 -> Technical details
        # frame_6 -> main frame 

        self.show_frame(5, self.pages)

    def show_frame(self, index, pages):
        for i, page in enumerate(pages):
            if i == index:
                page.pack(fill='both', expand=True)
            else:
                page.pack_forget()

    def next_frame(self):
        if self.count < len(self.pages) - 1:
            self.count += 1
            self.show_frame(self.count, self.pages)

    def previous_frame(self):
        if self.count > 0:
            self.count -= 1
            self.show_frame(self.count, self.pages)

    def get_city(self):
        # print(f"Retrieving city_name: {self.city_name}")
        return self.city_name

    def segmented_button_callback(self, value):
        if value == 'Temperature':
            self.show_frame(0, self.data_pages)
        elif value == 'Temperature diagram':
            self.show_frame(1, self.data_pages)
        elif value == '2':
            self.show_frame(2, self.data_pages)
        elif value == '2 diagram':
            self.show_frame(3, self.data_pages)
        elif value == '3':
            self.show_frame(4, self.data_pages)
        elif value == '3 diagram':
            self.show_frame(5, self.data_pages)

    def run(self):
        self.surface()
        #get_API_response(self)
        self.root.mainloop()


if __name__ == "__main__":
    app = Gui()
    app.run()