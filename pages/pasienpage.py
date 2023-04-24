import tkinter as tk


class PasienPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.teks = tk.Label(self, text="Ini adalah halaman pasien")
        self.teks.pack(padx=20, pady=20)
