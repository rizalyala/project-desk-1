import tkinter as tk


class InputDataFromFirebase(tk.Frame):
    def __init__(self, parent, res):
        super().__init__(parent)

        def input_window():
            window = tk.Toplevel()
            window.title("Tambah Data Pasien")
            window.geometry("400x600")
            window.resizable(False, False)

            label_ = tk.Label(window, text="Input Pasien")
            label_.grid(row=0, column=1, columnspan=2)

            fields = ['Nama', 'Alamat', 'Usia', 'Ruang', 'Diagnosis']

            for i, field in enumerate(fields):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)
                entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

            def submiting_data():
                if submit_:
                    entry_.delete(0, tk.END)

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=6, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            res, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=2, sticky="e", padx=5, pady=5)
