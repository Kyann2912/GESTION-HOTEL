from customtkinter import *
import customtkinter as Ctk
from time import strftime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import cpt


new = Ctk.CTk()
new.title("GESTION HOTEL")
new.geometry("1200x1200")

A = StringVar()
B = StringVar()
C = StringVar()
D = StringVar()
O = StringVar()


def Recherche():
    yann = O.get()

    if yann == "" :
        messagebox.showerror("Info","Veuillez entrer un Id valide")
    else:
        connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
        curseur = connexion.cursor()
        sql = "SELECT Produit ,Quantité FROM Stock WHERE Id_stock = %s"
        curseur.execute(sql,(yann,))  # la virgule , est très importante
        client = curseur.fetchone()
        if client:
            A.set(client[0])
            B.set(client[1])

        else:
            messagebox.showerror("Info","Produit Introuvable")
            connexion.commit()
            connexion.close()

def Supprimer():
    yann = O.get()

    if yann == "" :
        messagebox.showerror("Info","Veuillez entrer un Id valide")
    else:
        connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
        curseur = connexion.cursor()
        sql ="DELETE FROM Stock WHERE Id_stock = %s"
        curseur.execute(sql,(yann,))  # la virgule , est très importante
        messagebox.showinfo("Info","Produit Supprimer")
        connexion.commit()
        connexion.close()
        Effacer()


def Modifier():
    yann = O.get()

    if yann == "" :
        messagebox.showerror("Info","Veuillez entrer un Id valide")
    else:
        connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
        a = Frame3.get()
        b = Frame5.get()
        if(a=="" or b=="" ):
            messagebox.showerror("Info","Veuillez renseigner tous les champs ❌")
        else :
        

            curseur = connexion.cursor()
            sql ="Update Stock SET Produit =%s,Quantité=%s  WHERE Quantité = %s"
            valeur = (a,b,(yann,))
            curseur.execute(sql,valeur)  # la virgule , est très importante
            messagebox.showinfo("Info","Produit Modifier")
            connexion.commit()
            connexion.close()
            Effacer()


def Effacer():
    A.set("")
    B.set("")
    C.set("")
    D.set("")
    O.set("")





def Heure():
    heur = strftime("%H : %M  %S")
    var1.config(text=heur)
    var1.after(1000,Heure)
    
def Ajouter():
    import psycopg2
    import pyttsx3

    try:
        connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
        curseur = connexion.cursor()
        a = Frame3.get().strip()
        b = Frame5.get().strip()



        if(a=="" or b==""):
            messagebox.showerror("Info","Veuillez renseigner tous les champs ❌")

        else :
            sql = "INSERT INTO  Stock (Produit, Quantité) VALUES (%s, %s)"
            value = (a, b)
            curseur.execute(sql, value)

            connexion.commit()
            curseur.close()
            cpt.f +=1
            A.set("")
            B.set("")
            C.set("")
            D.set("")
            # yann = pyttsx3.init()

            # yann.say("Enregistrement du produit  réussi")
            messagebox.showinfo("Enregistrement du produit  réussi")

            # yann.runAndWait()
    except Exception as e:
        print("An error occurred:", e)

        # yann = pyttsx3.init()
        # yann.say(e)
        # yann.runAndWait()





var0 = Ctk.CTkLabel(new,text="GESTION DE STOCK", font=("Helvetica",36))
var0.place(x=430,y=20)

var1 = tk.Label(new,text="HH : MM : SS",font=("Helvetica",28),foreground="white",background="blue")
var1.place(x=1700,y=20)


Sexe = ["Masculin","Feminin"]


Heure()

ya2 = Ctk.CTkLabel(new,text="Chercher un produit (Id)",font=("Arial",30))
ya2.place(x=10,y=100)

ya3 = Ctk.CTkEntry(new,font=("Arial",30),width=400,textvariable=O)
ya3.place(x=10,y=150)



ya4 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="Entrer",fg_color="grey",command=Recherche)
ya4.place(x=370,y=100)

yann = Ctk.CTkButton(new,font=("Arial",30),width=150,text="VIDER",command=Effacer)
yann.place(x=460,y=150)

ya5 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="AJOUTER",fg_color="red",command=Ajouter)
ya5.place(x=660,y=150)

ya6 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="MODIFIER",fg_color="black",command=Modifier)
ya6.place(x=880,y=150)

ya4 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="SUPPRIMER",fg_color="orange",command=Supprimer)
ya4.place(x=1080,y=150)


Frame1 = Ctk.CTkFrame(new,width=400,height=400)
Frame1.place(x=10,y=200)

Frame2 = Ctk.CTkLabel(Frame1,text="Produit",font=("Arial",26),)
Frame2.place(x=10,y=10)

Frame3 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=A)
Frame3.place(x=10,y=50)

Frame4 = Ctk.CTkLabel(Frame1,text="Quantité",font=("Arial",26))
Frame4.place(x=10,y=100)

Frame5 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=B)
Frame5.place(x=10,y=140)

# Frame6 = Ctk.CTkLabel(Frame1,text="Contact",font=("Arial",26))
# Frame6.place(x=10,y=190)
   
# Frame7 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=C)
# Frame7.place(x=10,y=230)

# Frame8 = Ctk.CTkLabel(Frame1,text="Email",font=("Arial",26))
# Frame8.place(x=10,y=280)

# Frame9 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=D)
# Frame9.place(x=10,y=320)



style = ttk.Style()
style.configure("Treeview", font=("Arial", 14))

Affichage = ttk.Treeview(new,columns=(1,2,3),height=3,show="headings")
Affichage.place(x=650,y=330,height=620,width=1250)


Affichage.heading(1,text="Id_stock")
Affichage.heading(2,text="Produit")
Affichage.heading(3,text="Quantité")
# Affichage.heading(4,text="Contact")
# Affichage.heading(5,text="Email")


Affichage.column(1,width=10)
Affichage.column(2,width=100)
Affichage.column(3,width=100)
# Affichage.column(4,width=80)
# Affichage.column(5,width=120)

import psycopg2
connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
curseur = connexion.cursor()

curseur.execute("SELECT * FROM public.stock  ORDER BY id_stock ASC  ")

tableau = curseur.fetchall()

for valeur in tableau :
    Affichage.insert('','end',values=valeur)
connexion.close()

new.mainloop()

