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
    print(Spin_Value)
    return Spin_Value

def show_Selected():
    global selectVal
    # selection=tree.selection()
    for i in listbox.curselection():
        print("listbox.get(i)")
        selectVal=listbox.get(i)
        print(selectVal)
        return listbox.get(i)
    

def btn_1():
    print("Button back Clicked")
    print("Button Clicked")
    import subprocess
    window.destroy()
    subprocess.call("Categorie.py", shell=True)

def btn_2():
    selected=show_Selected()
    print("Button Commander Clicked")
    # print (current_value.get())
    item=item_Value()
    value = event.widget.get(index)
    print(selectVal)
    # print(item_Value())
    # print(value[0])
    # print(getElement())

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

background_img = PhotoImage(file = f"backgroundBebe2.png")
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
    command = show_Selected,
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
current_value = IntVar()
spin_box = ttk.Spinbox(
    window,
    from_=0,
    to=30,
    textvariable=current_value,
    command=item_Value,
    wrap=True)

spin_box.place(
    x = 623, y = 579,
    width = 60,
    height = 50
    
)  
#------------------------------------------
listbox = Listbox( width=40, height=10, selectmode=MULTIPLE)
listbox.bind('<<ListboxSelect>>', getElement)
# Inserting the listbox items
# listbox.insert(1, "Data Structure")
# listbox.insert(2, "Algorithm")
# listbox.insert(3, "Data Science")
# listbox.insert(4, "Machine Learning")
# listbox.insert(5, "Blockchain")
i=0
for row in result :
    listbox.insert(i, row)
    i+=1
# tree.insert('', 'end', text="2", values=reslut[1])
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
