from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1090x665")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 665,
    width = 1090,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"backgroundCat.png")
background = canvas.create_image(
    545.0, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Cat.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 736, y = 350,
    width = 330,
    height = 266)

img1 = PhotoImage(file = f"img1Cat.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 380, y = 350,
    width = 330,
    height = 266)

img2 = PhotoImage(file = f"img2Cat.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 24, y = 350,
    width = 330,
    height = 266)

img3 = PhotoImage(file = f"img3Cat.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 736, y = 15,
    width = 330,
    height = 266)

img4 = PhotoImage(file = f"img4Cat.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 374, y = 15,
    width = 330,
    height = 266)

img5 = PhotoImage(file = f"img5Cat.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 24, y = 15,
    width = 330,
    height = 266)

window.resizable(False, False)
window.mainloop()
