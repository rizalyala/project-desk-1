import sqlite3
import tkinter
import random
import string

# Add


class AddPasien():
    def __init__(self, fieldslist, entries):
        super().__init__()
        data = {}
        for field in fieldslist:
            data[field] = entries[field].get()
            entries[field].delete(0, tkinter.END)

        # membuat koneksi ke database
        conn = sqlite3.connect('pasien.db')
        c = conn.cursor()

        # membuat tabel jika belum ada
        c.execute('''CREATE TABLE IF NOT EXISTS pasien
                    (ID TEXT, Nama TEXT, Ruangan INTEGER, Gender TEXT, Usia TEXT,Dokter TEXT, Status TEXT, Diagnosis TEXT, Tanggal TEXT)''')

        sid = ''.join(random.choices(string.digits, k=6))
        num = str(random.randint(1, 10000)).zfill(6)
        id = str(sid+num)
        # menambahkan data ke tabel
        c.execute("INSERT INTO pasien VALUES (?, ?, ?, ?,?,?,?,?,?)",
                  (id, data['Nama'], data['Ruangan'], data['Gender'], data['Usia'], data['Dokter'], data['Status'], data['Diagnosis'], data['Tanggal']))
        conn.commit()

        # menutup koneksi ke database
        conn.close()

# Update


class UpdatePasien():
    def __init__(self, fieldslist, entries, table):
        super().__init__()
        data = {}
        for field in fieldslist:
            data[field] = entries[field].get()
            entries[field].delete(0, tkinter.END)

        # membuat koneksi ke database
        conn = sqlite3.connect('pasien.db')
        c = conn.cursor()

        selected_item = table.selection()[0]
        values = table.item(selected_item)["values"]
        # menambahkan data ke tabel
        c.execute("UPDATE pasien SET Nama = ?, Ruangan = ?, Gender = ?, Usia = ?, Dokter = ?, Status = ?, Diagnosis = ?, Tanggal =? WHERE id = ?",
                  (data['Nama'], data['Ruangan'], data['Gender'], data['Usia'], data['Dokter'], data['Status'], data['Diagnosis'], data['Tanggal'], values[0]))
        conn.commit()

        # menutup koneksi ke database
        conn.close()

# Delete


class DeletePasien():
    def __init__(self, table):
        super().__init__()
        # membuat koneksi ke database
        conn = sqlite3.connect('pasien.db')
        c = conn.cursor()

        selected_item = table.selection()[0]
        values = table.item(selected_item)["values"]

        c.execute("DELETE FROM pasien WHERE id=?", (values[0],))
        conn.commit()
        conn.close()
