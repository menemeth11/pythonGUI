import tkinter as tk

root = tk.Tk()
root.title("Label")

label = tk.Label(root, text= "Label in tkinter", bg= "yellow", 
font= "calibri", padx= 20, pady= 20) #wraplength= 50)

label.pack()

root.mainloop()