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


class FormInputFirebase(tk.Frame):
    def __init__(self, parent, res, fieldsList):
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
            for i, field in enumerate(fieldsList):
                entry_label = tk.Label(window, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)
                entry_ = tk.Entry(window, width=35)
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            def submiting_data():
                data = {}
                for field in fieldsList:
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


class EditFormFirebase(tk.Frame):
    def __init__(self, parent, table, fieldsList, table_tab):
        super().__init__(parent)

        entries = {}

        def show_edit_form():
            selected_item = table.selection()[0]
            values = table.item(selected_item)["values"]

            edit_form = tk.Toplevel(table_tab)
            edit_form.title("Edit Data")
            edit_form.geometry("400x600")
            edit_form.resizable(False, False)

            label_ = tk.Label(edit_form, text="Edit Data")
            label_.grid(row=0, column=1, columnspan=2)

            for i, field in enumerate(fieldsList):
                entry_label = tk.Label(edit_form, text=field + " : ")
                entry_label.grid(row=i+1, column=0, sticky="w", padx=10)
                entry_ = tk.Entry(edit_form, width=35)
                entry_.insert(0, values[i])
                entry_.grid(row=i+1, column=1, padx=10, pady=10)

                entries[field] = entry_

            submit_ = tk.Button(
                edit_form, text="Edit", border=0, bg="#EF5B0C", padx=10, fg="white", font=("Arial", 9, "bold"), command=lambda: submiting_data(entries, edit_form))
            submit_.grid(row=10, column=1, columnspan=2)

        def submiting_data(entries, edit_form):
            # Mendapatkan nilai dari entry untuk setiap kolom dan mengubah data pada Firebase

            data = db.child("pasien_datas").get().val()
            selected_key = list(data.keys())[0]
            dat = {}
            for field in fieldsList:
                dat[field] = entries[field].get()
                entries[field].delete(0, tk.END)
            # new_values = [entry.get() for entry in entries.values()]
            db.child("pasien_datas").child(selected_key).set(dat)
            print(selected_key)

            # Menutup window form setelah perubahan disimpan
            edit_form.destroy()

        def show_menu(event):
            item = table.identify_row(event.y)
            if item:
                menu.post(event.x_root, event.y_root)

        table.bind("<Button-3>", show_menu)
        menu = tk.Menu(table_tab, tearoff=0)
        menu.add_command(label="Edit",
                         command=show_edit_form)
