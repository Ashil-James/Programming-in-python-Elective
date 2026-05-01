import tkinter as tk
from tkinter import messagebox

def show_text():
    messagebox.showinfo("Greeting", "Hello, welcome to the world of Tkinter!")
    

root = tk.Tk()
root.title("Dialog box")
root.geometry("300x150")

button = tk.Button(root, text = "Show Greeting", command = show_text)
button.pack(pady = 20)
root.mainloop()