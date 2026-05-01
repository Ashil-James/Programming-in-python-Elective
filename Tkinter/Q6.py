import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Greeting", "Hello, welcome to the world of Tkinter!")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message!")
    
def show_error():
    messagebox.showerror("Error", "An error has occurred!")
    
def ask_question():
    response = messagebox.askyesno("Question", "Do you like Tkinter?")
    if response == True:
        messagebox.showinfo("Response", "Great! Tkinter is awesome!")
    else:
        messagebox.showinfo("Response", "Oh no! Maybe give it another try!")

root = tk.Tk()
root.title("Multiple Popups Example")

# Buttons to trigger each popup
tk.Button(root, text="Show Info", command=show_info).pack(pady=5)
tk.Button(root, text="Show Warning", command=show_warning).pack(pady=5)
tk.Button(root, text="Show Error", command=show_error).pack(pady=5)
tk.Button(root, text="Ask Yes/No", command=ask_question).pack(pady=5)

# Run GUI
root.mainloop()

