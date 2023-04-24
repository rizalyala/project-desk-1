import tkinter as tk


class DokterPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.teks = tk.Label(self, text="Ini adalah halaman dokter")
        self.teks.pack(padx=20, pady=20)
