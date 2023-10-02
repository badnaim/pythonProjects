import tkinter as tk
from tkinter import ttk

def button_func():
  entry_text = entry.get()
  print(entry_text)
  # update the label
  # label.configure(text = 'some otehr text')
  label['text'] = entry_text
  entry['state'] = 'disabled'
  # print(label.configure())

# window
window = tk.Tk()
window.title('Getting and setting widgets')

# widgets
label = ttk.Label(master = window, text = 'Hello')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'Submit', command = button_func)
button.pack()

# exercise 
# add another button that changes text bnack to 'some text' and that enables entry

def reset_func():
  # pass
  label['text'] = 'cleared'
  entry['state'] = 'enabled'

exercise_button = ttk.Button(master = window, text = 'button', command = reset_func)
exercise_button.pack()

# run
window.mainloop()