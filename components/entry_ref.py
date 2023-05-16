import sqlite3


class EntryRefPasien():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    # Nama Pasien
    querypas = "SELECT Nama_pasien FROM pasien"
    if querypas == querypas:
        cursor.execute(querypas)
        result = cursor.fetchall()
        options_pas = [r[0] for r in result]
    conn.close()


class EntryRefDokter():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    # Dokter
    querydoc = "SELECT Nama_dokter FROM dokter"
    if querydoc == querydoc:
        cursor.execute(querydoc)
        result = cursor.fetchall()
        options_doc = [r[0] for r in result]
    conn.close()


class EntryRefPerawatan():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    # Perawatan
    queryper = "SELECT ID FROM perawatan_medis"
    if queryper == queryper:
        cursor.execute(queryper)
        result = cursor.fetchall()
        options_per = [r[0] for r in result]
    conn.close()


class EntryRefObat():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    # Obat
    queryob = "SELECT Nama_Obat FROM obat"
    if queryob == queryob:
        cursor.execute(queryob)
        result = cursor.fetchall()
        options_ob = [r[0] for r in result]
    conn.close()


class EntryRefResObat():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    # Resep Obat
    queryres = "SELECT ID FROM resep_obat"
    if queryres == queryres:
        cursor.execute(queryres)
        result = cursor.fetchall()
        options_res = [r[0] for r in result]
    conn.close()
