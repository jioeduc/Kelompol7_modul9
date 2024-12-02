import tkinter as tk
from tkinter import ttk, Text, messagebox, StringVar, Listbox, END
import random
import os

# Skema warna
COLORS = {
    "bg": "#f7f9fc",  # Latar belakang aplikasi
    "btn_bg": "#4caf50",  # Warna tombol
    "btn_fg": "#ffffff",  # Teks pada tombol
    "text_bg": "#ffffff",  # Latar belakang area teks
    "text_fg": "#333333",  # Teks di area teks
    "entry_bg": "#ffffff",  # Latar belakang entry
    "entry_fg": "#000000",  # Teks di entry
    "label_fg": "#1e3a8a",  # Warna teks label
    "frame_bg": "#e3f2fd",  # Latar belakang frame/tab
}

# Membuat jendela utama
root = tk.Tk()
root.title("Student Productivity Toolkit")
root.geometry("500x600")
root.configure(bg=COLORS["bg"])

# Tab dengan ttk.Notebook
menu = ttk.Notebook(root)
menu.pack(expand=1, fill="both")

root.mainloop()
