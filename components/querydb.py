import sqlite3
import tkinter
import random
import string


# Pasien
class AddPasien():
    def __init__(self, fieldslist, entries):
        super().__init__()
        data = {}
        for field in fieldslist:
            data[field] = entries[field].get()
            entries[field].delete(0, tkinter.END)

        # membuat koneksi ke database
        conn = sqlite3.connect('hospital.db')
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
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()

        selected_item = table.selection()[0]
        values = table.item(selected_item)["values"]
        # menambahkan data ke tabel
        c.execute("UPDATE pasien SET Nama = ?, Ruangan = ?, Gender = ?, Usia = ?, Dokter = ?, Status = ?, Diagnosis = ?, Tanggal =? WHERE id = ?",
                  (data['Nama'], data['Ruangan'], data['Gender'], data['Usia'], data['Dokter'], data['Status'], data['Diagnosis'], data['Tanggal'], values[0]))
        conn.commit()

        # menutup koneksi ke database
        conn.close()
# =======================================================================================
# Dokter


class AddDokter():
    def __init__(self, fieldslist, entries):
        super().__init__()
        data = {}
        for field in fieldslist:
            data[field] = entries[field].get()
            entries[field].delete(0, tkinter.END)

        # membuat koneksi ke database
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()

        # membuat tabel jika belum ada
        c.execute('''CREATE TABLE IF NOT EXISTS dokter
                    (ID TEXT, Nama TEXT, Spesialis TEXT, Status TEXT)''')

        sid = ''.join(random.choices(string.digits, k=6))
        num = str(random.randint(1, 10000)).zfill(6)
        id = str(sid+num)
        # menambahkan data ke tabel
        c.execute("INSERT INTO dokter VALUES (?,?,?,?)",
                  (id, data['Nama'], data['Spesialis'], data['Status']))
        conn.commit()

        # menutup koneksi ke database
        conn.close()


class UpdateDokter():
    def __init__(self, fieldslist, entries, table):
        super().__init__()
        data = {}
        for field in fieldslist:
            data[field] = entries[field].get()
            entries[field].delete(0, tkinter.END)

        # membuat koneksi ke database
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()

        selected_item = table.selection()[0]
        values = table.item(selected_item)["values"]
        # menambahkan data ke tabel
        c.execute("UPDATE dokter SET Nama = ?, Spesialis = ?, Status = ? WHERE id = ?",
                  (data['Nama'], data['Spesialis'], data['Status'], values[0]))
        conn.commit()

        # menutup koneksi ke database
        conn.close()
# =======================================================================================
# Delete


class DeletePasien():
    def __init__(self, table):
        super().__init__()
        # membuat koneksi ke database
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()

        selected_item = table.selection()[0]
        values = table.item(selected_item)["values"]

        c.execute("DELETE FROM pasien WHERE id=?", (values[0],))
        conn.commit()
        conn.close()


class Readata():
    def __init__(self, table, db):
        super().__init__()
        # membuat koneksi ke database
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()

        # Read Data
        c.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(db))
        result = c.fetchone()

        if result:
            # tabel tersedia, lakukan operasi yang diinginkan
            c.execute("SELECT * FROM {}".format(db))
            data = c.fetchall()

            if db == 'pasien':
                index = 1
                if len(data) != 0:
                    table.delete(*table.get_children())
                    for row in data:
                        table.insert('', 'end', text=str(index), values=(
                            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                        index += 1
                    conn.commit()
                conn.close()

            if db == 'dokter':
                index = 1
                if len(data) != 0:
                    table.delete(*table.get_children())
                    for row in data:
                        table.insert('', 'end', text=str(index), values=(
                            row[0], row[1], row[2], row[3]))
                        index += 1
                    conn.commit()
                conn.close()

        else:
            # tabel tidak tersedia, tampilkan pesan kesalahan
            print("Tabel 'pasien' tidak tersedia di dalam database.")
