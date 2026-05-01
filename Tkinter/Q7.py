from tkinter import *
from tkinter import messagebox

root = Tk()

def show_all():
    messagebox.showinfo("Info", "Info Message")
    messagebox.showwarning("Warning", "Warning Message")
    messagebox.showerror("Error", "Error Message")
    res = messagebox.askyesno("Question", "Continue?")
    print(res)

btn = Button(root, text="Show", command=show_all)
btn.pack()

root.mainloop()