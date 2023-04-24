import tkinter as tk


class MainFrame(tk.Frame):
    def __init__(self, master, bg):
        super().__init__(master, bg=bg, width=600, height=600)
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(
            self, text='Home', font=('Arial', 20), pady=50)
        self.title_label.pack()

        self.content_label = tk.Label(
            self, text='Welcome to the Home page!', font=('Arial', 14))
        self.content_label.pack()
