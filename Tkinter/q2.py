import tkinter as tk
from tkinter import messagebox

def show_text():
    text = entry.get()
    messagebox.showinfo("Entered Text", text)
    

root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("300x150")

# Label
label = tk.Label(root, text ="Enter something: ")
label.pack(pady = 5)

# Entry 
entry = tk.Entry(root)
entry.pack(pady = 5)

# Button
button = tk.Button(root, text = "Show Text", command = show_text)
button.pack(pady = 5)

root.mainloop()