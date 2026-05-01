import tkinter as tk

root = tk.Tk()
root.title("Image Display")
root.geometry("400x400")
img = tk.PhotoImage(file = "cyber_logopng.png")
label = tk.Label(root, image = img)
label.pack()
root.mainloop()