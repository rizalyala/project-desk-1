import tkinter as tk

from components.tab_info import Detailed_staff_table


class StafPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.teks = tk.Label(self, text="Pegawai", font=("Arial", 24, "bold"))
        self.teks.pack(padx=20, pady=20,
                       )

        # TABEL STATISTIK PASIEN -----------------------------------------------------------
        table_staff = Detailed_staff_table(self)
        table_staff.pack(expand=True, fill="y")
