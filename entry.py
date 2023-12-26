import tkinter as tk

def Change():
    if entry["state"] !="normal":
        entry.config(state="normal")
    else:
        entry.config(state="disabled")
        print(entry.get())


root = tk.Tk()
root.title("Widget")

label = tk.Label(root, text="NAME: ")
button = tk.Button(root, text="Change it!", command=Change)
entry = tk.Entry(root, bg= "red", border=10,)

entry.insert(0, "Put here your name!")
entry.config(state="disabled")


label.pack()
entry.pack()
button.pack()

root.mainloop()