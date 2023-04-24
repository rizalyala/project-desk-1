import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("1280x720")

root.title("Praktek SI")

# Sidebar frame
sidebar = tk.Frame(root, bg='gray', width=200, height=500)
sidebar.pack(side='left', fill='y')

# Main frame
mainf = tk.Frame(root, bg='yellow')
mainf.pack(side='right', fill='both', expand=True)

# membuat style untuk garis
style = ttk.Style()
style.configure('Treeview', rowheight=25, font=('Arial', 12), background='white',
                foreground='black', fieldbackground='white', bordercolor='black', borderwidth=1)
# membuat treeview
tree = ttk.Treeview(mainf, columns=('col1', 'col2', 'col3'),
                    show='headings', style='Treeview')
tree.heading('col1', text='Kolom 1')
tree.heading('col2', text='Kolom 2')
tree.heading('col3', text='Kolom 3')
tree.pack(side='left', fill='both', expand=True)

# menambahkan data ke treeview
data = [
    ('Data 1', 'Data 2', 'Data 3'),
    ('Data 4', 'Data 5', 'Data 6'),
    ('Data 7', 'Data 8', 'Data 9')
]
for i, row in enumerate(data):
    tree.insert(parent='', index=i, values=row)
root.mainloop()
