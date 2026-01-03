from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# ---------------- MAIN WINDOW ----------------
root = Tk()
root.title("Denomination Calculator")
root.configure(bg="light blue")
root.geometry("650x400")

# Image
img = Image.open("app_img.jpg")
img = img.resize((300, 300))
photo = ImageTk.PhotoImage(img)

img_label = Label(root, image=photo, bg="light blue")
img_label.place(x=100, y=20)

welcome_label = Label(
    root,
    text="Hey user! Welcome to Denomination Counter Application.",
    bg="light blue",
    font=("Arial", 12)
)
welcome_label.place(relx=0.5, y=340, anchor=CENTER)

# ---------------- TOP WINDOW FUNCTION ----------------
def topwin():
    top = Toplevel(root)
    top.title("Denomination Calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    Label(top, text="Enter total amount:", bg="light grey").place(x=50, y=30)
    amount_entry = Entry(top)
    amount_entry.place(x=200, y=30)

    Label(
        top,
        text="Number of notes for each denomination",
        bg="light grey",
        font=("Arial", 10, "bold")
    ).place(x=120, y=70)

    Label(top, text="2000", bg="light grey").place(x=150, y=110)
    Label(top, text="500", bg="light grey").place(x=150, y=150)
    Label(top, text="100", bg="light grey").place(x=150, y=190)

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    t1.place(x=220, y=110)
    t2.place(x=220, y=150)
    t3.place(x=220, y=190)

    def calculator():
        try:
            amount = int(amount_entry.get())

            note2000 = amount // 2000
            amount %= 2000

            note500 = amount // 500
            amount %= 500

            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, note2000)
            t2.insert(END, note500)
            t3.insert(END, note100)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    Button(
        top,
        text="Calculate",
        command=calculator,
        bg="brown",
        fg="white"
    ).place(x=230, y=240)

# ---------------- MESSAGE BOX ----------------
def msg():
    answer = messagebox.askokcancel(
        "Alert",
        "Do you want to calculate the denomination count?"
    )
    if answer:
        topwin()

Button(
    root,
    text="Let's get started",
    command=msg,
    bg="brown",
    fg="white",
    font=("Arial", 11)
).place(x=260, y=360)

root.mainloop()
