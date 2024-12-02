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

# Fungsi Kalkulator
def add_to_expression(symbol):
    calc_entry_var.set(calc_entry_var.get() + symbol)

def clear_expression():
    calc_entry_var.set("")

def calculate_expression():
    try:
        result = eval(calc_entry_var.get())
        calc_entry_var.set(str(result))
    except Exception:
        messagebox.showerror("Error", "Ekspresi tidak valid!")

# Fungsi Motivational Quote Generator
def show_quote():
    quotes = [
        "Jangan menyerah, keajaiban terjadi setiap hari.",
        "Kesuksesan adalah hasil dari persiapan, kerja keras, dan belajar dari kegagalan.",
        "Hari ini adalah kesempatan untuk lebih baik dari kemarin.",
        "Percayalah pada proses dan dirimu sendiri."
    ]
    random_quote.set(random.choice(quotes))

# Membuat jendela utama
root = tk.Tk()
root.title("Student Productivity Toolkit")
root.geometry("500x600")
root.configure(bg=COLORS["bg"])

# Tab dengan ttk.Notebook
menu = ttk.Notebook(root)
menu.pack(expand=1, fill="both")

# Frame Kalkulator
frame_calculator = ttk.Frame(menu, style="Frame.TFrame")
menu.add(frame_calculator, text="Kalkulator")

calc_entry_var = StringVar()
calc_entry = ttk.Entry(frame_calculator, textvariable=calc_entry_var, font=("Arial", 16), justify="right")
calc_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    action = calculate_expression if text == '=' else clear_expression if text == 'C' else lambda t=text: add_to_expression(t)
    tk.Button(frame_calculator, text=text, command=action, bg=COLORS["btn_bg"], fg=COLORS["btn_fg"]).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Motivational Quote Generator
random_quote = StringVar()
quote_label = ttk.Label(root, textvariable=random_quote, wraplength=400, justify="center", foreground=COLORS["label_fg"])
quote_label.pack(pady=10)
quote_button = tk.Button(root, text="Tampilkan Motivasi", bg=COLORS["btn_bg"], fg=COLORS["btn_fg"], command=show_quote)
quote_button.pack(pady=5)

root.mainloop()
