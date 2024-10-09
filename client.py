from customtkinter import *
import customtkinter as Ctk
from time import strftime
import tkinter as tk
from tkinter import ttk
from tkinter import font
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
        messagebox.showerror("Info","Veuillez entrer un email valide")
    else:
        connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
        curseur = connexion.cursor()
        sql = "SELECT Nom ,Prenoms, Contact, Email FROM Client WHERE Email = %s"
        curseur.execute(sql,(yann,))  # la virgule , est très importante
        client = curseur.fetchone()
        if client:
            A.set(client[0])
            B.set(client[1])
            C.set(client[2])
            D.set(client[3])
        else:
            messagebox.showerror("Info","Client Introuvable")
            connexion.commit()
            connexion.close()

def Supprimer():
    yann = O.get()

    if yann == "" :
        messagebox.showerror("Info","Veuillez entrer un email valide")
    else:
        connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
        curseur = connexion.cursor()
        sql ="DELETE FROM Client WHERE Email = %s"
        curseur.execute(sql,(yann,))  # la virgule , est très importante
        messagebox.showinfo("Info","Client Supprimer")
        connexion.commit()
        connexion.close()
        Effacer()


def Modifier():
    yann = O.get()

    if yann == "" :
        messagebox.showerror("Info","Veuillez entrer un email valide")
    else:
        connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
        if(a=="" or b=="" or c=="" or d==""):
            messagebox.showerror("Info","Veuillez renseigner tous les champs ❌")
        else :
            a = Frame3.get()
            b = Frame5.get()
            c = Frame7.get()
            d = Frame9.get()
            curseur = connexion.cursor()
            sql ="Update Client SET Nom =%s,Prenoms=%s,Contact=%s,Email=%s WHERE Email = %s"
            valeur = (a,b,c,d,(yann,))
            curseur.execute(sql,valeur)  # la virgule , est très importante
            messagebox.showinfo("Info","Client Modifier")
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
        c = Frame7.get().strip()
        d = Frame9.get().strip()

        if(a=="" or b=="" or c=="" or d==""):
            messagebox.showerror("Info","Veuillez renseigner tous les champs ❌")

        else :
            sql = "INSERT INTO  Client (Nom, Prenoms,Contact, Email) VALUES (%s, %s, %s, %s)"
            value = (a, b, c, d)
            curseur.execute(sql, value)

            connexion.commit()
            curseur.close()
            A.set("")
            B.set("")
            C.set("")
            D.set("")
            yann = pyttsx3.init()

            yann.say("Enregistrement du client  réussi")
            yann.runAndWait()
            cpt.a += 1

    except Exception as e:
        print("An error occurred:", e)
        yann = pyttsx3.init()
        yann.say(e)
        yann.runAndWait()





var0 = Ctk.CTkLabel(new,text="GESTION DES CLIENTS", font=("Helvetica",36))
var0.place(x=430,y=20)

var1 = tk.Label(new,text="HH : MM : SS",font=("Helvetica",28),foreground="white",background="blue")
var1.place(x=1700,y=20)


Sexe = ["Masculin","Feminin"]


Heure()

ya2 = Ctk.CTkLabel(new,text="Chercher un client (Email)",font=("Arial",30))
ya2.place(x=10,y=100)

ya3 = Ctk.CTkEntry(new,font=("Arial",30),width=400,textvariable=O)
ya3.place(x=10,y=150)



ya4 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="Entrer",fg_color="grey",command=Recherche)
ya4.place(x=370,y=100)

cpt = Ctk.CTkButton(new,font=("Arial",30),width=150,text="VIDER",command=Effacer)
cpt.place(x=460,y=150)

ya5 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="AJOUTER",fg_color="red",command=Ajouter)
ya5.place(x=660,y=150)

ya6 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="MODIFIER",fg_color="black",command=Modifier)
ya6.place(x=880,y=150)

ya4 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="SUPPRIMER",fg_color="orange",command=Supprimer)
ya4.place(x=1080,y=150)


Frame1 = Ctk.CTkFrame(new,width=400,height=450)
Frame1.place(x=10,y=200)

Frame2 = Ctk.CTkLabel(Frame1,text="Nom",font=("Arial",26),)
Frame2.place(x=10,y=10)

Frame3 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=A)
Frame3.place(x=10,y=50)

Frame4 = Ctk.CTkLabel(Frame1,text="Prenom",font=("Arial",26))
Frame4.place(x=10,y=100)

Frame5 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=B)
Frame5.place(x=10,y=140)

Frame6 = Ctk.CTkLabel(Frame1,text="Contact",font=("Arial",26))
Frame6.place(x=10,y=190)
   
Frame7 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=C)
Frame7.place(x=10,y=230)

Frame8 = Ctk.CTkLabel(Frame1,text="Email",font=("Arial",26))
Frame8.place(x=10,y=280)

Frame9 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=D)
Frame9.place(x=10,y=320)



style = ttk.Style()
style.configure("Treeview", font=("Arial", 14))

Affichage = ttk.Treeview(new,columns=(1,2,3,4,5),height=5,show="headings")
Affichage.place(x=650,y=330,height=620,width=1250)


Affichage.heading(1,text="Id_client")
Affichage.heading(2,text="Nom")
Affichage.heading(3,text="Prenoms")
Affichage.heading(4,text="Contact")
Affichage.heading(5,text="Email")


Affichage.column(1,width=10)
Affichage.column(2,width=100)
Affichage.column(3,width=100)
Affichage.column(4,width=80)
Affichage.column(5,width=120)

import psycopg2
connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
curseur = connexion.cursor()

curseur.execute("SELECT * FROM public.client  ORDER BY id_clt ASC  ")

tableau = curseur.fetchall()

for valeur in tableau :
    Affichage.insert('','end',values=valeur)
connexion.close()

new.mainloop()

