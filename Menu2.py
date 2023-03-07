from tkinter import *


def btn_1():
    print("Button 1 Clicked")

def btn_2():
    print("Button 2 Clicked")
def btn_3():
    print("Button 3 Clicked")
    
def btn_4():
    print("Button 4 Clicked")
    
def btn_5():
    print("Button 5 Clicked")
    import subprocess
    window.destroy()
    subprocess.call("C:/Users/YASSIR/Desktop/prj/version2/All_Files/Connexion.py", shell=True)
    


window = Tk()

window.geometry("1090x665")
window.configure(bg = "#f7f7f7")
canvas = Canvas(
    window,
    bg = "#f7f7f7",
    height = 665,
    width = 1090,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"backgroundMenu2.png")
background = canvas.create_image(
    591.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Menu2.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_1,
    relief = "flat")

b0.place(
    x = 865, y = 392,
    width = 126,
    height = 167)

img1 = PhotoImage(file = f"img1Menu2.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_2,
    relief = "flat")

b1.place(
    x = 545, y = 392,
    width = 112,
    height = 167)

img2 = PhotoImage(file = f"img2Menu2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_3,
    relief = "flat")

b2.place(
    x = 865, y = 106,
    width = 112,
    height = 164)

img3 = PhotoImage(file = f"img3Menu2.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_4,
    relief = "flat")

b3.place(
    x = 545, y = 102,
    width = 112,
    height = 168)

img4 = PhotoImage(file = f"img4Menu2.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_5,
    relief = "flat")

b4.place(
    x = 368, y = 46,
    width = 70,
    height = 70)

window.resizable(False, False)
window.mainloop()
