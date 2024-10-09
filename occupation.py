from customtkinter import *
import customtkinter as Ctk
from time import strftime
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
import cpt



new = Ctk.CTk()
new.title("GESTION HOTEL")
new.geometry("1200x1200")

A = StringVar()
B = StringVar()
C = StringVar()
D = StringVar()
E = StringVar()
F = StringVar()
G = StringVar()
H = StringVar()
I = StringVar()
J = IntVar()
K = IntVar()
L = IntVar()
M = IntVar()
yann = IntVar()




def IMPRIMER():
    import os
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A8
    from reportlab.lib.units import cm
    # Le nom et prénom de l'apprenant
    a = Frame3.get().strip()
    b = Frame5.get().strip()
    
    # nom = "Recu.pdf"


    
    # Nom du fichier
    nom_fichier = f"{a}_{b}.pdf".replace(' ', '_').replace('/', '_').replace('\\', '_')

    
    # Chemins du dossier
    dossier_principal = "C:/Users/kouakou/Documents/GESTION-HOTEL/RECU"  # Changez ce chemin en celui que vous voulez pour le stockage principal
    chemin_fichier_principal = os.path.join(dossier_principal, nom_fichier)



    # Créez le PDF
    can = Canvas(chemin_fichier_principal, pagesize=A8)
    a = Frame3.get().strip()
    b = Frame5.get().strip()
    c = Frame7.get().strip()
    d = Frame13.get()
    e = Frame9.get().strip()

    i = Frame70.get().strip()
    j = str(Frame72.get().strip())
    k = str(Frame78.get().strip())
    l = str(Frame75.get().strip())

    franck = J.get()
    kouakou = K.get()
    ephrem = L.get()

    payer_str = int(franck) - int(ephrem)

    payer = str(payer_str)

    rendu =  int(kouakou) - int(payer)

    rdu = str(rendu)


    texte = "-------YANN HOTEL-------"
    abc1 = "Nom  "
    abc2 = "Prenoms "
    abc3 = "Contact "
    abc4 = "Date  "
    abc5 = "Nbre-Heures "
    abc6 = "Chambre "
    abc7 = "A Payer "
    abc8 = "Reduction "
    abc9= "Espèce "
    abc10= "Payer "
    abc11= "Rendu "

    msg = "Merci ! 😊😊😊"



    can.setFont("Helvetica-Bold",6)
    posOO,posFF = 1.5*cm,7*cm
    posA,posB = 0.5*cm,6.5*cm
    posC,posD = 0.5*cm,6*cm
    posE,posF=  0.5*cm,5.5*cm
    posG,posH = 0.5*cm,5*cm
    posI,posJ = 0.5*cm,4.5*cm
    posK,posL = 0.5*cm,4*cm
    posM,posN = 0.5*cm,3.5*cm
    posAA,posBB = 0.5*cm,3*cm
    posYY,posKK = 0.5*cm,2.5*cm
    posII,posOS = 0.5*cm,2*cm
    posLM,posLN = 0.5*cm,1.5*cm

    posMS,posNS = 1.5*cm,0.5*cm






    posWWA,posWWB = 2*cm,6.5*cm
    posWWC,posWWD = 2*cm,6*cm
    posWWE,posWWF = 2*cm,5.5*cm
    posWWG,posWWH = 2*cm,5*cm
    posWWI,posWWJ = 2*cm,4.5*cm
    posWWK,posWWL = 2*cm,4*cm
    posWWM,posWWN = 2*cm,3.5*cm
    posWWO,posWWP = 2*cm,3*cm
    posWWQ,posWWR = 2*cm,2.5*cm
    posWWS,posWWT = 2*cm,2*cm
    posWWU,posWWV = 2*cm,1.5*cm



    can.drawString(posOO,posFF,texte)
    can.drawString(posA,posB,abc1)
    can.drawString(posC,posD,abc2)
    can.drawString(posE,posF,abc3)
    can.drawString(posG,posH,abc4)
    can.drawString(posI,posJ,abc5)
    can.drawString(posK,posL,abc6)
    can.drawString(posM,posN,abc7)
    can.drawString(posAA,posBB,abc8)
    can.drawString(posYY,posKK,abc9)
    can.drawString(posII,posOS,abc10)
    can.drawString(posLM,posLN,abc11)
    can.drawString(posMS,posNS,msg)


    can.drawString(posWWA,posWWB,a)
    can.drawString(posWWC,posWWD,b)
    can.drawString(posWWE,posWWF,c)
    can.drawString(posWWG,posWWH,d)
    can.drawString(posWWI,posWWJ,i)
    can.drawString(posWWK,posWWL,e)
    can.drawString(posWWM,posWWN,j)
    can.drawString(posWWO,posWWP,k)
    can.drawString(posWWQ,posWWR,l)
    can.drawString(posWWS,posWWT,payer)
    can.drawString(posWWU,posWWV,rdu)


    can.save()

def Heure():
    heur = strftime("%H : %M  %S")
    var1.config(text=heur)
    var1.after(1000,Heure)

def Effacer():
    A.set("")
    B.set("")
    C.set("")
    D.set("")
    E.set("")
    F.set("")
    G.set("") 
    H.set("")
    I.set("")
    J.set("")
    K.set("")
    L.set("")
    M.set("")

def Quitter():
    import subprocess
    new.destroy()
    subprocess.run(['python','tableau.py'])

    
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
        a = Frame3.get().strip()
        b = Frame5.get().strip()
        c = Frame7.get().strip()
        d = Frame9.get().strip()
        e = E.get().strip()
        f = F.get().strip()
        g = G.get().strip()
        h = Frame70.get().strip()
        i = Frame77.get().strip()
        j = str(Frame72.get().strip())
        k = str(Frame75.get().strip())
        l = str(Frame78.get().strip())
        yann = int(j)- int(l)
        payer = str(yann)

        rdu = int(k) - int(payer) 

        rendu = str(rdu)

        

        if(a==""):
            messagebox.showerror("Info","Veuillez renseigner tous les champs ❌")

        else :
            curseur = connexion.cursor()
            sql = "INSERT INTO  Occupation (Nom, Prenoms,Contact,Numero_chbre,Date,Periode_Dbt,Periode_Fin,Nbre_Heure,Nbre_chbre,A_payer,Espece,Reduction,Rendu,Payer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
            value = (a, b, c, d,e,f,g,h,i,j,k,l,rendu,payer)
            curseur.execute(sql, value)

            connexion.commit()
            curseur.close()
            cpt.e +=1
            IMPRIMER()

            # yann = pyttsx3.init()
            messagebox.showinfo("Enregistrement d'occupation  réussi")
            # yann.say("Enregistrement d'occupation  réussi")
            # yann.runAndWait()
    except Exception as e:
        print("An error occurred:", e)
        yann = pyttsx3.init()
        yann.say(e)
        yann.runAndWait()





var0 = Ctk.CTkLabel(new,text="GESTION DES OCCUPATIONS", font=("Helvetica",36))
var0.place(x=430,y=20)

var1 = tk.Label(new,text="HH : MM : SS",font=("Helvetica",28),foreground="white",background="blue")
var1.place(x=1700,y=20)


Sexe = ["Masculin","Feminin"]


Heure()

##LES FONCTIONS





Frame1 = Ctk.CTkFrame(new,width=350,height=400)
Frame1.place(x=10,y=100)

Frame2 = Ctk.CTkLabel(Frame1,text="Nom",font=("Arial",26))
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

Frame8 = Ctk.CTkLabel(Frame1,text="Numero_chbre",font=("Arial",26))
Frame8.place(x=10,y=280)

Frame9 = Ctk.CTkEntry(Frame1,font=("Arial",26),width=300,textvariable=D)
Frame9.place(x=10,y=320)



Frame01 = Ctk.CTkFrame(new,width=350,height=400)
Frame01.place(x=410,y=100)

Frame2 = Ctk.CTkLabel(Frame01,text="Date",font=("Arial",26))
Frame2.place(x=10,y=10)

Frame13 = DateEntry(Frame01,font=("Arial",26),height=55,textvariable=E)
Frame13.place(x=10,y=70,width=450)

Frame4 = Ctk.CTkLabel(Frame01,text="Du",font=("Arial",26))
Frame4.place(x=10,y=100)

Frame14 = DateEntry(Frame01,font=("Arial",26),height=55,textvariable=F)
Frame14.place(x=10,y=200,width=450)

Frame4 = Ctk.CTkLabel(Frame01,text="Au",font=("Arial",26))
Frame4.place(x=10,y=170)

Frame30 = DateEntry(Frame01,font=("Arial",26),height=55,textvariable=G)
Frame30.place(x=10,y=310,width=450)


Frame4 = Ctk.CTkLabel(Frame01,text="Nombres Heures",font=("Arial",26))
Frame4.place(x=10,y=250)

Frame70 = Ctk.CTkEntry(Frame01,font=("Arial",26),width=300,textvariable=H)
Frame70.place(x=10,y=290)

Frame4 = Ctk.CTkLabel(Frame01,text="Nombre Chambres",font=("Arial",26))
Frame4.place(x=10,y=330)

Frame77 = Ctk.CTkEntry(Frame01,font=("Arial",26),width=300,textvariable=I)
Frame77.place(x=10,y=360)


Frame001 = Ctk.CTkFrame(new,width=1250,height=130)
Frame001.place(x=10,y=510)

Frame2 = Ctk.CTkLabel(Frame001,text="A payer",font=("Arial",26))
Frame2.place(x=10,y=10)

Frame72 = Ctk.CTkEntry(Frame001,font=("Arial",26),width=200,textvariable=J)
Frame72.place(x=120,y=10)

Frame2 = Ctk.CTkLabel(Frame001,text="Espèce",font=("Arial",26))
Frame2.place(x=10,y=80)

Frame75 = Ctk.CTkEntry(Frame001,font=("Arial",26),width=200,textvariable=K)
Frame75.place(x=120,y=80)

Frame2 = Ctk.CTkLabel(Frame001,text="Reduction",font=("Arial",26))
Frame2.place(x=340,y=10)

Frame78 = Ctk.CTkEntry(Frame001,font=("Arial",26),width=200,textvariable=L)
Frame78.place(x=470,y=10)

Frame2 = Ctk.CTkLabel(Frame001,text="Rendu",font=("Arial",26))
Frame2.place(x=340,y=80)

Frame28 = Ctk.CTkEntry(Frame001,font=("Arial",26),width=200,textvariable=M)
Frame28.place(x=470,y=80)

yann = Ctk.CTkButton(Frame001,font=("Arial",30),width=150,text="ENREGISTRER",fg_color="red",command=Ajouter)
yann.place(x=700,y=10)

ya5 = Ctk.CTkButton(Frame001,font=("Arial",30),width=150,text="VIDER",command=Effacer)
ya5.place(x=700,y=80)

ya6 = Ctk.CTkButton(Frame001,font=("Arial",30),width=150,text="QUITTER",fg_color="black",command=Quitter)
ya6.place(x=1000,y=80)

ya4 = Ctk.CTkButton(Frame001,font=("Arial",30),width=150,text="RECU",fg_color="orange",command=IMPRIMER)
ya4.place(x=1000,y=10)


Frame11 = Ctk.CTkFrame(new,width=455,height=400)
Frame11.place(x=800,y=100)

var20 = Ctk.CTkLabel(Frame11,text="Chambres Disponible",font=("Arial",26))
var20.place(x=100,y=10)


new.mainloop()