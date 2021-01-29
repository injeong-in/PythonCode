import tkinter as tk
from tkinter import filedialog


#make the window
win = tk.Tk()
win.geometry('300x500')
win.title('temp')


#make the button
btn = tk.Button(win, text="Button")
btn.pack()

btn2 = tk.Button(win, padx=5, pady=10, text="Button2")
btn2.pack()

btn3 = tk.Button(win, fg="red", bg='yellow', text="Button3")
btn3.pack()

# write the function(def) in command variable
btn4 = tk.Button(win, text="operating", command= 'function')

win.configure(bg='gray') #change the color

label = tk.Label(win, text="Xml Changing")
label.pack()


# List Frame
list_frame = tk.Frame(win)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = tk.Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

win.mainloop() #implment the window

