# Activity_1
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.tilte("image")
root.geometry("400x400")

upload = Image.open("app_img.jpg")
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width=300)
label2 = Label(root, text="This is how you add image Tkinter window")
label2.place(x=40, y=360)

root.mainloop()

# Activity_2
root.Tk()
root.geometry("200x200")


def msg():
    messagebox.showwarning("Alert", "Stop virus found")


button = Button(root, text="scan virus", command=msg)

root.mainloop()

# Activity_3
root = Tk()
root.geometry = "400x300"
root.title = "main"


def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    l2 = Label(top, text="this is toplevel window")
    l2.pack()

    top.mainloop()

    l = Label(root, text="this is the root window")
    btn = button(root, text="Click here to open another window", command=topwin)

    l.pack()
    btn.pack()
