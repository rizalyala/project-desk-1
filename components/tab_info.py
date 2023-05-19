import tkinter as tk
from tkinter import ttk
from components.input_data import DeleteData, InputDataDokter, InputDataObat, InputDataPasien, InputDataPerawatan, InputDataRekam, InputDataResep, InputDataRuangInap, InputDataStaff, UpdateDokter, UpdateObat, UpdatePasien, UpdatePerawatan, UpdateRekam, UpdateResep, UpdateRuangInap, UpdateStaff
from components.querydb import Readata, ReadataHome
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
        pat_columns = ["No.", "ID", "Nama", "Tanggal", "Ruang"]
        pat_widths = [50, 100, 200, 100, 100]
        pat_col_num = ["#0", "col1", "col2", "col3", "col4"]
        table1 = ttk.Treeview(
            pasien_table_tab1, columns=(
                "col1", "col2", "col3", "col4"), style="my_style.Treeview")
        table1.grid(row=1, column=0, columnspan=2)

        def readata():
            ReadataHome(table1, 'pasien', 'ruang_inap')
        readata()
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
        pat_det_columns = ["No.", 'ID', "Nama Pasien", "Tanggal Lahir", "Sex",
                           "Usia", "Gol. Darah", "Status", "Pekerjaan", "Diagnosa Awal", "Tanggal"]
        pat_det_fields = ['Nama Pasien', 'Tanggal Lahir', "Sex",
                          'Usia', 'Gol. Darah', "Status", "Pekerjaan", "Diagnosa Awal",  "Tanggal"]

        pat_det_widths = [30, 60, 200, 100, 70, 40, 70, 100, 100, 150, 100]
        pat_det_col_num = ["#0", "col1", "col2", "col3",
                           "col4", "col5", "col6", "col7", "col8", "col9", "col10"]
        table_pat_det = ttk.Treeview(pasien_table_tab1, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10"), height=20)

        # Read Data

        def readata():
            Readata(table_pat_det, 'pasien')
        readata()
        DefaultTable(col_name=pat_det_columns, col_num=pat_det_col_num,
                     widths=pat_det_widths, table=table_pat_det)
        table_pat_det.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

        # Search bar
        Search_name(
            pasien_table_tab1, pasien_table_tab1, table_pat_det)

        empty_box = tk.Label(pasien_table_tab1, width=65,
                             )
        empty_box.grid(row=0, column=3, padx=5, pady=5)
        # Add Button
        InputDataPasien(
            pasien_table_tab1, pat_det_fields, table_pat_det, 'Input Pasien')

        # Update
        UpdatePasien(pasien_table_tab1, pat_det_fields, table_pat_det)

        # Delete
        DeleteData(pasien_table_tab1, table_pat_det, 'pasien')


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

        # Tabel
        doc_columns = ["No.", "ID", "Nama Dokter", "Spesialis", "Jadwal Kerja"]
        doc_fields = ["Nama Dokter", "Spesialis", "Jadwal Kerja"]
        doc_widths = [50, 100, 200, 200, 70]
        doc_col_num = ["#0", "col1", "col2", "col3", "col4"]
        table_doc = ttk.Treeview(doctor_table_tab1, columns=(
            "col1", "col2", "col3", "col4"), style="my_style.Treeview", height=20)
        table_doc.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

        # Read Data
        def readata():
            Readata(table_doc, 'dokter')
        readata()
        DefaultTable(col_name=doc_columns, col_num=doc_col_num,
                     widths=doc_widths, table=table_doc)

        empty_box = tk.Label(doctor_table_tab1, width=11,
                             )
        empty_box.grid(row=0, column=3, padx=5, pady=5)
        # Search bar
        Search_name(
            doctor_table_tab1, doctor_table_tab1, table_doc)
        # Add Button
        InputDataDokter(
            doctor_table_tab1, doc_fields, table_doc, "Input Dokter")

        # Update
        UpdateDokter(doctor_table_tab1, doc_fields, table_doc)

        # Delete
        DeleteData(doctor_table_tab1, table_doc, 'dokter')


class Detailed_staff_table(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # doctor ---------------------------------------------------------------------------
        staff_frame = ttk.Notebook(self)
        staff_frame.grid(row=1, column=1, padx=10, pady=10)

        staff_table_tab1 = tk.Frame(staff_frame, padx=10,
                                    pady=10)

        staff_frame.add(staff_table_tab1, text="Staff")

        staff_columns = ["No.", "ID", "Nama Staff", "Posisi",
                         "Alamat", "Jadwal Piket", "No telp"]
        staff_fields = ["Nama Staff", "Posisi",
                        "Alamat", "Jadwal Piket", "No telp"]
        staff_widths = [40, 100, 200, 200, 200, 100, 100]
        staff_col_num = ["#0", "col1", "col2",
                         "col3", "col4", "col5", "col6", "col7"]
        table_staff = ttk.Treeview(staff_table_tab1, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6"), style="my_style.Treeview", height=20)
        table_staff.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

        # Read Data
        def readata():
            Readata(table_staff, 'staff')
        readata()

        empty_box = tk.Label(staff_table_tab1, width=55,
                             )
        empty_box.grid(row=0, column=3, padx=5, pady=5)
        DefaultTable(staff_columns, staff_col_num,
                     table_staff, staff_widths)
        # Search bar
        Search_name(
            staff_table_tab1, staff_table_tab1, table_staff)
        # Add Button
        InputDataStaff(
            staff_table_tab1, staff_fields, table_staff, "Input Staff")

        # Update
        UpdateStaff(staff_table_tab1, staff_fields, table_staff)

        # Delete
        DeleteData(staff_table_tab1, table_staff, 'staff')


class Detail_medis_table(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        medis_frame = ttk.Notebook(self)
        medis_frame.grid(row=1, column=1, padx=10, pady=10)

        # Rekam =================================================================================
        rekam_table_tab = tk.Frame(medis_frame, padx=10,
                                   pady=10)
        medis_frame.add(rekam_table_tab, text="Rekam Medis")

        rekam_columns = ["No.", "ID", "Nama Pasien", "Dokter",
                         "Perawatan", "Diagnosa Utama", "Resep Obat", "Tgl Keluar"]
        rekam_fields = ["Nama Pasien", "Dokter",
                        "Perawatan", "Diagnosa Utama", "Resep Obat", "Tgl Keluar"]
        rekam_widths = [40, 100, 200, 200, 100, 100, 100, 200]
        rekam_col_num = ["#0", "col1", "col2",
                         "col3", "col4", "col5", "col6", "col7"]
        table_rekam = ttk.Treeview(rekam_table_tab, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7"), style="my_style.Treeview", height=20)
        table_rekam.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

        # Read Data
        def readata():
            Readata(table_rekam, 'rekam_medis')
        readata()

        empty_box = tk.Label(rekam_table_tab, width=55,
                             )
        empty_box.grid(row=0, column=3, padx=5, pady=5)
        DefaultTable(rekam_columns, rekam_col_num,
                     table_rekam, rekam_widths)
        # Search bar
        Search_name(
            rekam_table_tab, rekam_table_tab, table_rekam)
        # Add Button
        InputDataRekam(
            rekam_table_tab, rekam_fields, table_rekam, "Input Rekam Medis")

        # Update
        UpdateRekam(rekam_table_tab, rekam_fields, table_rekam)

        # Delete
        DeleteData(rekam_table_tab, table_rekam, 'rekam_medis')

        # Perawatan ============================================================================
        perawatan_table_tab = tk.Frame(medis_frame, padx=10,
                                       pady=10)
        medis_frame.add(perawatan_table_tab, text="Perawatan Medis")

        perawatan_columns = ["No.", "ID", "Nama Pasien",
                             "P1", "P2", "P3", "Diagnosa Utama"]
        perawatan_fields = ["Nama Pasien",
                            "P1", "P2", "P3", "Diagnosa Utama"]
        perawatan_widths = [40, 100, 200, 100, 100, 100, 100, 200]
        perawatan_col_num = ["#0", "col1", "col2",
                             "col3", "col4", "col5", "col6"]
        table_perawatan = ttk.Treeview(perawatan_table_tab, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6"), style="my_style.Treeview", height=20)
        table_perawatan.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

        # Read Data
        def readata():
            Readata(table_perawatan, 'perawatan_medis')
        readata()

        empty_box = tk.Label(perawatan_table_tab, width=25,
                             )
        empty_box.grid(row=0, column=3, padx=5, pady=5)
        DefaultTable(perawatan_columns, perawatan_col_num,
                     table_perawatan, perawatan_widths)
        # Search bar
        Search_name(
            perawatan_table_tab, perawatan_table_tab, table_perawatan)
        # Add Button
        InputDataPerawatan(
            perawatan_table_tab, perawatan_fields, table_perawatan, "Input Perawatan Medis")

        # Update
        UpdatePerawatan(perawatan_table_tab, perawatan_fields, table_perawatan)

        # Delete
        DeleteData(perawatan_table_tab, table_perawatan, 'perawatan_medis')

        # Ruang Inap ===============================================================================
        ruangi_table_tab = tk.Frame(medis_frame, padx=10,
                                    pady=10)
        medis_frame.add(ruangi_table_tab, text="Ruang Inap")

        ruangi_columns = ["No.", "ID", "Nama Pasien",
                          "Ruang", "Diagnosa Utama"]
        ruangi_fields = ["Nama Pasien",
                         "Ruang", "Diagnosa Utama"]
        ruangi_widths = [40, 100, 200, 100, 200]
        ruangi_col_num = ["#0", "col1", "col2",
                          "col3", "col4"]
        table_ruangi = ttk.Treeview(ruangi_table_tab, columns=(
            "col1", "col2", "col3", "col4"), style="my_style.Treeview", height=20)
        table_ruangi.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

        # Read Data
        def readata():
            Readata(table_ruangi, 'ruang_inap')
        readata()

        empty_box = tk.Label(ruangi_table_tab, width=15,
                             )
        empty_box.grid(row=0, column=3, padx=5, pady=5)
        DefaultTable(ruangi_columns, ruangi_col_num,
                     table_ruangi, ruangi_widths)
        # Search bar
        Search_name(
            ruangi_table_tab, ruangi_table_tab, table_ruangi)
        # Add Button
        InputDataRuangInap(
            ruangi_table_tab, ruangi_fields, table_ruangi, "Input Ruang Inap")

        # Update
        UpdateRuangInap(ruangi_table_tab, ruangi_fields, table_ruangi)

        # Delete
        DeleteData(ruangi_table_tab, table_ruangi, 'ruang_inap')


class Detail_lab_table(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        lab_frame = ttk.Notebook(self)
        lab_frame.grid(row=1, column=1, padx=10, pady=10)

        # OBAT==============================================================================
        obat_table_tab = tk.Frame(lab_frame, padx=10,
                                  pady=10)

        lab_frame.add(obat_table_tab, text="Obat")
        obat_columns = ["No.", "ID", "Nama Obat", "Deskripsi",
                        "Dosis", "Stok", "Tgl Kadaluarsa"]
        obat_fields = ["Nama Obat", "Deskripsi",
                       "Dosis", "Stok", "Tgl Kadaluarsa"]
        obat_widths = [40, 100, 200, 200, 200, 100, 100]
        obat_col_num = ["#0", "col1", "col2",
                        "col3", "col4", "col5", "col6"]
        table_obat = ttk.Treeview(obat_table_tab, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6"), style="my_style.Treeview", height=20)
        table_obat.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

        # Read Data
        def readata():
            Readata(table_obat, 'obat')
        readata()

        empty_box = tk.Label(obat_table_tab, width=55,
                             )
        empty_box.grid(row=0, column=3, padx=5, pady=5)
        DefaultTable(obat_columns, obat_col_num,
                     table_obat, obat_widths)
        # Search bar
        Search_name(
            obat_table_tab, obat_table_tab, table_obat)
        # Add Button
        InputDataObat(
            obat_table_tab, obat_fields, table_obat, "Input Obat")

        # Update
        UpdateObat(obat_table_tab, obat_fields, table_obat)

        # Delete
        DeleteData(obat_table_tab, table_obat, 'obat')

        # Resep Obat =======================================================================================

        resep_table_tab = tk.Frame(lab_frame, padx=10,
                                   pady=10)

        lab_frame.add(resep_table_tab, text="Resep Obat")
        resep_columns = ["No.", "ID", "Nama Pasien", "Obat_1",
                         "Obat_2", "Obat_3", "Obat_4"]
        resep_fields = ["Nama Pasien", "Obat_1",
                        "Obat_2", "Obat_3", "Obat_4"]
        resep_widths = [40, 100, 200, 200, 200, 100, 100]
        resep_col_num = ["#0", "col1", "col2",
                         "col3", "col4", "col5", "col6"]
        table_resep = ttk.Treeview(resep_table_tab, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6"), style="my_style.Treeview")
        table_resep.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

        # Read Data
        def readata():
            Readata(table_resep, 'resep_obat')
        readata()

        empty_box = tk.Label(resep_table_tab, width=55,
                             )
        empty_box.grid(row=0, column=3, padx=5, pady=5)
        DefaultTable(resep_columns, resep_col_num,
                     table_resep, resep_widths)
        # Search bar
        Search_name(
            resep_table_tab, resep_table_tab, table_resep)
        # Add Button
        InputDataResep(
            resep_table_tab, resep_fields, table_resep, "Input Resep")

        # Update
        UpdateResep(resep_table_tab, resep_fields, table_resep)

        # Delete
        DeleteData(resep_table_tab, table_resep, 'resep_obat')
