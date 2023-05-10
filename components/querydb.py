import sqlite3
import tkinter
import random
import string


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

        num = str(random.randint(1, 10000)).zfill(6)
        id = str("P"+num)
        # menambahkan data ke tabel
        c.execute("INSERT INTO pasien VALUES (?, ?, ?, ?,?,?,?,?,?)",
                  (id, data['Nama'], data['Ruangan'], data['Gender'], data['Usia'], data['Dokter'], data['Status'], data['Diagnosis'], data['Tanggal']))
        conn.commit()

        # menutup koneksi ke database
        conn.close()


class UpdatePas():
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
                    (ID TEXT, Nama TEXT, Spesialis TEXT, Jadwal_kerja TEXT)''')

        num = str(random.randint(1, 10000)).zfill(6)
        id = str("D"+num)
        # menambahkan data ke tabel
        c.execute("INSERT INTO dokter VALUES (?,?,?,?)",
                  (id, data['Nama'], data['Spesialis'], data['Jadwal Kerja']))
        conn.commit()

        # menutup koneksi ke database
        conn.close()


class UpdateDok():
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
        c.execute("UPDATE dokter SET Nama = ?, Spesialis = ?, Jadwal_kerja = ? WHERE id = ?",
                  (data['Nama'], data['Spesialis'], data['Jadwal Kerja'], values[0]))
        conn.commit()

        # menutup koneksi ke database
        conn.close()
# =======================================================================================


class AddStaff():
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
        c.execute('''CREATE TABLE IF NOT EXISTS staff
                    (ID TEXT, Nama TEXT,Posisi TEXT, alamat TEXT, jadwal_piket TEXT, no_telp INTEGER)''')

        num = str(random.randint(1, 10000)).zfill(6)
        id = str("S"+num)
        # menambahkan data ke tabel
        c.execute("INSERT INTO staff VALUES (?,?,?,?,?,?)",
                  (id, data['Nama'], data['Posisi'],  data['Alamat'], data['Jadwal Piket'], data['No telp']))
        conn.commit()

        # menutup koneksi ke database
        conn.close()


class UpdStaff():
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
        c.execute("UPDATE staff SET Nama = ?,Posisi=?,  Alamat = ?,Jadwal_piket = ?, No_Telp=? WHERE id = ?",
                  (data['Nama'], data['Posisi'],  data['Alamat'], data['Jadwal Piket'], data['No Telp'], values[0]))
        conn.commit()

        # menutup koneksi ke database
        conn.close()
# =======================================================================================


class DeleteD():
    def __init__(self, table, db):
        super().__init__()
        # membuat koneksi ke database
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()

        selected_item = table.selection()[0]
        values = table.item(selected_item)["values"]

        c.execute("DELETE FROM {} WHERE id=?".format(db), (values[0],))
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

            if db == 'staff':
                index = 1
                if len(data) != 0:
                    table.delete(*table.get_children())
                    for row in data:
                        table.insert('', 'end', text=str(index), values=(
                            row[0], row[1], row[2], row[3], row[4]))
                        index += 1
                    conn.commit()
                conn.close()
