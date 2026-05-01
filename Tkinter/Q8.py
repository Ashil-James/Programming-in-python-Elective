import tkinter as tk
from PIL import Image, ImageTk

def show_text():
    text = entry.get()
    result_label.config(text=text)
    
    
root = tk.Tk()
root.title("Event - Driven Programming")
root.geometry("400x400")

img = Image.open("cyber_logopng.png")
img = img.resize((200, 200))
img_tk = ImageTk.PhotoImage(img)
image_label = tk.Label(root, image=img_tk)
image_label.pack(pady=10)
image_label.image = img_tk

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

button = tk.Button(root, text="Show Text", command=show_text)
button.pack(pady=5)


root.mainloop()