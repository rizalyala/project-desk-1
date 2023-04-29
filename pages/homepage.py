import tkinter as tk
from tkinter import ttk

from components.tab_info import TabInfoPanel


class Homepage(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # ROW 1
        pasien_table_frame = ttk.LabelFrame(self, text="Pasien")
        pasien_table_frame.grid(row=1, column=1, padx=10, pady=10)

        table = ttk.Treeview(pasien_table_frame, columns=(
            "col1", "col2", "col3", "col4", "col5"))
        table.column("#0", width=50)
        table.column("col1", width=200)
        table.column("col2", width=70)
        table.column("col3", width=150)
        table.column("col4", width=100)
        table.column("col5", width=50)
        table.heading("#0", text="No.")
        table.heading("col1", text="Nama")
        table.heading("col2", text="Ruangan")
        table.heading("col3", text="Gejala")
        table.heading("col4", text="Tanggal")
        table.heading("col5", text="Umur")
        table.pack(padx=5, pady=5)

        table.insert("", "end", text="1", values=(
            "Data 1", "Data 2", "Data 3"))
        table.insert("", "end", text="2", values=(
            "Data 4", "Data 5", "Data 6"))
        table.insert("", "end", text="3", values=(
            "Data 7", "Data 8", "Data 9"))

        information_frame = ttk.LabelFrame(
            self, text='Panel')
        information_frame.grid(row=1, column=2, padx=10, pady=10)

        info_menu = tk.Frame(information_frame, padx=10, pady=10, height=50, )
        label_doc = tk.Label(info_menu, text="Dokter :")
        label_pasien = tk.Label(info_menu, text="Pasien/Ruangan :")

        label_doc.pack()
        label_pasien.pack()
        info_menu.pack()

        # ROW 2
        related_pasien_table_frame = ttk.LabelFrame(
            self, text="Pasien terbaru")
        related_pasien_table_frame.grid(row=2, column=1, padx=10, pady=10)

        table = ttk.Treeview(related_pasien_table_frame, columns=(
            "col1", "col2", "col3", "col4", "col5"))
        table.column("#0", width=50)
        table.column("col1", width=200)
        table.column("col2", width=70)
        table.column("col3", width=150)
        table.column("col4", width=100)
        table.column("col5", width=50)
        table.heading("#0", text="No.")
        table.heading("col1", text="Nama")
        table.heading("col2", text="Ruangan")
        table.heading("col3", text="Gejala")
        table.heading("col4", text="Tanggal")
        table.heading("col5", text="Umur")
        table.pack(padx=5, pady=5)

        table.insert("", "end", text="1", values=(
            "Data 1", "Data 2", "Data 3"))
        table.insert("", "end", text="2", values=(
            "Data 4", "Data 5", "Data 6"))
        table.insert("", "end", text="3", values=(
            "Data 7", "Data 8", "Data 9"))
