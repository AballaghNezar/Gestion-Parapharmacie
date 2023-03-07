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

cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, userName text NOT NULL, Email text NOT NULL, password text NOT NULL); """)
def login():
    # exec(open("C:/Users/aball/Desktop/test5 - Copie/window.py").read())
    # os.system("C:/Users/aball/Desktop/test5 - Copie/window.py")
    import subprocess
    window.destroy()
    subprocess.call("Connexion.py", shell=True)
    
    # import runpy
    # file_globals = runpy.run_path("C:/Users/aball/Desktop/test5 - Copie/window.py")

    #========================================
    # execfile("C:/Users/aball/Desktop/test5 - Copie/window.py")
    # root=Toplevel(window)
    # root.title("Login")
    # root.geometry("1280x720")
    # root.configure(bg=grey)
    # root.resizable(False,False)
    # root.grab_set()
    # window.withdraw()
    # btn = Button(root,text="Destry Parent",command=lambda:root.grab_set())
    # btn.place(
    # x = 555, y = 492,
    # width = 430,
    # height = 56)


def Register():

    print("Button Clicked")
    userName=entry2.get()
    Email=entry1.get()
    password=entry0.get()
    
    print(userName)
    print(Email)
    print(password)

    cursor.execute("SELECT COUNT(*) from users WHERE username = '"+ userName+"' ")
    result = cursor.fetchone()
    if int (result[0])>0:
        # error["text"]= "l'utilisateur deja existe "
        showerror(title = "Error", message = "l'utilisateur deja existe")
    else:
        if(userName!='' and Email!='' and password!='' ):
            cursor.execute("INSERT INTO users(userName,Email,password)VALUES(?,?,?)",(userName,Email,password))
            db.commit()
            error["text"]="Votre compte a ete ajoute "
            entry2.delete(0, 'end')
            entry1.delete(0, 'end')
            entry0.delete(0, 'end')
        else:
            messagebox.showinfo("Erreur", "Veuillez remplire les champs obligatoires")

        
    # logintodb(userName, password)
    # try:
    #     file=open('datasheet.txt','r+')
    #     d=file.read()
    #     r=ast.literal_eval(d)

    #     dict2={userName:password}
    #     r.update(dict2)
    #     file.truncate(0)
    #     file.clode()

    #     file=open('datasheet.txt','w')
    #     w=file.write(str(r))

    #     messagebox.showinfo('signUp','Succesfully sign up')
    # except:
    #     file=open('datasheet.txt','w')
    #     pp=str({userName:password})
    #     file.write(pp)
    #     file.close()
    # -------------------------------------------------
    # myInfo= userName + Email + password 
    # text_file = open('Users.txt','r+')
    # Profile= text_file.read()
    # myInfo.insert(END, Profile)
    # Profile.close()
    # -----------------------------------------------
# def logintodb(user, passw):
     
#     # If password is enetered by the
#     # user
#     if passw:
#         db = mysql.connector.connect(host ="localhost",
#                                      user = user,
#                                      password = passw,
#                                      db ="College")
#         cursor = db.cursor()
         
#     # If no password is enetered by the
#     # user
#     else:
#         db = mysql.connector.connect(host ="localhost",
#                                      user = user,
#                                      db ="College")
#         cursor = db.cursor()
         
#     # A Table in the database
#     savequery = "select * from STUDENT"
     
#     try:
#         cursor.execute(savequery)
#         myresult = cursor.fetchall()
         
#         # Printing the result of the
#         # query
#         for x in myresult:
#             print(x)
#         print("Query Executed successfully")
         
#     except:
#         db.rollback()
#         print("Error occured")


    


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
#
error = Message(text="", width=160)
error.place(x = 30,y =10)
error.config(padx=0)
#
# label

#
background_img = PhotoImage(file = f"backgroundReg.png")
background = canvas.create_image(
    591.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = f"img0Reg.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = Register,
    # cursor=circle,
    relief = "flat")

b0.place(
    x = 555, y = 492,
    width = 430,
    height = 56)

img1 = PhotoImage(file = f"img1Reg.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    # cursor=cursor,
    # command = btn_clicked,
    relief = "flat",
    # command=window.destroy,
    command=login)

b1.place(
    x = 639, y = 557,
    width = 261,
    height = 20)

entry2_img = PhotoImage(file = f"img_textBox2Reg.png")
entry2_bg = canvas.create_image(
    769.5, 233.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0,
    font = ('arial',11,'normal'))
entry2.focus()
entry2.place(
    x = 595.0, y = 210,
    width = 349.0,
    height = 44)

entry1_img = PhotoImage(file = f"img_textBox1Reg.png")
entry1_bg = canvas.create_image(
    769.5, 327.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0,
    font = ('arial',11,'normal'))

entry1.place(
    x = 595.0, y = 304,
    width = 349.0,
    height = 44)


entry0_img = PhotoImage(file = f"img_textBox0Reg.png")
entry0_bg = canvas.create_image(
    769.5, 421.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#fdffff",
    highlightthickness = 0,
    text = 'Password',
    # textvariable = "Email",
    font = ('arial',11,'normal'),
    show="*")


entry0.place(
    x = 595.0, y = 398,
    width = 349.0,
    height = 44)




window.resizable(False, False)
window.mainloop()
