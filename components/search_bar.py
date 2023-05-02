import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Search_name(tk.Frame):
    def __init__(self, parent, tableFrame, tables):
        super().__init__(parent)

        def search():
            keyword = search_var.get()
            if keyword:
                found = False
                for row in tables.get_children():
                    if keyword.lower() in tables.item(row)['values'][0].lower():
                        tables.selection_set(row)
                        found = True
                    else:
                        tables.selection_remove(row)
                if not found:
                    messagebox.showinfo('Not found', 'Data not found.')
            else:
                tables.selection_clear()

        search_var = tk.StringVar()
        search_entry = ttk.Entry(
            tableFrame, textvariable=search_var, width=50)
        search_entry.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        search_button = tk.Button(
            tableFrame, text="Cari Nama", command=search, bg="#EF5B0C", border=0, fg="white", font=("Arial", 9, "bold"), padx=10)
        search_button.grid(row=0, column=1, padx=5, pady=5, sticky="w")
