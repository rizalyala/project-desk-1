import tkinter as tk

from components.tab_info import Detailed_doctor_table


class DokterPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.teks = tk.Label(self, text="DOKTER", font=("Arial", 24, "bold"))
        self.teks.pack(padx=20, pady=20,
                       )

        # TABEL STATISTIK PASIEN -----------------------------------------------------------
        table_doctor = Detailed_doctor_table(self)
        table_doctor.pack(expand=True, fill="y")
