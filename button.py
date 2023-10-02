import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

# button
def button_func():
  print("basic button")
  print(radio_var.get())

button_string = tk.StringVar(value = 'a button with string var')

button = ttk.Button(window, text = "button", command = button_func, textvariable = button_string)
# button = ttk.Button(window, text = "button", command = lambda: print('basic button'))
button.pack()

# checkbutton

# check_var = tk.BooleanVar()
check_var = tk.StringVar()
# check_var = tk.IntVar()
check = ttk.Checkbutton(
  window, text = "checkbox 1", 
  command = lambda: print('check button', check_var.get()),
  # command = lambda: print('check button', type(check_var.get())),
  variable = check_var,
  onvalue = 5,
  offvalue = 10)
check.pack()

check1 = ttk.Checkbutton(
  window, 
  text = "checkbox 2", 
  command = lambda: print('check button1'))
check1.pack()

# radio button 
radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(window, text='Radio button 1', value = 'radio 1', variable = radio_var, command= lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text='Radio button 2', value = 2, variable= radio_var)
radio2.pack()
# run 
window.mainloop()