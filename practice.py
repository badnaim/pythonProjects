import tkinter as tk
import tkinter as ttk

# functions
def button_func():
  print('button pressed')

# create a window
window = tk.Tk()
window.title('Window and widgets')
window.geometry('800x500')

# ttk widgets /label/
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# create widgets
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# exercise label
exercise_label = ttk.Label(master = window, text = 'my label')
exercise_label.pack()

# ttk button
button = ttk.Button(master = window, text = 'Submit', command = button_func) 
button.pack()

# exercise button
exercise_button = ttk.Button(master = window, text = 'Submit lambda', command = lambda: print('fuk you')) 
exercise_button.pack()


# run'
# mainloop:    Updates the gui ---- Checks for events (button, clicks, mouse movement, closing the window)
window.mainloop()
print("hello")