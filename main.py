import tkinter as tk
from sidebar import Sidebar


root = tk.Tk()
root.geometry("1080x600")
root.title("Praktek SI")


# Main frame
mainf = tk.Frame(root)
mainf.pack(side='right', fill='both', expand=True)

sidebar = Sidebar(root, mainf)
root.mainloop()
