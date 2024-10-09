from customtkinter import *
import customtkinter as Ctk
from time import strftime
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
import psycopg2

import cpt

from tkinter import ttk

new = Ctk.CTk()
new.title("GESTION HOTEL")
new.geometry("1200x1200")


A = StringVar()
B = StringVar()
C = StringVar()
D = StringVar()
E = StringVar()
F = StringVar()
O = StringVar()

def Effacer():
    A.set("")
    B.set("")
    C.set("")
    D.set("")
    O.set("")
    E.set("")
    F.set("")


def Recherche():
    yann = O.get()

    if yann == "" :
        messagebox.showerror("Info","Veuillez entrer un Id de Reservation valide")
    else:
        connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
        curseur = connexion.cursor()
        sql = "SELECT Date_Reser ,Nre_chbre, Periode_Dbt,Periode_Fin,Nbre_Heure,Id_clt FROM Reservation WHERE Id_Reser = %s"
        curseur.execute(sql,(yann,))  # la virgule , est très importante
        reservation = curseur.fetchone()
        if reservation:
            A.set(reservation[0])
            B.set(reservation[1])
            C.set(reservation[2])
            D.set(reservation[3])
            E.set(reservation[4])
            F.set(reservation[5])

        else:
            messagebox.showerror("Info","Reservation Introuvable")
            connexion.commit()
            connexion.close()

def Supprimer():
    yann = O.get()

    if yann == "" :
        messagebox.showerror("Info","Veuillez entrer un Id de Reservation valide")

    else:
        connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
        curseur = connexion.cursor()
        sql ="DELETE FROM Reservation WHERE Id_Reser = %s"
        curseur.execute(sql,(yann,))  # la virgule , est très importante
        messagebox.showinfo("Info","Reservation Supprimer")
        connexion.commit()
        connexion.close()
        Effacer()


def Modifier():
    yann = O.get()

    if yann == "" :
        messagebox.showerror("Info","Veuillez entrer un Id de Reservation valide")
    else:
        connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
        a = A.get()
        b = B.get()
        c = C.get()
        d = D.get()
        e = E.get()
        f = F.get()


        if(a=="" or b=="" ):
            messagebox.showerror("Info","Veuillez renseigner les champs vide  ❌")
        else :
            curseur = connexion.cursor()
            sql = "Update Reservation SET  Date_Reser=%s ,Nre_chbre=%s, Periode_Dbt=%s,Periode_Fin=%s,Nbre_Heure=%s ,Id_clt=%s  WHERE Id_Reser = %s"
            valeur = (a,b,c,d,e,f,(yann,))
            curseur.execute(sql,valeur)  # la virgule , est très importante
            messagebox.showinfo("Info","Reservation Modifier")
            connexion.commit()
            connexion.close()
            Effacer()
# date_reser

    
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
        a = A.get().strip()
        b = B.get().strip()
        c = C.get().strip()
        d = D.get().strip()
        e = E.get().strip()
        f = F.get().strip()

        if(a=="" or b==""):
            messagebox.showerror("Info","Veuillez renseigner tous les champs ❌")

        else :
            sql = "INSERT INTO  Reservation (Date_Reser ,Nre_chbre, Periode_Dbt,Periode_Fin,Nbre_Heure,Id_clt) VALUES (%s, %s, %s, %s,%s,%s)"
            value = (a, b, c, d,e,f)
            curseur.execute(sql, value)

            connexion.commit()
            curseur.close()
            cpt.c += 1
            A.set("")
            B.set("")
            C.set("")
            D.set("")
            # yann = pyttsx3.init()
            messagebox.showinfo("Enregistrement de la reservation  réussi")


            # yann.say("Enregistrement de la reservation  réussi")
            # yann.runAndWait()
    except Exception as e:
        print(e)
        # yann = pyttsx3.init()
        # yann.say(e)
        # yann.runAndWait()
    Effacer()


def Heure():
    heur = strftime("%H : %M  %S")
    var1.config(text=heur)
    var1.after(1000,Heure)

sexe = ["Masculin","Feminin"]


var0 = Ctk.CTkLabel(new,text="GESTION DES RESERVATIONS", font=("Helvetica",36))
var0.place(x=430,y=20)

var1 = tk.Label(new,text="HH : MM : SS",font=("Helvetica",28),foreground="white",background="blue")
var1.place(x=1700,y=20)

Heure()

ya2 = Ctk.CTkLabel(new,text="Chercher une Reservation",font=("Arial",30))
ya2.place(x=10,y=80)

ya3 = Ctk.CTkEntry(new,font=("Arial",30),width=400,textvariable=O)
ya3.place(x=10,y=130)


ya4 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="Entrer",fg_color="grey",command=Recherche)
ya4.place(x=460,y=80)

yann = Ctk.CTkButton(new,font=("Arial",30),width=150,text="VIDER",command=Effacer)
yann.place(x=460,y=150)

ya5 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="AJOUTER",fg_color="red",command=Ajouter)
ya5.place(x=660,y=150)

ya6 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="MODIFIER",fg_color="black",command=Modifier)
ya6.place(x=880,y=150)

ya4 = Ctk.CTkButton(new,font=("Arial",30),width=150,text="SUPPRIMER",fg_color="orange",command=Supprimer)
ya4.place(x=1080,y=150)


Frame1 = Ctk.CTkFrame(new,width=400,height=470)
Frame1.place(x=10,y=180)

Frame2 = Ctk.CTkLabel(Frame1,text="Date de Réservation",font=("Arial",26))
Frame2.place(x=10,y=10)

Frame3 = DateEntry(Frame1,font=("Arial",26),height=55,textvariable=A)
Frame3.place(x=10,y=70,width=450)



Frame4 = Ctk.CTkLabel(Frame1,text="Periode_Dbt",font=("Arial",26))
Frame4.place(x=10,y=90)
   
Frame5 = DateEntry(Frame1,font=("Arial",26),height=55,textvariable=B)
Frame5.place(x=10,y=190,width=450)

Frame6 = Ctk.CTkLabel(Frame1,text="Periode_Fin",font=("Arial",26))
Frame6.place(x=10,y=160)

Frame7 = DateEntry(Frame1,font=("Arial",26),textvariable=C)
Frame7.place(x=10,y=290,width=450 ,height=55)

Frame9 = Ctk.CTkLabel(Frame1,text="Nbr_Heures",font=("Arial",26))
Frame9.place(x=10,y=240)

Frame10 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=D)
Frame10.place(x=10,y=270)

Frame11 = Ctk.CTkLabel(Frame1,text="Nbre de chambre",font=("Arial",26))
Frame11.place(x=10,y=310)

Frame12 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=E)
Frame12.place(x=10,y=340)

Frame13 = Ctk.CTkLabel(Frame1,text="Id_Client",font=("Arial",26))
Frame13.place(x=10,y=380)

Frame14 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=F)
Frame14.place(x=10,y=420)



style = ttk.Style()
style.configure("Treeview", font=("Arial", 14))

Affichage = ttk.Treeview(new,columns=(1,2,3,4,5,6,7),height=7,show="headings")
Affichage.place(x=650,y=330,height=620,width=1250)


Affichage.heading(1,text="Id_Reservation")
Affichage.heading(2,text="Date_Reser")
Affichage.heading(3,text="Periode_Dbt")
Affichage.heading(4,text="Periode_Fin")
Affichage.heading(5,text="Nbre_chbre")
Affichage.heading(6,text="Nbre_Hure")
Affichage.heading(7,text="Id_Client")



Affichage.column(1,width=10)
Affichage.column(2,width=100)
Affichage.column(3,width=100)
Affichage.column(4,width=80)
Affichage.column(5,width=100)
Affichage.column(6,width=100)
Affichage.column(7,width=100)



import psycopg2
connexion = psycopg2.connect(
            user="postgres",
            password="29122003",
            host="localhost",
            port="5432",
            database="Hotel"
        )
curseur = connexion.cursor()

curseur.execute("SELECT * FROM public.reservation  ORDER BY id_reser ASC  ")

tableau = curseur.fetchall()

for valeur in tableau :
    Affichage.insert('','end',values=valeur)
connexion.close()
  



new.mainloop()