# GUI / Grapical User interface

import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk

window = tk.Tk()
window.configure(bg="#ef5fff")
window.title("Apps inputan")
window.geometry("300x200")
window.resizable(False,False)

# input frame
input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=0, fill="x", expand=True)

# 1.membuat label
nama_depan = ttk.Label(input_frame, text="nama depan")
nama_depan.pack(padx=10, fill="x", expand=True)
# 2.entry nama depan
Ndepan = tk.StringVar()
entry_nama_depan = ttk.Entry(input_frame, textvariable=Ndepan)
entry_nama_depan.pack(padx=10, fill="x", expand=True)

# 3.membuat label
nama_belakang = ttk.Label(input_frame, text="nama belakang")
nama_belakang.pack(padx=10, fill="x", expand=True)
# 4.entry nama belakang
Nbelakang = tk.StringVar()
entry_nama_belakang = ttk.Entry(input_frame, textvariable=Nbelakang)
entry_nama_belakang.pack(padx=10, fill="x", expand=True)

# btn
def onclic():
   msg = f"{Ndepan.get()} {Nbelakang.get()}"
   showinfo(title="pesan masuk", message=msg)
btn = ttk.Button(input_frame, command=onclic, text="ok")
btn.pack(padx=10, pady=20, fill="x", expand=True)


































window.mainloop()