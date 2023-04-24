from tkinter import *
import tkinter as tk

root = Tk()
root.geometry('800x600')

# membuat menu bar
menubar = Menu(root)
root.config(menu=menubar)


def page1():
    # menampilkan halaman 1
    halaman2.pack_forget()  # menghapus halaman 2 dari tampilan
    halaman1.pack(fill=tk.BOTH, expand=True)


def page2():
    # menampilkan halaman 2
    halaman1.pack_forget()  # menghapus halaman 1 dari tampilan
    halaman2.pack(fill=tk.BOTH, expand=True)


# membuat menu file

# menambahkan menu file ke menu bar
menubar.add_command(label="Home",  command=page1)

# membuat menu help

# menambahkan menu help ke menu bar
menubar.add_command(label="Help",  command=page2)

# membuat halaman 1
halaman1 = tk.Frame(root)
teks_halaman1 = tk.Label(halaman1, text="Ini adalah halaman 1")
teks_halaman1.pack(padx=20, pady=20)

# membuat halaman 2
halaman2 = tk.Frame(root)
teks_halaman2 = tk.Label(halaman2, text="Ini adalah halaman 2")
teks_halaman2.pack(padx=20, pady=20)

root.mainloop()
