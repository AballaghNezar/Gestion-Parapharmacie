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
cursor.execute("SELECT * from Produit ")
result = cursor.fetchall()


def btn_clicked():
    print("Button Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Menu3.py", shell=True)


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

background_img = PhotoImage(file = f"backgroundAff.png")
background = canvas.create_image(
    591.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Aff.png")
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


MedicamentList = StringVar(value=result)

# listbox = MultiListbox(
    
#     listvariable=MedicamentList,
#     height=6,
#     selectmode='extended',
#     font = ('arial',16,'normal'))

# # listbox.grid(
# #     column=20,
# #     row=100,
# #     sticky='nwes'
# # )
# listbox.place(
#     x = 471, y = 45,
#     width = 598,
#     height = 598
#     )
tree = ttk.Treeview( column=("c1", "c2", "c3","c4","c5","c6","c7","c8"), show='headings', height=9)
tree.column("# 1", anchor=CENTER, width=50)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER, width=70)
tree.heading("# 2", text="Nom Med")
tree.column("# 3", anchor=CENTER, width=50)
tree.heading("# 3", text="Ref Med")
tree.column("# 4", anchor=CENTER, width =70)
tree.heading("# 4", text="Prix Med")
tree.column("# 5", anchor=CENTER, width=40)
tree.heading("# 5", text="Qte Med")
tree.column("# 6", anchor=CENTER, width=70)
tree.heading("# 6", text="Fournisseur")
tree.column("# 7", anchor=CENTER, width=70)
tree.heading("# 7", text="Categorie")
tree.column("# 8", anchor=CENTER, width=70)
tree.heading("# 8", text="Vente")
i=0
for row in result :
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
# tree.pack(side=LEFT)

# tree.pack(padx=471)
# XScroll=ttk.Scrollbar(orient="horizontal",command=tree.xview )
# XScroll.pack(side=LEFT, fill='x')
window.resizable(False, False)
window.mainloop()
