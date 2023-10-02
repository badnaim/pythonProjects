import tkinter as tk
from tkinter import ttk

def button_func():
  print(string_var.get())
  string_var.set('button pressed')

# window \
window = tk.Tk()
window.title('Tkinter variables')

# tkinter variable
string_var = tk.StringVar()

# widgets 
label = ttk.Label(master = window, text = 'label', textvariable= string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable= string_var)
entry.pack()

entry1 = ttk.Entry(master = window, textvariable= string_var)
entry1.pack()

button = ttk.Button(master=window, text = 'button', command = button_func)
button.pack()

# ----------

exercie_var = tk.StringVar(value='test')

entry1 = ttk.Entry(master = window, textvariable = exercie_var)
entry1.pack()
entry2 = ttk.Entry(master = window, textvariable = exercie_var)
entry2.pack()

exercie_label = ttk.Label(master = window, textvariable = exercie_var)
exercie_label.pack()

# ----------

# run 
window.mainloop()