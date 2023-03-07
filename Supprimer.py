from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.messagebox import showerror


with sqlite3.connect('Produit.db') as db:
    cursor=db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS Produit(id integer PRIMARY KEY AUTOINCREMENT,
     Nom text NOT NULL, Reference text NOT NULL, Prix float NOT NULL, Qte int NOT NULL,
     Fournisseur text NOT NULL, Categorie text, Vente int NOT NULL DEFAULT 0 ); """)


def btn_Back():
    print("Button Back Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Menu3.py", shell=True)
def Supp():
    ProduitSupp=entry0.get()
    cursor.execute("SELECT COUNT(*) from Produit WHERE Reference = '"+ ProduitSupp+"' ")
    result = cursor.fetchone()
    if int (result[0])>0:
        try:
            cursor.execute("DELETE FROM Produit WHERE Reference='"+ProduitSupp+"'")
            db.commit()
            entry0.delete(0,'end')
            print('Produit supprime')
            messagebox.showinfo("Erreur", "le Medicament a ete Supprime avec succes")
        except:
            print('Error de suppression')
    elif(ProduitSupp==''):
        messagebox.showinfo("Erreur", "Veuillez saisir la Reference du Produit")
    else:
        messagebox.showinfo("Erreur", "Il n\'existe pas d'un Produit avec cet Reference!")
        print('le produit n existe pas !')

    

    return

window = Tk()

photo = PhotoImage(file = "logoIconReg.png")
window.iconphoto(False, photo)
window.title("MyParmacy")
window.geometry("1090x665")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 665,
    width = 1090,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"backgroundSupp.png")
background = canvas.create_image(
    591.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Supp.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Supp,
    relief = "flat")

b0.place(
    x = 592, y = 381,
    width = 261,
    height = 61)

entry0_img = PhotoImage(file = f"img_textBox0Supp.png")
entry0_bg = canvas.create_image(
    722.5, 333.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 548.0, y = 310,
    width = 349.0,
    height = 44)

canvas.create_text(
    592.5, 293.0,
    text = "Reference :",
    fill = "#838484",
    font = ("Inter-Light", int(18.0)))

img1 = PhotoImage(file = f"img1Supp.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_Back,
    relief = "flat")

b1.place(
    x = 368, y = 78,
    width = 70,
    height = 70)

window.resizable(False, False)
window.mainloop()
