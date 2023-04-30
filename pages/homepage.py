import tkinter as tk
from tkinter import ttk

from components.tab_info import TableHome, TableHomeRelatedPatient


class Homepage(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # TABEL STATISTIK PASIEN -----------------------------------------------------------
        table_patient_bar = TableHome(self)
        table_patient_bar.grid(row=1, column=1)

        # PASIEN TERBARU
        table_relpatient_bar = TableHomeRelatedPatient(self)
        table_relpatient_bar.grid(row=2, column=1)

        # INFORMATION PANEL-------------------------------------------------------------------
        information_frame = ttk.Notebook(
            self)
        information_frame.grid(row=1, column=2, padx=10, pady=10)

        info_tab1 = tk.Frame(information_frame, padx=10,
                             pady=10)

        information_frame.add(info_tab1, text="Information")
        label_doc = tk.Label(info_tab1, text="Dokter :")
        label_pasien = tk.Label(info_tab1, text="Pasien/Ruangan :")
        label_ambulan = tk.Label(info_tab1, text="Ambulance : ")
        label_visitor = tk.Label(info_tab1, text="Pengunjung : ")

        label_doc.grid(row=0, column=1, sticky="w")
        label_pasien.grid(row=1, column=1, sticky="w")
        label_ambulan.grid(row=2, column=1, sticky="w")
        label_visitor.grid(row=3, column=1, sticky="w")
