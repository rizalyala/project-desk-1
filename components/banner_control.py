from datetime import datetime
import tkinter as tk


class BannerControl(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

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
            ban_container, text="0", bg='#025464', fg='white', font=("Arial", 10, "bold"))
        ban_pas.grid(row=0, column=2, padx=5)
        ban_pas = tk.Label(
            ban_container, text="0", bg='#025464', fg='white', font=("Arial", 10, "bold"))
        ban_pas.grid(row=1, column=2, padx=5)
        ban_pas = tk.Label(
            ban_container, text="0", bg='#025464', fg='white', font=("Arial", 10, "bold"))
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
