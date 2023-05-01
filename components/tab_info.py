import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


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

        # Search bar

        def search():
            keyword = search_var.get()
            if keyword:
                found = False
                for row in table1.get_children():
                    if keyword.lower() in table1.item(row)['values'][0].lower():
                        table1.selection_set(row)
                        found = True
                    else:
                        table1.selection_remove(row)
                if not found:
                    messagebox.showinfo('Not found', 'Data not found.')
            else:
                table1.selection_clear()

        search_var = tk.StringVar()
        search_entry = ttk.Entry(
            pasien_table_tab1, textvariable=search_var)
        search_entry.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        search_button = ttk.Button(
            pasien_table_tab1, text="Cari Nama", command=search)
        search_button.grid(row=0, column=1, padx=5, pady=5, sticky="w")

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
        table1.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

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


class Detailed_patient_table(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # PATIENT ---------------------------------------------------------------------------
        patient_frame = ttk.Notebook(self)
        patient_frame.grid(row=1, column=1, padx=10, pady=10)

        pasien_table_tab1 = tk.Frame(patient_frame, padx=10,
                                     pady=10)
        pasien_table_tab2 = tk.Frame(patient_frame, padx=10,
                                     pady=10)
        patient_frame.add(pasien_table_tab1, text="Daftar")
        patient_frame.add(pasien_table_tab2, text="Statistik")

        # Tabel 1
        table1 = ttk.Treeview(pasien_table_tab1, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        table1.column("#0", width=50)
        table1.column("col1", width=200)
        table1.column("col2", width=70)
        table1.column("col3", width=150)
        table1.column("col4", width=100)
        table1.column("col5", width=50)
        table1.column("col6", width=200)
        table1.column("col7", width=70)
        table1.heading("#0", text="No.")
        table1.heading("col1", text="Nama")
        table1.heading("col2", text="Ruangan")
        table1.heading("col3", text="Gejala")
        table1.heading("col4", text="Tanggal")
        table1.heading("col5", text="Umur")
        table1.heading("col6", text="Dokter")
        table1.heading("col7", text="Status")
        table1.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        table1.insert("", "end", text="1", values=(
            "Data 1", "Data 2", "Data 3"))
        table1.insert("", "end", text="2", values=(
            "Data 4", "Data 5", "Data 6"))
        table1.insert("", "end", text="3", values=(
            "Data 7", "Data 8", "Data 9"))
