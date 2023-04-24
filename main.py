import tkinter as tk
from tkinter import *
from pages.dokterpage import DokterPage

from pages.helpage import Helpage
from pages.homepage import Homepage
from pages.obatpage import Obatpage
from pages.pasienpage import PasienPage
from pages.stafpage import StafPage

root = tk.Tk()
root.geometry('800x600')

# membuat menu bar
menubar = Menu(root)
root.config(menu=menubar)


def homepage():
    # menampilkan halaman home
    dokterpages.pack_forget()
    helpages.pack_forget()  # menghapus halaman help dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    obatpages.pack_forget()  # menghapus halaman obat dari tampilan
    homepages.pack(fill=tk.BOTH, expand=True)


def helpage():
    # menampilkan halaman 2
    dokterpages.pack_forget()
    homepages.pack_forget()  # menghapus halaman home dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    obatpages.pack_forget()  # menghapus halaman homepages dari tampilan
    helpages.pack(fill=tk.BOTH, expand=True)


def pasienpage():
    # menampilkan halaman 2
    homepages.pack_forget()
    dokterpages.pack_forget()
    helpages.pack_forget()  # menghapus halaman help dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    obatpages.pack_forget()  # menghapus halaman homepages dari tampilan
    pasienpages.pack(fill=tk.BOTH, expand=True)


def dokterpage():
    # menampilkan halaman 2

    helpages.pack_forget()  # menghapus halaman help dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    obatpages.pack_forget()
    homepages.pack_forget()  # menghapus halaman homepages dari tampilan
    dokterpages.pack(fill=tk.BOTH, expand=True)


def stafpage():
    # menampilkan halaman 2
    dokterpages.pack_forget()
    helpages.pack_forget()  # menghapus halaman help dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    obatpages.pack_forget()
    homepages.pack_forget()  # menghapus halaman homepages dari tampilan
    stafpages.pack(fill=tk.BOTH, expand=True)


def obatpage():
    # menampilkan halaman 2
    dokterpages.pack_forget()
    helpages.pack_forget()  # menghapus halaman help dari tampilan
    pasienpages.pack_forget()  # menghapus halaman pasien dari tampilan
    stafpages.pack_forget()  # menghapus halaman staff dari tampilan
    homepages.pack_forget()  # menghapus halaman homepages dari tampilan
    obatpages.pack(fill=tk.BOTH, expand=True)


# menambahkan menu file ke menu bar
menubar.add_command(label="Home",  command=homepage)

# menambahkan menu database
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Pasien", command=pasienpage)
file_menu.add_command(label="Dokter", command=dokterpage)
file_menu.add_command(label="Staf", command=stafpage)
file_menu.add_separator()
file_menu.add_command(label="Obat", command=obatpage)

menubar.add_cascade(label="Database", menu=file_menu)

# menambahkan menu help ke menu bar
menubar.add_command(label="Help",  command=helpage)

# Halaman
homepages = Homepage(root)
helpages = Helpage(root)
pasienpages = PasienPage(root)
stafpages = StafPage(root)
dokterpages = DokterPage(root)
obatpages = Obatpage(root)

# Default Halaman saat di buka pertama kali
homepages.pack(fill=tk.BOTH, expand=True)
root.mainloop()
