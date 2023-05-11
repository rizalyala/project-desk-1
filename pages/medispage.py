import tkinter as tk

from components.tab_info import Detail_medis_table


class Medispage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.teks = tk.Label(self, text="Medis", font=("Arial", 24, "bold"))
        self.teks.pack(padx=20, pady=20)

        # TABEL STATISTIK PASIEN -----------------------------------------------------------
        table_patient = Detail_medis_table(self)
        table_patient.pack(expand=True, fill="y")
