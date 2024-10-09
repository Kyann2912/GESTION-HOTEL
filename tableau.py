from customtkinter import *
import customtkinter as Ctk
from time import strftime
import tkinter as tk
from PIL import Image, ImageTk
import io
import cpt
fenetre = Ctk.CTk()
fenetre.title("GESTION HOTEL")
fenetre.geometry("1200x1200")
fenetre.configure(fg_color="blue")

def Deconnexion():
    import subprocess
    fenetre.destroy()
    subprocess.run(["python","connexion.py"])

def Reservation():
    import subprocess
    subprocess.run(["python","reservation.py"])

def Depense():
    import subprocess
    subprocess.run(["python","depense.py"])

def Stock():
    import subprocess
    subprocess.run(["python","stock.py"])

def Heure():
    heur = strftime("%H : %M  %S")
    var1.config(text=heur)
    var1.after(1000,Heure)

def Personnel():
    import subprocess
    subprocess.run(["python","personnel.py"])

def Client():
    import subprocess
    subprocess.run(["python","client.py"])

def Occupation():
    import subprocess
    subprocess.run(["python","occupation.py"])


var0 = Ctk.CTkLabel(fenetre,text="Bienvenue : Admin", font=("Helvetica",28))
var0.place(x=500,y=20)

var1 = tk.Label(fenetre,text="HH : MM : SS",font=("Helvetica",28),foreground="white",background="blue")
var1.place(x=1700,y=20)

Heure()

var2 = Ctk.CTkLabel(fenetre,text="DASHBOARD",font=("Helvetica",28))
var2.place(x=80,y=200)

var3 = Ctk.CTkButton(fenetre,text="GESTION DES RESERVATIONS",font=("Arial",28),fg_color="blue",command=Reservation)
var3.place(x=5,y=255)

var4 = Ctk.CTkButton(fenetre,text="GESTION DE STOCK",font=("Arial",28),fg_color="blue",command=Stock)
var4.place(x=5,y=315)

var5 = Ctk.CTkButton(fenetre,text="GESTION DU PERSONNEL",font=("Arial",28),fg_color="blue",command=Personnel)
var5.place(x=5,y=375)

var6 = Ctk.CTkButton(fenetre,text="GESTION DES DEPENSES",font=("Arial",28),fg_color="blue",command=Depense)
var6.place(x=5,y=435)

var6 = Ctk.CTkButton(fenetre,text="GESTION DES OCCUPATIONS",font=("Arial",28),fg_color="blue",command=Occupation)
var6.place(x=5,y=495)

var7 = Ctk.CTkButton(fenetre,text="GESTION DES CLIENTS",font=("Arial",28),fg_color="blue",command=Client)
var7.place(x=5,y=550)

var7 = Ctk.CTkButton(fenetre,text="DECONNEXION",font=("Arial",28),fg_color="white",text_color="red",command=Deconnexion)
var7.place(x=5,y=600)



##Création du graphique
x1 = cpt.a
x2 = cpt.b
x3 = cpt.c
x4 = cpt.d
x5 = cpt.e
x6 = cpt.f



import matplotlib.pyplot as plt
labels = ["Client","Personnel", "Réservation", "Depenses", "Occupations", "Stock"]
sizes = [x1,x2,x3,x4,x5,x6]

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(sizes, labels=labels, shadow=True)
ax.set_title("Statistique")



#Stockons notre image
zone = io.BytesIO()
plt.savefig(zone, format='png')
zone.seek(0)

# Chargement de l'image avec PIL et conversion en image Tkinter
img = Image.open(zone)
photo = ImageTk.PhotoImage(img)

# Création du label pour afficher l'image du graphique
var8 = tk.Label(fenetre, image=photo)
var8.place(x=1100, y=320)  

# Charger l'image avec Pillow
original_image = Image.open("hotel.jpg")

# Redimensionner l'image
new_size = (600, 250)  # Taille souhaitée (largeur, hauteur)
resized_image = original_image.resize(new_size)

# Convertir l'image redimensionnée en format compatible Tkinter
tk_image = ImageTk.PhotoImage(resized_image)

var9 = tk.Label(fenetre , image= tk_image)
var9.place(x=0,y=0)

fenetre.mainloop()
