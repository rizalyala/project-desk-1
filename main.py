import tkinter as tk

root = tk.Tk()

root.geometry("1280x720")

root.title("Praktek SI")

sidebar = tk.Frame(root, bg='gray', width=200, height=500)
sidebar.pack(side='left', fill='y')

# membuat tombol-tombol menu
menu1_btn = tk.Button(sidebar, text='Menu 1')
menu1_btn.pack(pady=10)

menu2_btn = tk.Button(sidebar, text='Menu 2')
menu2_btn.pack(pady=10)

menu3_btn = tk.Button(sidebar, text='Menu 3')
menu3_btn.pack(pady=10)

# membuat frame utama
main_frame = tk.Frame(root, bg='white', width=500, height=500)
main_frame.pack(side='right', fill='both', expand=True)

root.mainloop()
