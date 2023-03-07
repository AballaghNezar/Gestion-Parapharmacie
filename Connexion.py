from cgitb import grey
from distutils import text_file
from logging import root
import os
# from ssl import _PasswordType
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showerror
import sqlite3
from turtle import screensize
with sqlite3.connect('users.db') as db:
    cursor=db.cursor()
def btn_clicked():
    print("Button Clicked")

def Menu():
    print("Button Clicked")
    Email=entry1.get()
    password=entry0.get()
    
    print(Email)
    print(password)

    cursor.execute("SELECT COUNT(*) from users WHERE Email = '"+ Email+"' AND password= '"+password+"'")
    result = cursor.fetchone()
    if (Email=='admin' and password=='admin'):
            import subprocess
            window.destroy()
            subprocess.call("Menu3.py", shell=True)
    else:
        if int (result[0])>0:
            # error["text"]= "l'utilisateur deja existe "
            # showerror(title = "Error", message = "l'utilisateur existe")
            print('existe')
            import subprocess
            window.destroy()
            subprocess.call("Categorie.py", shell=True)
        elif(Email=='' or password==''):
            messagebox.showinfo("Erreur", "Veuillez remplire les champs obligatoires")

        else:
            showerror(title = "Error", message = "l'utilisateur n'existe pas")
            # cursor.execute("INSERT INTO users(userName,Email,password)VALUES(?,?,?)",(userName,Email,password))
            # db.commit()
            # error["text"]="Votre compte a ete ajoute "
            # entry2.delete(0, 'end')
            # entry1.delete(0, 'end')
            # entry0.delete(0, 'end')
        

def Registration():
    print("clicked")
    import subprocess
    window.destroy()
    subprocess.call("C:/Users/YASSIR/Desktop/prj/version2/All_Files/Registration.py", shell=True)
    
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

background_img = PhotoImage(file = f"backgroundConn.png")
background = canvas.create_image(
    591.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Conn.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Menu,
    relief = "flat")

b0.place(
    x = 557, y = 459,
    width = 430,
    height = 56)

img1 = PhotoImage(file = f"img1Conn.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = Registration,
    relief = "flat")

b1.place(
    x = 652, y = 528,
    width = 259,
    height = 20)

entry0_img = PhotoImage(file = f"img_textBox0Conn.png")
entry0_bg = canvas.create_image(
    769.5, 362.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#fdffff",
    font = ('arial',11,'normal'),
    highlightthickness = 0,
    show='*')
# entry0.insert(END,'0')

entry0.place(
    x = 595.0, y = 339,
    width = 349.0,
    height = 44)

entry1_img = PhotoImage(file = f"img_textBox1Conn.png")
entry1_bg = canvas.create_image(
    769.5, 255.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    font = ('arial',11,'normal'),
    highlightthickness = 0)
# entry1.insert(END,'1')


entry1.place(
    x = 595.0, y = 232,
    width = 349.0,
    height = 44)

window.resizable(False, False)
window.mainloop()
