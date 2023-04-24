import tkinter as tk
from tkinter import ttk


class Homepage(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        #
        label_frame = ttk.LabelFrame(self, text="Label Entry")
        label_frame.grid(row=1, column=1, padx=10, pady=10)

        table = ttk.Treeview(label_frame, columns=(
            "col1", "col2", "col3"), height=100)
        table.column("#0", width=50)
        table.column("col1", width=150)
        table.column("col2", width=150)
        table.column("col3", width=150)
        table.heading("#0", text="No.")
        table.heading("col1", text="Kolom 1")
        table.heading("col2", text="Kolom 2")
        table.heading("col3", text="Kolom 3")
        table.pack(padx=5, pady=5)
