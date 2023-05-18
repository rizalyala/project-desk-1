import tkinter as tk


class BannerControl(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        ban_container = tk.Frame(self, bg='#025464', height=100, width=1080)
        ban_container.grid(row=0, column=2, columnspan=4)
