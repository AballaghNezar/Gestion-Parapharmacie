from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showerror

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




def btn_0():
    print("Button back Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Menu3.py", shell=True)


def btn_2():
    Reference= entry4.get()

    print("Button RechParRef Clicked")
    cursor.execute("SELECT COUNT(*) from Produit WHERE Reference = '"+ Reference+"' ")
    result = cursor.fetchone()
    if int (result[0])>0:
        cursor.execute("SELECT * FROM Produit WHERE Reference = '"+Reference+"'")
        result2 = cursor.fetchone()

        print(result2)
        entry0.delete(0,'end')
        entry1.delete(0,'end')
        entry2.delete(0,'end')
        entry3.delete(0,'end')
        variable.set(result2[6])
        entry0.insert(END,result2[5])
        entry1.insert(END,result2[4])
        entry2.insert(END,result2[3])
        entry3.insert(END,result2[1])
        
        
    else:
        messagebox.showinfo("Erreur", "Le Medicament qui a cette Reference n\'existe pas!")
def btn_1():
    Reference= entry4.get()
    Nom=entry3.get()
    Prix=entry2.get()
    Qte=entry1.get()
    Fourni=entry0.get()
    Categories=variable.get()
    print(Categories)
    print("Button Modifier Clicked")
    if(Nom!='' and Prix!='' and Qte!='' and Fourni!='' ):
        try:
            cursor.execute("UPDATE Produit SET Nom='"+Nom+"',Prix='"+Prix+"',Qte='"+Qte+"',Fournisseur='"+Fourni+"',Categorie='"+Categories+"' where Reference='"+Reference+"'")
            db.commit()
            entry4.delete(0, 'end')
            entry3.delete(0, 'end')
            entry2.delete(0, 'end')
            entry1.delete(0, 'end')
            entry0.delete(0, 'end')
        # entry5.delete(0, 'end')
        except:
            print("Y a un erreur dans la requete!!")
        
    else:
        messagebox.showinfo("Erreur", "Veuillez Remplire les Champs Obligatoires")


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

background_img = PhotoImage(file = f"backgroundMod.png")
background = canvas.create_image(
    591.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Mod.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_0,
    relief = "flat")

b0.place(
    x = 368, y = 49,
    width = 70,
    height = 70)

values=["Douleur","Med Naturelle","Bebe","Feminite","Premiers Soins","Comp Alimentaires"] 
variable = StringVar()
variable.set(values[0])
MyCategorie = OptionMenu( window,variable,*values
                            )
MyCategorie.place(
    x = 900, y = 250,
    width = 150,
    height = 41
    )


img1 = PhotoImage(file = f"img1Mod.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_1,
    relief = "flat")

b1.place(
    x = 555, y = 569,
    width = 261,
    height = 61)

entry0_img = PhotoImage(file = f"img_textBox0Mod.png")
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

entry1_img = PhotoImage(file = f"img_textBox1Mod.png")
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

entry2_img = PhotoImage(file = f"img_textBox2Mod.png")
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

entry3_img = PhotoImage(file = f"img_textBox3Mod.png")
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

img2 = PhotoImage(file = f"img2Mod.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_2,
    relief = "flat")

b2.place(
    x = 591, y = 171,
    width = 192,
    height = 51)

entry4_img = PhotoImage(file = f"img_textBox4Mod.png")
entry4_bg = canvas.create_image(
    685.5, 137.0,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)
# entry4.insert(END,'4')
entry4.place(
    x = 511.0, y = 114,
    width = 349.0,
    height = 44)

window.resizable(False, False)
window.mainloop()
