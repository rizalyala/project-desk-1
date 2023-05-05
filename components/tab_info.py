import tkinter as tk
from tkinter import ttk
from components.input_data import EditFormFirebase, FormInputFirebase
import pyrebase
from components.search_bar import Search_name

firebaseConfig = {
    "apiKey": "AIzaSyCDhnuglYOPe9B3N3eqBn_tvw2IOqxdQZc",
    "authDomain": "sirs-01-3adfc.firebaseapp.com",
    "databaseURL": "https://sirs-01-3adfc-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "sirs-01-3adfc",
    "storageBucket": "sirs-01-3adfc.appspot.com",
    "messagingSenderId": "1017194189692",
    "appId": "1:1017194189692:web:76b902e8d1a65a5addcaf9"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


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
        pat_columns = ["No.", "Nama", "Ruangan", "Gejala", "Tanggal", "Umur"]
        pat_widths = [50, 200, 70, 150, 100, 50]
        pat_col_num = ["#0", "col1", "col2", "col3", "col4", "col5"]
        table1 = ttk.Treeview(
            pasien_table_tab1, columns=(
                "col1", "col2", "col3", "col4", "col5"), style="my_style.Treeview")
        table1.grid(row=1, column=0, columnspan=2)
        DefaultTable(col_name=pat_columns, col_num=pat_col_num,
                     widths=pat_widths, table=table1)

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
        rel_columns = ["No.", "Nama", "Ruangan", "Gejala", "Tanggal", "Umur"]
        rel_widths = [50, 200, 70, 150, 100, 50]
        rel_col_num = ["#0", "col1", "col2", "col3", "col4", "col5"]

        related_pasien_table_frame = ttk.LabelFrame(
            self, text="Pasien terbaru")
        related_pasien_table_frame.grid(row=2, column=1, padx=10, pady=10)

        table = ttk.Treeview(related_pasien_table_frame, columns=(
            "col1", "col2", "col3", "col4", "col5"))
        table.pack(padx=5, pady=5)
        DefaultTable(col_name=rel_columns, col_num=rel_col_num,
                     widths=rel_widths, table=table)


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

        # Tabel
        pat_det_entry_list = ['Nama', 'Ruangan', 'Gender',
                              'Usia', "Dokter", "Status", 'Diagnosis', "Tanggal"]
        pat_det_columns = ["No.", "Nama", "Ruangan", "Gender",
                           "Usia", "Dokter", "Status", "Diagnosis", "Tanggal"]

        pat_det_widths = [50, 200, 70, 50, 50, 200, 100, 100, 150]
        pat_det_col_num = ["#0", "col1", "col2", "col3",
                           "col4", "col5", "col6", "col7", "col8"]
        table_pat_det = ttk.Treeview(pasien_table_tab1, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))

        DefaultTable(col_name=pat_det_columns, col_num=pat_det_col_num,
                     widths=pat_det_widths, table=table_pat_det)
        table_pat_det.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Read Data
        data = db.child("pasien_datas").get()

        index = 1
        if data.each():
            for row in data.each():
                values = (row.val()["Nama"], row.val()["Ruangan"], row.val()["Gender"],
                          row.val()["Usia"], "", "", row.val()["Diagnosis"], "")

                table_pat_det.insert('', 'end', text=str(index), values=values)
                index += 1

        else:
            # Add one row with message "No data available"
            values = ("No data available", "", "", "", "", "", "", "")
            table_pat_det.insert('', 'end', text=str(index), values=values)

        # Edit
        EditFormFirebase(pasien_table_tab1, table=table_pat_det,
                         table_tab=pasien_table_tab1, fieldsList=pat_det_entry_list)

        # Search bar
        Search_name(
            pasien_table_tab1, tableFrame=pasien_table_tab1, tables=table_pat_det)

        # Add Button
        FormInputFirebase(
            pasien_table_tab1, res=pasien_table_tab1, fieldsList=pat_det_entry_list)


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

        doc_columns = ["No.", "Nama", "Spesialis", "Status"]
        doc_widths = [50, 200, 70, 150]
        doc_col_num = ["#0", "col1", "col2", "col3"]
        table2 = ttk.Treeview(doctor_table_tab1, columns=(
            "col1", "col2", "col3"), style="my_style.Treeview")
        table2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        DefaultTable(col_name=doc_columns, col_num=doc_col_num,
                     widths=doc_widths, table=table2)

        # Search bar
        Search_name(
            doctor_table_tab1, tableFrame=doctor_table_tab1, tables=table2)

        # Search bar
        Search_name(
            doctor_table_tab1, tableFrame=doctor_table_tab1, tables=table2)


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

        staff_columns = ["No.", "Nama", "Gender", "Spesialis", "Status"]
        staff_widths = [40, 200, 70, 100, 50]
        staff_col_num = ["#0", "col1", "col2", "col3", "col4"]
        table2 = ttk.Treeview(staff_table_tab1, columns=(
            "col1", "col2", "col3", "col4"), style="my_style.Treeview")
        table2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        DefaultTable(col_name=staff_columns, col_num=staff_col_num,
                     widths=staff_widths, table=table2)

        # Search bar
        Search_name(
            staff_table_tab1, tableFrame=staff_table_tab1, tables=table2)
