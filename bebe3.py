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
    Categorie text, Vente int NOT NULL DEFAULT 0 ); """)
cursor.execute("SELECT Nom,Prix from Produit WHERE Categorie='Bebe' ")
result = cursor.fetchall()


def getElement(event):
  selection = event.widget.curselection()
  index = selection[0]
  value = event.widget.get(index)
#   print(index,' -> ',value)
#   print(value[0])
  return value[0]
#   result.set(value)
#   print(index,' -> ',value)
 


# def selectItem(a):
#     curItem = tree.focus()
#     # print(tree.item(curItem))
#     # print(loc_value)
#     # print(curItem)


def item_Value():
    global Spin_Value
    Spin_Value=current_value.get()
    # print(Spin_Value)
    global itemVal
    itemVal=Spin_Value
    return Spin_Value

def show_Selected():
    
    # selection=tree.selection()
    for i in listbox.curselection():
        print(listbox.get(i))
        global selectVal
        selectVal=listbox.get(i)
        # print(selectVal)
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
    # print (current_value.get())
    # item=item_Value()
    # value = event.widget.get(index)
    # print(selectVal[0])

    # print(selected())
    count=0
    MyItem=StringVar()
    # for car2 in selected:
    #     while car2 !=" ":
    #         # MyItem=str(MyItem)+str(car)
    #         count+=1
    # for i in range (0,len(selected)):
    #     # while(selected[i]!=" "): 
    #     #     count+=1
    #     print("hello")
    # found = re.search(' (.+?) ', selected).group(1)
    # print(found)

    # MyItem=selected
    print(resultQte[0])
    # selected=selected[:count]
    # item=car
    try:
        if (resultQte[0] > 0 ):
            cursor.execute("UPDATE Produit SET Qte=Qte - '"+str(1)+"' where Nom='"+row[0]+"'")
            db.commit()
            cursor.execute("UPDATE Produit SET Vente=Vente + 1 where Nom='"+row[0]+"'")
            db.commit()
            print(resultQte[1])
            print("update avec succes")
            messagebox.showinfo("Erreur", "Votre commande a été passée avec succès")
        # print(itemVal)
        else:
            messagebox.showinfo("Erreur", "Excusez nous!, Y a un rupture de stock dans cet Medicament")
    except:
        print("Probleme lor's de la updating")
        # print(itemVal)
    # print(show_Selected())
    # print(item)
    # print(getElement())

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

background_img = PhotoImage(file = f"backgroundBebe.png")
background = canvas.create_image(
    591.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Bebe2.png")
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

img1 = PhotoImage(file = f"img1Bebe2.png")
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
# tree = ttk.Treeview( column=("c1","c2"), show='headings', height=9)

# tree.column("# 1",  width=100)
# tree.heading("# 1", text="Nom Med")
# tree.column("# 2",  width=100)
# tree.heading("# 2", text="Prix")
# tree.bind('<ButtonRelease-1>', selectItem)
# i=0
# for row in result :
#     # NomMed = Label(
#     #               text = result[i])
    
#     # tree.insert('', 'end', text="1", values=result[i])
#     i+=1
# tree.insert('', 'end', text="2", values=reslut[1])
# tree.insert('', 'end', text="3", values=reslut[2])
# tree.insert('', 'end', text="4", values=reslut[3])
# tree.insert('', 'end', text="5", values=reslut[4])
# tree.place(
#     x = 471, y = 45,
#     width = 600,
#     height = 502
#     )
# NomMed.place(
#     x = 471, y = 45,
#     )
# current_value = StringVar(value=0)
# spin_box = ttk.Spinbox(
#     from_=0,
#     to=30,
#     textvariable=current_value,
#     wrap=True)
#==================SpinBox:=============================
# current_value = IntVar()
# spin_box = ttk.Spinbox(
#     window,
#     from_=0,
#     to=30,
#     textvariable=current_value,
#     command=item_Value,
#     wrap=True)

# spin_box.place(
#     x = 623, y = 579,
#     width = 60,
#     height = 50
    
# )  
#------------------------------------------
# NomProd=label(window,text="Nom Produit" , relief=RAISED)
# NomProd.place(x = 471, y = 35,)
w = Label(window, text="NOM DE PRODUIT")
w.place(x = 471, y = 21)
w = Label(window, text="PRIX DE PRODUIT")
w.place(x = 771, y = 21)
listbox = Listbox( width=40, height=10)
listbox.bind('<<ListboxSelect>>', getElement)
# Inserting the listbox items
# listbox.insert(1, "Data Structure")
# listbox.insert(2, "Algorithm")
# listbox.insert(3, "Data Science")
# listbox.insert(4, "Machine Learning")
# listbox.insert(5, "Blockchain")
# listbox.insert(0, "Nom:                         |    Prix:")
i=0
# myTuple=row
print(result) 
spacing="                                                                                                                 "
for row in result :
    print(row[0])
    for i in range (0,len(row[0])):
        spacing= spacing[:-2]

    print(len(row[0]))
    rowCourant=row
    listbox.insert(i,spacing.join(str(j) for j in rowCourant))
    
    
    # listbox.insert(i, "        ")
    i+=1
    spacing="                                                                                                                 "# tree.insert('', 'end', text="2", values=reslut[1])
# tree.insert('', 'end', text="3", values=reslut[2])
# tree.insert('', 'end', text="4", values=reslut[3])
# tree.insert('', 'end', text="5", values=reslut[4])
listbox.place(
    x = 471, y = 45,
    width = 600,
    height = 502
    )
# def selected_item2():
     
#     # Traverse the tuple returned by
#     # curselection method and print
#     # corresponding value(s) in the listbox
#     for i in listbox.curselection():
#         print(listbox.get(i))
 
# Create a button widget and
# map the command parameter to
# selected_item function
# btn = Button( text='Print Selected', command=selected_item2)
 
# Placing the button and listbox
# btn.pack(side='bottom')
# listbox.pack()



window.resizable(False, False)
window.mainloop()
