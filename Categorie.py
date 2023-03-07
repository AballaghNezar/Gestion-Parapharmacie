from tkinter import *


def PremiersSoins():
    print("Button PremiersS Clicked")
    import subprocess
    window.destroy()
    subprocess.call("PremiersSoins.py", shell=True)


def ComplementsAlimentaires():
    print("Button CompAl Clicked")
    import subprocess
    window.destroy()
    subprocess.call("AlimentationsComplementaires.py", shell=True)

def Feminite():
    print("Button Feminite Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Feminite.py", shell=True)

    
def btn_4():
    print("Button Back Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Connexion.py", shell=True)

def douleur():
    print("Button Douleur Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Douleur.py", shell=True)

def MedN():
    print("Button MedN Clicked")
    import subprocess
    window.destroy()
    subprocess.call("MedecineNaturelle.py", shell=True)

def Bebe():
    print("Button Bebe Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Bebe3.py", shell=True)

window = Tk()

photo = PhotoImage(file = "logoIconReg.png")
window.iconphoto(False, photo)
window.title("MyParmacy")
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

background_img = PhotoImage(file = f"backgroundCate.png")
background = canvas.create_image(
    586.0, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Cate.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = PremiersSoins,
    relief = "flat")

b0.place(
    x = 693, y = 412,
    width = 112,
    height = 112)

img1 = PhotoImage(file = f"img1Cate.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = ComplementsAlimentaires,
    relief = "flat")

b1.place(
    x = 897, y = 412,
    width = 112,
    height = 112)

img2 = PhotoImage(file = f"img2Cate.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = Feminite,
    relief = "flat")

b2.place(
    x = 489, y = 412,
    width = 112,
    height = 112)

img3 = PhotoImage(file = f"img3Cate.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_4,
    relief = "flat")

b3.place(
    x = 368, y = 78,
    width = 57,
    height = 54)

img4 = PhotoImage(file = f"img4Cate.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = douleur,
    relief = "flat")

b4.place(
    x = 489, y = 148,
    width = 112,
    height = 112)

img5 = PhotoImage(file = f"img5Cate.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = MedN,
    relief = "flat")

b5.place(
    x = 693, y = 148,
    width = 112,
    height = 112)

img6 = PhotoImage(file = f"img6Cate.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = Bebe,
    relief = "flat")

b6.place(
    x = 897, y = 148,
    width = 112,
    height = 112)

window.resizable(False, False)
window.mainloop()
