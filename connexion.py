import customtkinter as Ctk
from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


fenetre = Ctk.CTk()

fenetre.title("CONNEXION")
fenetre.geometry("1200x1200")

A = Ctk.StringVar()
B = Ctk.StringVar()


def Connnexion(Email,password):

    Email = var4.get().strip()
    password= var6.get().strip()
    if Email==" " or password=="":
        messagebox.showinfo("Info","Veuillez renseingner tous les champs ")
    else:
        import psycopg2
        connexion = psycopg2.connect(
        user="postgres",
        password="29122003",
        host="localhost",
        port="5432",
        database="Hotel"
        )
        curseur = connexion.cursor()
        curseur.execute("SELECT * FROM \"administrateur\" WHERE Email = %s AND password = %s", (Email, password))

        resultat = curseur.fetchone()
        connexion.commit()
        return resultat


def Authentifier():

    Email = var4.get()
    password = var6.get()

    resultat = Connnexion(Email,password)

    if resultat:
        messagebox.showinfo("Succes","Bienvenue")
        A.set("")
        B.set("")
        fenetre.destroy()
        import subprocess
        subprocess.run(["python","C:/Users/kouakou/Documents/GESTION-HOTEL/tableau.py"])
    else : 
        messagebox.showerror("Erreur","Email ou Mot de Passe incorrect ")
 
var0 = Label(fenetre,text="YANN HOTEL" , font=("Helvetica",34),foreground="blue")
var0.place(x=1100,y=20)

# Charger l'image avec Pillow
original_image = Image.open("hotel.jpg")

# Redimensionner l'image
new_size = (600, 980)  # Taille souhaitée (largeur, hauteur)
resized_image = original_image.resize(new_size)

# Convertir l'image redimensionnée en format compatible Tkinter
tk_image = ImageTk.PhotoImage(resized_image)

var1 = Label(fenetre , image= tk_image)
var1.place(x=0,y=0)

var2  = Ctk.CTkLabel(fenetre , font=("Helvetica",34),text="Connectez vous !♻️")
var2.place(x=730,y=80)

var3 = Ctk.CTkLabel(fenetre,text="Email",font=("Helvetica",34))
var3.place(x=500,y=200)

var4 = Ctk.CTkEntry(fenetre,font=("Helvetica",28),width=400,textvariable=A)
var4.place(x=680,y=200)

var5 = Ctk.CTkLabel(fenetre,text="Mot_Passe",font=("Helvetica",34))
var5.place(x=500,y=280)

var6 = Ctk.CTkEntry(fenetre,font=("Helvetica",28),width=400,show="*",textvariable=B)
var6.place(x=680,y=280)

var7 = Ctk.CTkButton(fenetre,text="CONNEXION",font=("Helvetica",28),fg_color="green",command=Authentifier)
var7.place(x=770,y=350)



fenetre.mainloop()