import tkinter as tk
import sqlite3


class InputDataFromFirebase(tk.Frame):
    def __init__(self, parent, fieldslist):
        super().__init__(parent)

        # Window
        def input_window():
            window = tk.Toplevel()
            window.title("Tambah Data Pasien")
            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text="Input Pasien")
            label_.grid(row=0, column=1, columnspan=2)

            entries = {}
            for i, field in enumerate(fieldslist):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)
                entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                data = {}
                for field in fieldslist:
                    data[field] = entries[field].get()
                    entries[field].delete(0, tk.END)

                # membuat koneksi ke database
                conn = sqlite3.connect('pasien.db')
                c = conn.cursor()

                # membuat tabel jika belum ada
                c.execute('''CREATE TABLE IF NOT EXISTS pasien
                            (Nama TEXT, Ruangan INTEGER, Gender TEXT, Usia TEXT,Dokter TEXT, Status TEXT, Diagnosis TEXT, Tanggal TEXT)''')

                # menambahkan data ke tabel
                c.execute("INSERT INTO pasien VALUES (?, ?, ?, ?,?,?,?,?)",
                          (data['Nama'], data['Ruangan'], data['Gender'], data['Usia'], data['Dokter'], data['Status'], data['Diagnosis'], data['Tanggal']))
                conn.commit()

                # menutup koneksi ke database
                conn.close()

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=2, sticky="e", padx=5, pady=5)
