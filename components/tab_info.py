import tkinter as tk
from tkinter import ttk
from components.input_data import InputDataFromFirebase

from components.search_bar import Search_name


class DefaultTable():
    def __init__(self, col_name, col_num, table, widths):
        super().__init__()

        for i in range(len(col_name)):
            table.column(col_num[i], width=widths[i])
            table.heading(col_num[i], text=col_name[i])


class TableHome(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # STYLE
        style = ttk.Style(self)
        style.configure("my_style.Treeview.Heading",
                        background="black", foreground="grey")
        # PATIENT ---------------------------------------------------------------------------
        pasien_table_frame = ttk.Notebook(self)
        pasien_table_frame.grid(row=1, column=1, padx=10, pady=10)

        pasien_table_tab1 = tk.Frame(pasien_table_frame, padx=20,
                                     pady=20, borderwidth=0)
        pasien_table_tab2 = tk.Frame(pasien_table_frame, padx=10,
                                     pady=10)
        pasien_table_frame.add(pasien_table_tab1, text="Pasien")
        pasien_table_frame.add(pasien_table_tab2, text="Dokter")

        # Patient
        columns = ["No.", "Nama", "Ruangan", "Gejala", "Tanggal", "Umur"]
        widths = [50, 200, 70, 150, 100, 50]
        col1 = ["#0", "col1", "col2", "col3", "col4", "col5"]
        table1 = ttk.Treeview(
            pasien_table_tab1, columns=(
                "col1", "col2", "col3", "col4", "col5"), style="my_style.Treeview")
        table1.grid(row=1, column=0, columnspan=2)
        DefaultTable(col_name=columns, col_num=col1,
                     widths=widths, table=table1)

        # Doctor
        doc_columns = ["No.", "Nama", "Spesialis", "Status"]
        doc_widths = [50, 200, 70, 150]
        doc_col_num = ["#0", "col1", "col2", "col3"]
        table2 = ttk.Treeview(pasien_table_tab2, columns=(
            "col1", "col2", "col3"), style="my_style.Treeview")
        table2.pack(padx=5, pady=5)
        DefaultTable(col_name=doc_columns, col_num=doc_col_num,
                     widths=doc_widths, table=table2)

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
        table1.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Search bar
        Search_name(
            pasien_table_tab1, tableFrame=pasien_table_tab1, tables=table1)

        # Add Button
        InputDataFromFirebase(pasien_table_tab1, res=pasien_table_tab1)


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

        # Search bar
        Search_name(
            staff_table_tab1, tableFrame=staff_table_tab1, tables=table1)
