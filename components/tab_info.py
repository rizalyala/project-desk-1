import tkinter as tk
from tkinter import ttk


class TabInfoPanel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        table_info = ttk.Treeview(self, columns=("cole"))
        table_info.column('cole')


class TabReportPanel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        table_info = ttk.Treeview(self, columns=("cole"))
        table_info.column('cole')
