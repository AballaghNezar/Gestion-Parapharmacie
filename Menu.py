from tkinter import *


def btn_1():
    print("Button 1 Clicked")
    import subprocess
    window.destroy()
    subprocess.call("C:/Users/YASSIR/Desktop/prj/version2/All_Files/Connexion.py", shell=True)
    
def btn_2():
    print("Button 2 Clicked")
def btn_3():
    print("Button 3 Clicked")
    
def btn_4():
    print("Button 4 Clicked")
def btn_5():
    print("Button 5 Clicked")


window = Tk()

window.geometry("1090x665")
window.configure(bg = "#f0f0f0")
canvas = Canvas(
    window,
    bg = "#f0f0f0",
    height = 665,
    width = 1090,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"backgroundMenu.png")
background = canvas.create_image(
    545.0, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Menu.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_1,
    relief = "flat")

b0.place(
    x = -12, y = 600,
    width = 125,
    height = 65)

img1 = PhotoImage(file = f"img1Menu.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_2,
    relief = "flat")

b1.place(
    x = 668, y = 173,
    width = 100,
    height = 100)

img2 = PhotoImage(file = f"img2Menu.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_3,
    relief = "flat")

b2.place(
    x = 255, y = 143,
    width = 100,
    height = 160)

img3 = PhotoImage(file = f"img3Menu.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_4,
    relief = "flat")

b3.place(
    x = 668, y = 385,
    width = 100,
    height = 100)

img4 = PhotoImage(file = f"img4Menu.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_5,
    relief = "flat")

b4.place(
    x = 255, y = 392,
    width = 100,
    height = 100)

window.resizable(False, False)
window.mainloop()
