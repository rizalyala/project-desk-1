import tkinter as tk
from tkinter import ttk


class TableHome(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # PATIENT ---------------------------------------------------------------------------
        pasien_table_frame = ttk.Notebook(self)
        pasien_table_frame.grid(row=1, column=1, padx=10, pady=10)

        pasien_table_tab1 = tk.Frame(pasien_table_frame, padx=10,
                                     pady=10)
        pasien_table_tab2 = tk.Frame(pasien_table_frame, padx=10,
                                     pady=10)
        pasien_table_frame.add(pasien_table_tab1, text="Pasien")
        pasien_table_frame.add(pasien_table_tab2, text="Dokter")

        # Tabel 1
        table1 = ttk.Treeview(pasien_table_tab1, columns=(
            "col1", "col2", "col3", "col4", "col5"))
        table1.column("#0", width=50)
        table1.column("col1", width=200)
        table1.column("col2", width=70)
        table1.column("col3", width=150)
        table1.column("col4", width=100)
        table1.column("col5", width=50)
        table1.heading("#0", text="No.")
        table1.heading("col1", text="Nama")
        table1.heading("col2", text="Ruangan")
        table1.heading("col3", text="Gejala")
        table1.heading("col4", text="Tanggal")
        table1.heading("col5", text="Umur")
        table1.pack(padx=5, pady=5)

        table1.insert("", "end", text="1", values=(
            "Data 1", "Data 2", "Data 3"))
        table1.insert("", "end", text="2", values=(
            "Data 4", "Data 5", "Data 6"))
        table1.insert("", "end", text="3", values=(
            "Data 7", "Data 8", "Data 9"))

        # Tabel 2
        table2 = ttk.Treeview(pasien_table_tab2, columns=(
            "col1", "col2", "col3", "col4", "col5"))
        table2.column("#0", width=50)
        table2.column("col1", width=200)
        table2.column("col2", width=70)
        table2.column("col3", width=150)
        table2.column("col4", width=100)
        table2.column("col5", width=50)
        table2.heading("#0", text="No.")
        table2.heading("col1", text="Nama")
        table2.heading("col2", text="Spesialis")
        table2.heading("col3", text="Status")

        table2.pack(padx=5, pady=5)

        table2.insert("", "end", text="1", values=(
            "Data 1", "Data 2", "Data 3"))
        table2.insert("", "end", text="2", values=(
            "Data 4", "Data 5", "Data 6"))
        table2.insert("", "end", text="3", values=(
            "Data 7", "Data 8", "Data 9"))


class TableHomeRelatedPatient(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # RELATED PATIENT---------------------------------------------------------------------
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
