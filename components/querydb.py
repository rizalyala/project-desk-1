import sqlite3
import tkinter
import random


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
                    (ID_pasien TEXT, Nama_pasien TEXT, tgl_lahir INTEGER, Sex TEXT, Usia TEXT,Gol_darah TEXT,Status TEXT,Pekerjaan TEXT,Diag_awal Text,  Tanggal TEXT)''')

        num = str(random.randint(1, 10000)).zfill(6)
        id = str("P"+num)
        # menambahkan data ke tabel
        c.execute("INSERT INTO pasien VALUES (?, ?, ?, ?,?,?,?,?,?,?)",
                  (id, data['Nama Pasien'], data['Tanggal Lahir'], data['Sex'], data['Usia'], data['Gol. Darah'], data['Status'], data['Pekerjaan'], data['Diagnosa Awal'],  data['Tanggal']))
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
        c.execute("UPDATE pasien SET Nama_pasien = ?, tgl_lahir = ?, Sex = ?, Usia = ?, Gol_darah = ?, Status = ?, Pekerjaan = ?, Diag_awal=?,Tanggal =? WHERE id = ?",
                  (data['Nama Pasien'], data['Tanggal Lahir'], data['Sex'], data['Usia'], data['Gol. Darah'], data['Status'], data['Pekerjaan'], data['Diagnosa Awal'], data['Tanggal'], values[0]))
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
                    (ID TEXT, Nama_dokter TEXT, Spesialis TEXT, Jadwal_kerja TEXT)''')

        num = str(random.randint(1, 10000)).zfill(6)
        id = str("D"+num)
        # menambahkan data ke tabel
        c.execute("INSERT INTO dokter VALUES (?,?,?,?)",
                  (id, data['Nama Dokter'], data['Spesialis'], data['Jadwal Kerja']))
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
        c.execute("UPDATE dokter SET Nama_dokter = ?, Spesialis = ?, Jadwal_kerja = ? WHERE id = ?",
                  (data['Nama Dokter'], data['Spesialis'], data['Jadwal Kerja'], values[0]))
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
                    (ID TEXT, Nama_staff TEXT,Posisi TEXT, alamat TEXT, jadwal_piket TEXT, no_telp INTEGER)''')

        num = str(random.randint(1, 10000)).zfill(6)
        id = str("S"+num)
        # menambahkan data ke tabel
        c.execute("INSERT INTO staff VALUES (?,?,?,?,?,?)",
                  (id, data['Nama Staff'], data['Posisi'],  data['Alamat'], data['Jadwal Piket'], data['No telp']))
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
        c.execute("UPDATE staff SET Nama_staff = ?,Posisi=?,  Alamat = ?,Jadwal_piket = ?, No_Telp=? WHERE id = ?",
                  (data['Nama Staff'], data['Posisi'],  data['Alamat'], data['Jadwal Piket'], data['No Telp'], values[0]))
        conn.commit()

        # menutup koneksi ke database
        conn.close()
# =======================================================================================


class AddObat():
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
        c.execute('''CREATE TABLE IF NOT EXISTS obat
                    (ID TEXT, Nama_obat TEXT,Deskripsi TEXT, Dosis TEXT, stok TEXT, tgl_kdluarsa INTEGER)''')

        num = str(random.randint(1, 10000)).zfill(6)
        id = str("S"+num)
        # menambahkan data ke tabel
        c.execute("INSERT INTO obat VALUES (?,?,?,?,?,?)",
                  (id, data['Nama Obat'], data['Deskripsi'],  data['Dosis'], data['Stok'], data['Tgl Kadaluarsa']))
        conn.commit()

        # menutup koneksi ke database
        conn.close()


class UpdObat():
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
        c.execute("UPDATE obat SET Nama_obat = ?,Deskripsi=?,  Dosis = ?,stok=?, tgl_kdluarsa=? WHERE id = ?",
                  (data['Nama Obat'], data['Deskripsi'],  data['Dosis'], data['Stok'], data['Tgl Kadaluarsa'], values[0]))
        conn.commit()

        # menutup koneksi ke database
        conn.close()
# =======================================================================================


class AddRekam():
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
        c.execute('''CREATE TABLE IF NOT EXISTS rekam_medis
                    (ID TEXT, Nama_pasien TEXT,Dokter TEXT, Perawatan TEXT, Diag_utama TEXT, Resep_obat Text, tgl_keluar TEXT)''')

        num = str(random.randint(1, 10000)).zfill(6)
        id = str("S"+num)
        # menambahkan data ke tabel
        c.execute("INSERT INTO rekam_medis VALUES (?,?,?,?,?,?,?)",
                  (id, data['Nama Pasien'], data['Dokter'],  data['Perawatan'], data['Diagnosa Utama'], data['Resep Obat'], data['Tgl Keluar']))
        conn.commit()

        # menutup koneksi ke database
        conn.close()


class UpdRekam():
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
        c.execute("UPDATE rekam_medis SET Nama_pasien = ?,Dokter=?,  Perawatan = ?,Diag_utama=?, Resep_obat=?,tgl_keluar=? WHERE id = ?",
                  (data['Nama Pasien'], data['Dokter'],  data['Perawatan'], data['Diagnosa Utama'], data['Resep Obat'], data['Tgl Keluar'], values[0]))
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

        c.execute("DELETE FROM {} WHERE ID=?".format(db), (values[0],))
        conn.commit()
        Readata(table, db)
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
                            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
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
                            row[0], row[1], row[2], row[3], row[4], row[5]))
                        index += 1
                    conn.commit()
                conn.close()

            if db == 'obat':
                index = 1
                if len(data) != 0:
                    table.delete(*table.get_children())
                    for row in data:
                        table.insert('', 'end', text=str(index), values=(
                            row[0], row[1], row[2], row[3], row[4], row[5]))
                        index += 1
                    conn.commit()
                conn.close()

            if db == 'rekam_medis':
                index = 1
                if len(data) != 0:
                    table.delete(*table.get_children())
                    for row in data:
                        table.insert('', 'end', text=str(index), values=(
                            row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                        index += 1
                    conn.commit()
                conn.close()
