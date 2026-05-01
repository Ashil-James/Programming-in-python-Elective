import tkinter as tk

root = tk.Tk()
    
entry = tk.Entry(root)   # create textbox
entry.pack()             # show it

label = tk.Label(root)   # create label
label.pack()             # show it

def show():
    text = entry.get()           # get input
    label.config(text=text)      # show input

btn = tk.Button(root, text="Show", command=show)
btn.pack()

root.mainloop()