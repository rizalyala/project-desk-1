import tkinter as tk

from components.tab_info import Detail_lab_table


class LabPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.teks = tk.Label(self, text="Laboratorium",
                             font=("Arial", 24, "bold"))
        self.teks.pack(padx=20, pady=20,
                       )

        # TABEL STATISTIK PASIEN -----------------------------------------------------------
        table_lab = Detail_lab_table(self)
        table_lab.pack(expand=True, fill="y")
