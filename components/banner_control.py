from datetime import datetime
import sqlite3
import tkinter as tk


class BannerControl(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()

        q = "SELECT COUNT(*) FROM pasien"
        cursor.execute(q)
        result = cursor.fetchone()
        jumlah_pas = result[0]

        q = "SELECT COUNT(*) FROM dokter"
        cursor.execute(q)
        result = cursor.fetchone()
        jumlah_doc = result[0]

        ban_container = tk.Frame(self, bg='#025464')
        ban_container.grid(row=0)

        ban_label = tk.Label(ban_container, text="Pasien",
                             bg='#025464', fg='white', width=40,  anchor='nw', font=("Arial", 24, "bold"))
        ban_label.grid(row=0, column=0, rowspan=3,
                       padx=10, pady=20)

        # Label
        ban_pas = tk.Label(
            ban_container, text="Pasien", bg='#025464', fg='white', font=("Arial", 10, "bold"))
        ban_pas.grid(row=0, column=1, padx=5)
        ban_pas = tk.Label(
            ban_container, text="Ruang", bg='#025464', fg='white', font=("Arial", 10, "bold"))
        ban_pas.grid(row=1, column=1, padx=5)
        ban_pas = tk.Label(
            ban_container, text="Dokter", bg='#025464', fg='white', font=("Arial", 10, "bold"))
        ban_pas.grid(row=2, column=1, padx=5)

        # Value
        ban_pas = tk.Label(
            ban_container, text=jumlah_pas, bg='#025464', fg='white', font=("Arial", 10, "bold"))
        ban_pas.grid(row=0, column=2, padx=5)
        ban_pas = tk.Label(
            ban_container, text="1000", bg='#025464', fg='white', font=("Arial", 10, "bold"))
        ban_pas.grid(row=1, column=2, padx=5)
        ban_pas = tk.Label(
            ban_container, text=jumlah_doc, bg='#025464', fg='white', font=("Arial", 10, "bold"))
        ban_pas.grid(row=2, column=2, padx=5)

        # Time
        def update_datetime():
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ban_pas.config(text=current_datetime)
            ban_pas.after(1000, update_datetime)

        ban_pas = tk.Label(
            ban_container, bg='#025464', fg='white', font=("Arial", 10, "bold"), width=20, anchor='ne')
        ban_pas.grid(row=0, column=3, padx=5)
        update_datetime()
