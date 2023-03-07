from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showerror
import re

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
cursor.execute("SELECT Nom,Prix from Produit WHERE Categorie='Comp Alimentaires' ")
result = cursor.fetchall()


def getElement(event):
  selection = event.widget.curselection()
  index = selection[0]
  value = event.widget.get(index)
  return value[0]

def item_Value():
    global Spin_Value
    Spin_Value=current_value.get()
    global itemVal
    itemVal=Spin_Value
    return Spin_Value

def show_Selected():
    
    for i in listbox.curselection():
        print(listbox.get(i))
        global selectVal
        selectVal=listbox.get(i)
        return listbox.get(i)
    

def btn_1():
    print("Button back Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Categorie.py", shell=True)

def btn_2():
    cursor.execute("SELECT Qte,Vente from Produit WHERE Nom='"+row[0]+"' ")
    resultQte = cursor.fetchone()
    selected=show_Selected()
    print("Button Commander Clicked")
    count=0
    MyItem=StringVar()
    print(row[0])
    try:
        if (resultQte[0] > 0 ):
            cursor.execute("UPDATE Produit SET Qte=Qte - '"+str(1)+"' where Nom='"+row[0]+"'")
            db.commit()
            cursor.execute("SELECT Qte,Vente from Produit WHERE Nom='"+row[0]+"' ")
            resultQte = cursor.fetchone()
            print("update avec succes")
            messagebox.showinfo("Felicitation!", "Votre commande a été passée avec succès")
        # print(itemVal)
        else:
            messagebox.showinfo("Not Lucky!", "Excusez nous!, Y a un rupture de stock dans cet Medicament")
    except:
        print("Probleme lor's de la updating")

window = Tk()
photo = PhotoImage(file = "logoIconReg.png")
window.iconphoto(False, photo)
window.title("MyParmacy")
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

background_img = PhotoImage(file = f"backgroundAm.png")
background = canvas.create_image(
    591.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Am.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_1,
    relief = "flat")

b0.place(
    x = 368, y = 49,
    width = 70,
    height = 70)

img1 = PhotoImage(file = f"img1Am.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_2,
    relief = "flat")

b1.place(
    x = 723, y = 571,
    width = 261,
    height = 61)

w = Label(window, text="NOM DE PRODUIT")
w.place(x = 471, y = 21)
w = Label(window, text="PRIX DE PRODUIT")
w.place(x = 771, y = 21)
listbox = Listbox( width=40, height=10)
listbox.bind('<<ListboxSelect>>', getElement)
i=0
print(result) 
spacing="                                                                                                                 "
for row in result :
    print(row[0])
    for i in range (0,len(row[0])):
        spacing= spacing[:-2]

    print(len(row[0]))
    rowCourant=row
    listbox.insert(i,spacing.join(str(j) for j in rowCourant))
    i+=1
    spacing="                                                                                                                 "

listbox.place(
    x = 471, y = 45,
    width = 600,
    height = 502
    )


window.resizable(False, False)
window.mainloop()
