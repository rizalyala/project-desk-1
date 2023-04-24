import tkinter as tk


class Sidebar:
    def __init__(self, master, mainf, bg='green'):
        self.master = master
        self.mainf = mainf
        self.bg = bg
        self.create_menu()

    def create_menu(self):
        self.menu_frame = tk.Frame(
            self.master, bg=self.bg, width=200, height=600, padx=20)
        self.menu_frame.pack(side='left', fill='y')

        self.home_button = tk.Button(self.menu_frame, text='Home', font=(
            'Arial', 14), command=lambda: self.on_menu_click('home'), borderwidth=0, relief='groove')
        self.home_button.pack(pady=10)

        self.about_button = tk.Button(self.menu_frame, text='About', font=(
            'Arial', 14), command=lambda: self.on_menu_click('about'))
        self.about_button.pack(pady=10)

    def on_menu_click(self, menu_name):
        if menu_name == 'home':
            self.mainf.config(bg='white')
        elif menu_name == 'about':
            self.mainf.config(bg='blue')
