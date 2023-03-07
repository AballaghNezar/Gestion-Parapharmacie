from tkinter import *
import sqlite3
from tkinter import ttk


with sqlite3.connect('Produit.db') as db:
    cursor=db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Produit(
    id integer PRIMARY KEY AUTOINCREMENT,
    Nom text NOT NULL,
    Reference text NOT NULL,
    Prix float NOT NULL,
    Qte int NOT NULL,
    Fournisseur text NOT NULL,
    Categorie text, Vente int NOT NULL DEFAULT 0); """)



def btn_1():
    print("Button 1 Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Menu3.py", shell=True)
def btn_2():
    print("Button 2 Clicked")
    Categorie=variable.get()
    print(Categorie)
    NomP=entry4.get()
    ReferenceP=entry3.get()
    PrixP=entry2.get()
    QteP=entry1.get()
    FournisseurP=entry0.get()
    if(NomP!='' and ReferenceP!='' and PrixP!='' and QteP!='' and FournisseurP!='' ):
        cursor.execute("INSERT INTO Produit(Nom,Reference,Prix,Qte,Fournisseur,Categorie)VALUES(?,?,?,?,?,?)",(NomP,ReferenceP,PrixP,QteP,FournisseurP,Categorie))
        db.commit()
        # entry5.delete(0, 'end')
        variable.set("Douleur")
        entry4.delete(0, 'end')
        entry3.delete(0, 'end')
        entry2.delete(0, 'end')
        entry1.delete(0, 'end')
        entry0.delete(0, 'end')

def getvalue(value):
    value=variable.get()
    print(value)
window = Tk()

window.geometry("1090x665")
window.configure(bg = "#0c92bc")
canvas = Canvas(
    window,
    bg = "#0c92bc",
    height = 665,
    width = 1090,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"backgroundAjout.png")
background = canvas.create_image(
    591.5, 332.5,
    image=background_img)

values=["Douleur","Med Naturelle","Bebe","Feminite","Premiers Soins","Comp Alimentaires"] 
variable = StringVar()
variable.set(values[0])
MyCategorie = OptionMenu( window,variable,*values,command=getvalue
                            )
MyCategorie.place(
    x = 900, y = 163,
    width = 150,
    height = 41
    )
# comboExample.current(0)

img0 = PhotoImage(file = f"img0Ajout.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_1,
    relief = "flat")


b0.place(
    x = 368, y = 78,
    width = 70,
    height = 70)

img1 = PhotoImage(file = f"img1Ajout.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_2,
    relief = "flat")

b1.place(
    x = 555, y = 569,
    width = 261,
    height = 61)

entry0_img = PhotoImage(file = f"img_textBox0Ajout.png")
entry0_bg = canvas.create_image(
    685.5, 520.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)
# entry0.insert(END,'0')


entry0.place(
    x = 511.0, y = 497,
    width = 349.0,
    height = 44)

entry1_img = PhotoImage(file = f"img_textBox1Ajout.png")
entry1_bg = canvas.create_image(
    685.5, 439.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)
# entry1.insert(END,'1')


entry1.place(
    x = 511.0, y = 416,
    width = 349.0,
    height = 44)

entry2_img = PhotoImage(file = f"img_textBox2Ajout.png")
entry2_bg = canvas.create_image(
    685.5, 356.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)
# entry2.insert(END,'2')

entry2.place(
    x = 511.0, y = 333,
    width = 349.0,
    height = 44)

entry3_img = PhotoImage(file = f"img_textBox3Ajout.png")
entry3_bg = canvas.create_image(
    685.5, 271.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)
# entry3.insert(END,'3')

entry3.place(
    x = 511.0, y = 248,
    width = 349.0,
    height = 44)

entry4_img = PhotoImage(file = f"img_textBox4Ajout.png")
entry4_bg = canvas.create_image(
    685.5, 184.0,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)
# entry4.insert(END,'4')

entry4.place(
    x = 511.0, y = 161,
    width = 349.0,
    height = 44)

window.resizable(False, False)
window.mainloop()
