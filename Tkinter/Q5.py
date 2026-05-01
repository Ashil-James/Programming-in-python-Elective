import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Display")
root.geometry("400x400")
# Load the image using PIL
img = Image.open("cyber_logopng.png")
img = img.resize((300, 300))
# Convert the image to a format compatible with Tkinter
img_tk = ImageTk.PhotoImage(img)

label = tk.Label(root, image = img_tk)
label.pack()

label.image = img_tk  # Keep a reference to avoid garbage collection
root.mainloop()