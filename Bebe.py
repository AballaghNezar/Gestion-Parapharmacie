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
    Categorie text); """)
cursor.execute("SELECT Nom,Prix from Produit ")
result = cursor.fetchall()


def btn_clicked():
    print("Button Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Categorie.py", shell=True)

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

background_img = PhotoImage(file = f"backgroundBebe.png")
background = canvas.create_image(
    591.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Bebe.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 368, y = 49,
    width = 70,
    height = 70)

tree = ttk.Treeview( column=("c1","c2"), show='headings', height=9)

tree.column("# 1",  width=100)
tree.heading("# 1", text="Nom Med")
tree.column("# 2",  width=100)
tree.heading("# 2", text="Prix")
i=0
for row in result :
    # NomMed = Label(
    #               text = result[i])
    
    tree.insert('', 'end', text="1", values=result[i])
    i+=1
# tree.insert('', 'end', text="2", values=reslut[1])
# tree.insert('', 'end', text="3", values=reslut[2])
# tree.insert('', 'end', text="4", values=reslut[3])
# tree.insert('', 'end', text="5", values=reslut[4])
tree.place(
    x = 471, y = 45,
    width = 598,
    height = 598
    )
# NomMed.place(
#     x = 471, y = 45,
#     )
# current_value = StringVar(value=0)
# spin_box = ttk.Spinbox(
#     from_=0,
#     to=30,
#     textvariable=current_value,
#     wrap=True)

window.resizable(False, False)
window.mainloop()
