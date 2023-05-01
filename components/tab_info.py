import tkinter as tk
from tkinter import ttk

from components.search_bar import Search_name


class TableHome(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # PATIENT ---------------------------------------------------------------------------
        pasien_table_frame = ttk.Notebook(self)
        pasien_table_frame.grid(row=1, column=1, padx=10, pady=10)

        pasien_table_tab1 = tk.Frame(pasien_table_frame, padx=10,
                                     pady=10, bg="white")
        pasien_table_tab2 = tk.Frame(pasien_table_frame, padx=10,
                                     pady=10, bg="white")
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

        # Search bar
        Search_name(
            pasien_table_tab1, tableFrame=pasien_table_tab1, tables=table1)


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
            "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))

        table1.column("#0", width=40)
        table1.column("col1", width=200)
        table1.column("col2", width=70)
        table1.column("col3", width=50)
        table1.column("col4", width=50)
        table1.column("col5", width=200)
        table1.column("col6", width=100)
        table1.column("col7", width=100)
        table1.column("col8", width=150)

        table1.heading("#0", text="No.")
        table1.heading("col1", text="Nama")
        table1.heading("col2", text="Ruangan")
        table1.heading("col3", text="Gender")
        table1.heading("col4", text="Umur")
        table1.heading("col5", text="Dokter")
        table1.heading("col6", text="Status")
        table1.heading("col7", text="Diagnosis")
        table1.heading("col8", text="Tanggal")
        table1.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        table1.insert("", "end", text="1", values=(
            "Data 1", "Data 2", "Data 3"))
        table1.insert("", "end", text="2", values=(
            "Data 4", "Data 5", "Data 6"))
        table1.insert("", "end", text="3", values=(
            "Data 7", "Data 8", "Data 9"))

        # Search bar
        Search_name(
            pasien_table_tab1, tableFrame=pasien_table_tab1, tables=table1)


class Detailed_doctor_table(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # doctor ---------------------------------------------------------------------------
        doctor_frame = ttk.Notebook(self)
        doctor_frame.grid(row=1, column=1, padx=10, pady=10)

        doctor_table_tab1 = tk.Frame(doctor_frame, padx=10,
                                     pady=10)
        doctor_table_tab2 = tk.Frame(doctor_frame, padx=10,
                                     pady=10)
        doctor_frame.add(doctor_table_tab1, text="Daftar")
        doctor_frame.add(doctor_table_tab2, text="Statistik")

        # Tabel 1
        table1 = ttk.Treeview(doctor_table_tab1, columns=(
            "col1", "col2", "col3", "col4"))

        table1.column("#0", width=40)
        table1.column("col1", width=200)
        table1.column("col2", width=70)
        table1.column("col3", width=100)
        table1.column("col4", width=50)

        table1.heading("#0", text="No.")
        table1.heading("col1", text="Nama")
        table1.heading("col2", text="Gender")
        table1.heading("col3", text="Spesialisasi")
        table1.heading("col4", text="Status")
        table1.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        table1.insert("", "end", text="1", values=(
            "Data 1", "Data 2", "Data 3"))
        table1.insert("", "end", text="2", values=(
            "Data 4", "Data 5", "Data 6"))
        table1.insert("", "end", text="3", values=(
            "Data 7", "Data 8", "Data 9"))

        # Search bar
        Search_name(
            doctor_table_tab1, tableFrame=doctor_table_tab1, tables=table1)


class Detailed_staff_table(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # doctor ---------------------------------------------------------------------------
        staff_frame = ttk.Notebook(self)
        staff_frame.grid(row=1, column=1, padx=10, pady=10)

        staff_table_tab1 = tk.Frame(staff_frame, padx=10,
                                    pady=10)
        staff_table_tab2 = tk.Frame(staff_frame, padx=10,
                                    pady=10)
        staff_table_tab3 = tk.Frame(staff_frame, padx=10,
                                    pady=10)
        staff_table_tab4 = tk.Frame(staff_frame, padx=10,
                                    pady=10)
        staff_table_tab5 = tk.Frame(staff_frame, padx=10,
                                    pady=10)
        staff_frame.add(staff_table_tab1, text="Receptionist")
        staff_frame.add(staff_table_tab2, text="Cleaning")
        staff_frame.add(staff_table_tab3, text="Electric Instalation")
        staff_frame.add(staff_table_tab4, text="Driver")
        staff_frame.add(staff_table_tab5, text="Helper")

        # Tabel 1
        table1 = ttk.Treeview(staff_table_tab1, columns=(
            "col1", "col2", "col3", "col4"))

        table1.column("#0", width=40)
        table1.column("col1", width=200)
        table1.column("col2", width=70)
        table1.column("col3", width=100)
        table1.column("col4", width=50)

        table1.heading("#0", text="No.")
        table1.heading("col1", text="Nama")
        table1.heading("col2", text="Gender")
        table1.heading("col3", text="Spesialisasi")
        table1.heading("col4", text="Status")

        table1.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        table1.insert("", "end", text="1", values=(
            "Data 1", "Data 2", "Data 3"))
        table1.insert("", "end", text="2", values=(
            "Data 4", "Data 5", "Data 6"))
        table1.insert("", "end", text="3", values=(
            "Data 7", "Data 8", "Data 9"))

        # Search bar
        Search_name(
            staff_table_tab1, tableFrame=staff_table_tab1, tables=table1)
