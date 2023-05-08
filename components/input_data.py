import tkinter as tk
from components.querydb import AddPasien, DeletePasien, UpdatePasien
import tkinter.messagebox as messagebox


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
                AddPasien(fieldslist, entries)

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=2, sticky="e", padx=5, pady=5)


class Update(tk.Frame):
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
                entry_ = tk.Entry(window, width=35)
                entry_.insert(0, values[i])
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                UpdatePasien(fieldslist, entries, table)

            submit_ = tk.Button(
                window, text="Update", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            parent, text="Edit", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=3, sticky="e", padx=5, pady=5)


class DeleteData(tk.Frame):
    def __init__(self, parent, table):
        super().__init__()

        def deleted():
            confirm = messagebox.askyesno("Hapus", "Yakin ingin menghapus ?")
            if confirm:
                DeletePasien(table)
                messagebox.showinfo("", "Data terhapus")

        input_button = tk.Button(
            parent, text="Delete", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=deleted)
        input_button.grid(row=0, column=4, sticky="e", padx=5, pady=5)
