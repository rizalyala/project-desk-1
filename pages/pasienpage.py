import tkinter as tk

from components.tab_info import Detailed_patient_table


class PasienPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.teks = tk.Label(self, text="PASIEN", font=("Arial", 24, "bold"))
        self.teks.pack(padx=20, pady=20,
                       )

        # TABEL STATISTIK PASIEN -----------------------------------------------------------
        table_patient = Detailed_patient_table(self)
        table_patient.pack(expand=True, fill="y")
