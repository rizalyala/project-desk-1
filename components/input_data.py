import tkinter as tk
import pyrebase

# Database
firebaseConfig = {
    "apiKey": "AIzaSyCDhnuglYOPe9B3N3eqBn_tvw2IOqxdQZc",
    "authDomain": "sirs-01-3adfc.firebaseapp.com",
    "databaseURL": "https://sirs-01-3adfc-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "sirs-01-3adfc",
    "storageBucket": "sirs-01-3adfc.appspot.com",
    "messagingSenderId": "1017194189692",
    "appId": "1:1017194189692:web:76b902e8d1a65a5addcaf9"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


class InputDataFromFirebase(tk.Frame):
    def __init__(self, parent, res, fieldslist):
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
                data = {}
                for field in fieldslist:
                    data[field] = entries[field].get()
                    entries[field].delete(0, tk.END)
                db.child("pasien_datas").push(data)

            submit_ = tk.Button(
                window, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=submiting_data)
            submit_.grid(row=10, column=1, columnspan=2)

        # Main
        input_button = tk.Button(
            res, text="Add", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=input_window)
        input_button.grid(row=0, column=2, sticky="e", padx=5, pady=5)
