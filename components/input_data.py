import datetime
import sqlite3
import tkinter as tk
from tkinter import ttk
from components.entry_ref import EntryRefDokter, EntryRefObat, EntryRefPasien, EntryRefPerawatan, EntryRefResObat
from components.querydb import AddDokter, AddObat, AddPasien, AddPerawatan, AddRekam, AddResepObat, AddStaff, DeleteD, Readata, UpdObat, UpdPerawatan, UpdRekam, UpdResepObat, UpdStaff, UpdateDok, UpdatePas
import tkinter.messagebox as messagebox


dates = datetime.datetime.now().strftime("%Y-%m-%d")

# ======================================================================================
opsi_pas = {"Sex": ["Male", "Female"],
            "Status": ["Kawin", "Belum Kawin", "Janda", "Duda"],
            "Gol. Darah": ["A", "B", "AB", "O"],
            "Pekerjaan": ["Wirausaha", "Wiraswasta", "ASN", "TNI/POLRI", "Pelajar", "Mahasiswa/i"],
            "Tanggal": dates,
            }


class InputDataPasien(tk.Frame):
    def __init__(self, parent, fieldslist, table, label):
        super().__init__(parent)

        # Window

        def input_window():
            window = tk.Toplevel()

            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text=label)
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)

                if field in opsi_pas:
                    entry_ = ttk.Combobox(
                        window, values=opsi_pas[field], width=32)

                else:
                    entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                AddPasien(fieldslist, entries)
                Readata(table, 'pasien')

                window.destroy()

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=3, sticky="e", padx=5, pady=5)


class UpdatePasien(tk.Frame):
    def __init__(self, parent, fieldslist, table):
        super().__init__(parent)

        # Window
        def input_window():
            selected_item = table.selection()[0]
            values = table.item(selected_item)["values"]

            window = tk.Toplevel()
            window.title("Tambah Data Pasien")
            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text="Input Pasien")
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist, start=1):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)

                if field in opsi_pas:
                    entry_ = ttk.Combobox(
                        window, values=opsi_pas[field], width=32)

                else:
                    entry_ = tk.Entry(window, width=35)
                entry_.insert(0, values[i])
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                UpdatePas(fieldslist, entries, table)
                Readata(table, 'pasien')

            submit_ = tk.Button(
                window, text="Update", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=11, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Edit", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=4, sticky="e", padx=5, pady=5)
# ======================================================================================


opsi_doc = {
    "Spesialis": ["Umum", "Bedah", "Internal", "Anestesi", "Radiologi", "Kandungan", "Anak", "Orthopedi", "Psikiatri"],
}


class InputDataDokter(tk.Frame):
    def __init__(self, parent, fieldslist, table, label):
        super().__init__(parent)

        # Window

        def input_window():
            window = tk.Toplevel()

            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text=label)
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)

                if field in opsi_doc:
                    entry_ = ttk.Combobox(
                        window, values=opsi_doc[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                AddDokter(fieldslist, entries)
                Readata(table, 'dokter')

                window.destroy()

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=3, sticky="e", padx=5, pady=5)


class UpdateDokter(tk.Frame):
    def __init__(self, parent, fieldslist, table):
        super().__init__(parent)

        # Window
        def input_window():
            selected_item = table.selection()[0]
            values = table.item(selected_item)["values"]

            window = tk.Toplevel()
            window.title("Tambah Data Dokter")
            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text="Input Dokter")
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist, start=1):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)
                if field in opsi_doc:
                    entry_ = ttk.Combobox(
                        window, values=opsi_doc[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entry_.insert(0, values[i])

                entries[field] = entry_

            def submiting_data():
                UpdateDok(fieldslist, entries, table)
                Readata(table, 'dokter')

            submit_ = tk.Button(
                window, text="Update", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Edit", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=4, sticky="e", padx=5, pady=5)
# =======================================================================================


opsi_staff = {"Sex": ["Male", "Female"],
              "Status": ["Kawin", "Belum Kawin", "Janda", "Duda"],
              "Tanggal": dates
              }


class InputDataStaff(tk.Frame):
    def __init__(self, parent, fieldslist, table, label):
        super().__init__(parent)
        # Window

        def input_window():
            window = tk.Toplevel()

            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text=label)
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)

                if field in opsi_staff:
                    entry_ = ttk.Combobox(
                        window, values=opsi_staff[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                AddStaff(fieldslist, entries)
                Readata(table, 'staff')

                window.destroy()

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=3, sticky="e", padx=5, pady=5)


class UpdateStaff(tk.Frame):
    def __init__(self, parent, fieldslist, table):
        super().__init__(parent)

        # Window
        def input_window():
            selected_item = table.selection()[0]
            values = table.item(selected_item)["values"]

            window = tk.Toplevel()
            window.title("Tambah Data Staff")
            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text="Input Staff")
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist, start=1):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)

                if field in opsi_staff:
                    entry_ = ttk.Combobox(
                        window, values=opsi_staff[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)

                entry_.insert(0, values[i])
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                UpdStaff(fieldslist, entries, table)
                Readata(table, 'staff')

            submit_ = tk.Button(
                window, text="Update", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Edit", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=4, sticky="e", padx=5, pady=5)
# =======================================================================================


opsi_ob = {
    "Obat_1": EntryRefObat.options_ob,
    "Obat_2": EntryRefObat.options_ob,
    "Obat_3": EntryRefObat.options_ob,
    "Obat_4": EntryRefObat.options_ob,
}


class InputDataObat(tk.Frame):
    def __init__(self, parent, fieldslist, table, label):
        super().__init__(parent)

        def input_window():
            window = tk.Toplevel()

            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text=label)
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)

                if field in opsi_ob:
                    entry_ = ttk.Combobox(
                        window, values=opsi_ob[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                AddObat(fieldslist, entries)
                Readata(table, 'obat')

                window.destroy()

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=3, sticky="e", padx=5, pady=5)


class UpdateObat(tk.Frame):
    def __init__(self, parent, fieldslist, table):
        super().__init__(parent)

        # Window
        def input_window():
            selected_item = table.selection()[0]
            values = table.item(selected_item)["values"]

            window = tk.Toplevel()

            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text="Input Obat")
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist, start=1):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)

                if field in opsi_ob:
                    entry_ = ttk.Combobox(
                        window, values=opsi_ob[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)

                entry_.insert(0, values[i])
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                UpdObat(fieldslist, entries, table)
                Readata(table, 'obat')

            submit_ = tk.Button(
                window, text="Update", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Edit", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=4, sticky="e", padx=5, pady=5)
# =======================================================================================


opsi_rekam = {
    "Resep Obat": EntryRefResObat.options_res,
    "Perawatan": EntryRefPerawatan.options_per,
    "Tanggal": dates,
    "Dokter": EntryRefDokter.options_doc,
}


class InputDataRekam(tk.Frame):
    def __init__(self, parent, fieldslist, table, label):
        super().__init__(parent)

        def input_window():
            window = tk.Toplevel()

            window.geometry("1000x400")
            window.resizable(False, False)

            label_ = tk.Label(window, text=label)
            label_.grid(row=0, column=1, columnspan=2)

            def search_id(event):
                entered_id = entry_search.get()
                # Database
                conn = sqlite3.connect("hospital.db")
                cursor = conn.cursor()
                querys = "SELECT Nama_pasien FROM pasien WHERE ID_pasien=?"
                cursor.execute(querys, (entered_id,))
                result = cursor.fetchone()
                cursor.close()
                conn.close()

                if result:
                    # Jika ditemukan, isikan Entry Nama dengan data yang sesuai
                    # Menghapus teks yang ada di Entry Nama
                    entries["Nama Pasien"].delete(0, tk.END)
                    # Isi Entry Nama dengan data yang sesuai
                    entries["Nama Pasien"].insert(0, result[0])
                else:
                    # Jika tidak ditemukan, kosongkan Entry Nama
                    entries["Nama Pasien"].delete(0, tk.END)

            # Search ID
            entry_search_label = tk.Label(window, text="Search ID : ")
            entry_search_label.grid(row=1, column=0, padx=10, pady=10)
            entry_search = tk.Entry(window, width=35)
            entry_search.grid(row=1, column=1, padx=10, pady=10)
            entry_search.bind("<KeyRelease>", search_id)

            entries = {}
            for i, field in enumerate(fieldslist):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=2, sticky="w", padx=10)

                if field in opsi_rekam:
                    entry_ = ttk.Combobox(
                        window, values=opsi_rekam[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=3, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                AddRekam(fieldslist, entries)
                Readata(table, 'rekam_medis')

                window.destroy()

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=3)

        # Main
        input_button = tk.Button(
            parent, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=3, sticky="e", padx=5, pady=5)


class UpdateRekam(tk.Frame):
    def __init__(self, parent, fieldslist, table):
        super().__init__(parent)

        # Window
        def input_window():
            selected_item = table.selection()[0]
            values = table.item(selected_item)["values"]

            window = tk.Toplevel()

            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text="Input Rekam Medis")
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist, start=1):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)
                if field in opsi_rekam:
                    entry_ = ttk.Combobox(
                        window, values=opsi_rekam[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)

                entry_.insert(0, values[i])
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                UpdRekam(fieldslist, entries, table)
                Readata(table, 'rekam_medis')

            submit_ = tk.Button(
                window, text="Update", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Edit", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=4, sticky="e", padx=5, pady=5)
# =======================================================================================


opsi_perawatan = {
    "P1": ["ICU", "RI", "RJ", "GD", "Operasi", "Intensif", "Paliatif", "Khusus", "Rehab"],
    "P2": ["ICU", "RI", "RJ", "GD", "Operasi", "Intensif", "Paliatif", "Khusus", "Rehab"],
    "P3": ["ICU", "RI", "RJ", "GD", "Operasi", "Intensif", "Paliatif", "Khusus", "Rehab"],
    "Tanggal": dates,
    "Dokter": EntryRefDokter.options_doc,
    "Nama Pasien": EntryRefPasien.options_pas
}


class InputDataPerawatan(tk.Frame):
    def __init__(self, parent, fieldslist, table, label):
        super().__init__(parent)

        def input_window():
            window = tk.Toplevel()

            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text=label)
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)

                if field in opsi_perawatan:
                    entry_ = ttk.Combobox(
                        window, values=opsi_perawatan[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                AddPerawatan(fieldslist, entries)
                Readata(table, 'perawatan_medis')

                window.destroy()

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=3, sticky="e", padx=5, pady=5)


class UpdatePerawatan(tk.Frame):
    def __init__(self, parent, fieldslist, table):
        super().__init__(parent)

        # Window
        def input_window():
            selected_item = table.selection()[0]
            values = table.item(selected_item)["values"]

            window = tk.Toplevel()

            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text="Input Perawatan Medis")
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist, start=1):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)
                if field in opsi_perawatan:
                    entry_ = ttk.Combobox(
                        window, values=opsi_perawatan[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)

                entry_.insert(0, values[i])
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                UpdPerawatan(fieldslist, entries, table)
                Readata(table, 'perawatan_medis')

            submit_ = tk.Button(
                window, text="Update", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Edit", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=4, sticky="e", padx=5, pady=5)
# =======================================================================================


opsi_resep = {
    "Obat_1": EntryRefObat.options_ob,
    "Obat_2": EntryRefObat.options_ob,
    "Obat_3": EntryRefObat.options_ob,
    "Obat_4": EntryRefObat.options_ob,
    "Tanggal": dates,
    "Dokter": EntryRefDokter.options_doc,
    "Nama Pasien": EntryRefPasien.options_pas
}


class InputDataResep(tk.Frame):
    def __init__(self, parent, fieldslist, table, label):
        super().__init__(parent)

        def input_window():
            window = tk.Toplevel()

            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text=label)
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)

                if field in opsi_resep:
                    entry_ = ttk.Combobox(
                        window, values=opsi_resep[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                AddResepObat(fieldslist, entries)
                Readata(table, 'resep_obat')

                window.destroy()

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=3, sticky="e", padx=5, pady=5)


class UpdateResep(tk.Frame):
    def __init__(self, parent, fieldslist, table):
        super().__init__(parent)

        # Window
        def input_window():
            selected_item = table.selection()[0]
            values = table.item(selected_item)["values"]

            window = tk.Toplevel()

            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text="Input Resep bat")
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist, start=1):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)
                if field in opsi_resep:
                    entry_ = ttk.Combobox(
                        window, values=opsi_resep[field], width=32)
                else:
                    entry_ = tk.Entry(window, width=35)

                entry_.insert(0, values[i])
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                UpdResepObat(fieldslist, entries, table)
                Readata(table, 'resep_obat')

            submit_ = tk.Button(
                window, text="Update", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Edit", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=4, sticky="e", padx=5, pady=5)

# =======================================================================================


class DeleteData(tk.Frame):
    def __init__(self, parent, table, db):
        super().__init__()

        def deleted():
            confirm = messagebox.askyesno("Hapus", "Yakin ingin menghapus ?")
            if confirm:
                DeleteD(table, db)
                messagebox.showinfo("", "Data terhapus")

        input_button = tk.Button(
            parent, text="Delete", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=deleted)
        input_button.grid(row=0, column=5, sticky="e", padx=5, pady=5)
