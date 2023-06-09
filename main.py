import tkinter as tk

from pages.dokterpage import DokterPage
from pages.helpage import Helpage
from pages.homepage import Homepage
from pages.labpage import LabPage
from pages.medispage import Medispage
from pages.pasienpage import PasienPage
from pages.stafpage import StafPage

root = tk.Tk()
root.geometry('1080x700')
root.resizable(False, False)

# membuat menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)


def homepage():
    # menampilkan halaman home
    dokterpages.pack_forget()
    helpages.pack_forget()  # menghapus halaman help dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    medispages.pack_forget()
    labpages.pack_forget()
    homepages.pack(fill='y', expand=True)


def helpage():
    # menampilkan halaman 2
    dokterpages.pack_forget()
    homepages.pack_forget()  # menghapus halaman home dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    medispages.pack_forget()  # menghapus halaman homepages dari tampilan
    labpages.pack_forget()
    helpages.pack(fill='y', expand=True)


def pasienpage():
    # menampilkan halaman 2
    homepages.pack_forget()
    dokterpages.pack_forget()
    helpages.pack_forget()  # menghapus halaman help dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    medispages.pack_forget()  # menghapus halaman homepages dari tampilan
    labpages.pack_forget()
    pasienpages.pack(fill='y', expand=True)


def dokterpage():
    # menampilkan halaman 2

    helpages.pack_forget()  # menghapus halaman help dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    medispages.pack_forget()
    homepages.pack_forget()  # menghapus halaman homepages dari tampilan
    labpages.pack_forget()
    dokterpages.pack(fill='y', expand=True)


def stafpage():
    # menampilkan halaman 2
    dokterpages.pack_forget()
    helpages.pack_forget()  # menghapus halaman help dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    medispages.pack_forget()
    homepages.pack_forget()  # menghapus halaman homepages dari tampilan
    labpages.pack_forget()
    stafpages.pack(fill='y', expand=True)


def medispage():
    # menampilkan halaman 2
    dokterpages.pack_forget()
    helpages.pack_forget()  # menghapus halaman help dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    homepages.pack_forget()  # menghapus halaman homepages dari tampilan
    labpages.pack_forget()
    medispages.pack(fill='y', expand=True)


def labpage():
    # menampilkan halaman 2
    dokterpages.pack_forget()
    helpages.pack_forget()  # menghapus halaman help dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    homepages.pack_forget()  # menghapus halaman homepages dari tampilan
    medispages.pack_forget()
    labpages.pack(fill='y', expand=True)


# menambahkan menu file ke menu bar
menubar.add_command(label="Home",  command=homepage)

# menambahkan menu database
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Pasien", command=pasienpage)
file_menu.add_command(label="Dokter", command=dokterpage)
file_menu.add_command(label="Staf", command=stafpage)
file_menu.add_separator()
file_menu.add_command(label="Medis", command=medispage)
file_menu.add_command(label="Laboratory", command=labpage)

menubar.add_cascade(label="Database", menu=file_menu)

# menambahkan menu help ke menu bar
menubar.add_command(label="Help",  command=helpage)

# Halaman
homepages = Homepage(root)
helpages = Helpage(root)
pasienpages = PasienPage(root)
stafpages = StafPage(root)
dokterpages = DokterPage(root)
medispages = Medispage(root)
labpages = LabPage(root)

# Default Halaman saat di buka pertama kali
homepages.pack(fill="y", expand=True, padx=100)

root.update()
root.mainloop()
