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

# Fungsi Timer Belajar
def start_timer():
    try:
        minutes = int(timer_entry.get())
        seconds = minutes * 60
        countdown(seconds)
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka valid untuk waktu!")

def countdown(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer_label.config(text=f"{mins:02d}:{secs:02d}")
        root.after(1000, countdown, seconds - 1)
    else:
        timer_label.config(text="Waktu Habis!")
        messagebox.showinfo("Notifikasi", "Timer selesai!")

# Fungsi Catatan Harian
def save_note():
    file_path = "catatan_harian.txt"
    with open(file_path, "w") as file:
        file.write(note_text.get("1.0", "end-1c"))
    messagebox.showinfo("Notifikasi", f"Catatan disimpan ke {os.path.abspath(file_path)}")

def load_notes():
    try:
        with open("catatan_harian.txt", "r") as file:
            note_text.delete("1.0", "end")
            note_text.insert("1.0", file.read())
    except FileNotFoundError:
        messagebox.showerror("Error", "Tidak ada catatan yang ditemukan!")

# Fungsi To-Do List
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(END, task)
        task_entry.delete(0, END)

def mark_done():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)
        task_listbox.insert(END, f"{task} (Selesai)")

def clear_tasks():
    task_listbox.delete(0, END)

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
        "Waktu adalah segalanya, maka jangan sia-siakan kesempatan emasmu",
        "Kesuksesan adalah hasil dari persiapan, kerja keras, dan belajar dari kegagalan.",
        "Terkadang Kesuksesan selalu dimulai dari langkah kecil.",
        "Ayo terus kejar impianmu, karena hanya diri sendirilah yang dapat diharapkan pada akhitnya.",
        "Kelalalaian waktu adalah hal yang paling serakah di dunia ini.",
        "Segini aja? gimana mau raih cita-cita kalo usahamu kecil!",
        "Aikatsu, harus tetap semangat!!"
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

# Frame Timer
frame_timer = ttk.Frame(menu, style="Frame.TFrame")
menu.add(frame_timer, text="Timer Belajar")

timer_label = ttk.Label(frame_timer, text="00:00", font=("Arial", 24), foreground=COLORS["label_fg"])
timer_label.pack(pady=10)
timer_entry = ttk.Entry(frame_timer, width=10, background=COLORS["entry_bg"], foreground=COLORS["entry_fg"])
timer_entry.pack(pady=5)
start_button = tk.Button(frame_timer, text="Mulai Timer", bg=COLORS["btn_bg"], fg=COLORS["btn_fg"], command=start_timer)
start_button.pack(pady=5)

# Frame Catatan Harian
frame_notes = ttk.Frame(menu, style="Frame.TFrame")
menu.add(frame_notes, text="Catatan Harian")

note_text = Text(frame_notes, height=15, width=50, wrap="word", font=("Arial", 12), bg=COLORS["text_bg"], fg=COLORS["text_fg"], bd=2, relief="groove")
note_text.pack(pady=10)
save_button = tk.Button(frame_notes, text="Simpan Catatan", bg=COLORS["btn_bg"], fg=COLORS["btn_fg"], command=save_note)
save_button.pack(pady=5)
load_button = tk.Button(frame_notes, text="Baca Catatan", bg=COLORS["btn_bg"], fg=COLORS["btn_fg"], command=load_notes)
load_button.pack(pady=5)

# Frame To-Do List
frame_todo = ttk.Frame(menu, style="Frame.TFrame")
menu.add(frame_todo, text="To-Do List")

task_entry = ttk.Entry(frame_todo, width=30, background=COLORS["entry_bg"], foreground=COLORS["entry_fg"])
task_entry.pack(pady=5)
add_task_button = tk.Button(frame_todo, text="Tambah Tugas", bg=COLORS["btn_bg"], fg=COLORS["btn_fg"], command=add_task)
add_task_button.pack(pady=5)
task_listbox = Listbox(frame_todo, height=10, width=40, bg=COLORS["text_bg"], fg=COLORS["text_fg"])
task_listbox.pack(pady=5)
done_button = tk.Button(frame_todo, text="Tandai Selesai", bg=COLORS["btn_bg"], fg=COLORS["btn_fg"], command=mark_done)
done_button.pack(pady=5)
clear_button = tk.Button(frame_todo, text="Hapus Semua", bg=COLORS["btn_bg"], fg=COLORS["btn_fg"], command=clear_tasks)
clear_button.pack(pady=5)

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

