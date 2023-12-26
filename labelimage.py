import tkinter as tk
from PIL import Image, ImageTk

image = Image.open("image.jpg")
image = image.resize((500, 400))


root = tk.Tk()
root.title("Image")

img = ImageTk.PhotoImage(image)

label = tk.Label(root,  image= img)
label.pack()

root.mainloop()