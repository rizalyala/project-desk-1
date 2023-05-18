import tkinter as tk
from components.banner_control import BannerControl

from components.tab_info import Detailed_patient_table


class PasienPage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.banner = BannerControl(self)
        self.banner.pack(padx=10, pady=10,
                         )

        # TABEL STATISTIK PASIEN -----------------------------------------------------------
        table_patient = Detailed_patient_table(self)
        table_patient.pack(expand=True, fill="y")
