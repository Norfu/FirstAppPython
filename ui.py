from cgitb import text
from tkinter import *
from turtle import right
import webbrowser
import services
from classes import User




maFenetre = Tk()
 
#screen
maFenetre.geometry("1280x720")
maFenetre.title("Application Sante de Quentin & Berenice")
mainmenu = Menu(maFenetre)

#label
l1 = Label(text="Bienvenue dans l'application de Sante", bg='green')
l1.pack(pady=150)

if services.UserAlreadyExist():
    #form
    form_frame = Frame(maFenetre)
    form_frame.pack()

    
    #input field
    Label(form_frame, text="Nom").grid(row=0, column=0)
    lastname_entry = Entry(form_frame)
    lastname_entry.grid(row=0, column=1)

    Label(form_frame, text="Prénom").grid(row=1, column=0)
    firstname_entry =Entry(form_frame)
    firstname_entry.grid(row=1, column=1)
    
    Label(form_frame, text="Poids").grid(row=2, column=0)
    weight_entry =Entry(form_frame)
    weight_entry.grid(row=2, column=1)
    
    Label(form_frame, text="Taille").grid(row=3, column=0)
    height_entry =Entry(form_frame)
    height_entry.grid(row=3, column=1)
    
    Label(form_frame, text="Genre").grid(row=4, column=0)
    gender_entry =Entry(form_frame)
    gender_entry.grid(row=4, column=1)

    
  
    # Create the submit button
    submit_button = Button(form_frame, text="Submit", command=lambda :
        services.CreateUser(User(firstname_entry.get(),lastname_entry.get(),weight_entry.get(),height_entry.get(),gender_entry.get())))
    submit_button.grid(row=5, column=0, columnspan=2)
    
else:
    None
        
    
#def
def youtube():
    webbrowser.open_new("https://www.youtube.com/watch?v=8nYUFJIuIpg")

def exit():
    quit()

def text():
    l1 = Label(text="blablabla", )
    l1.pack()

#Button
bExit = Button(maFenetre , text = "Quitter cette application", command=(exit))
bYoutube = Button(maFenetre , text = "Regarder sur Youtube", command=(youtube))
 
# Placer le bouton sur la fenêtre
bExit.pack()
bYoutube.pack() 

#Menu
first = Menu(mainmenu)
first.add_radiobutton(label = "Carotte", command=(text))
first.add_radiobutton(label = "Poireau", command=(text))
first.add_radiobutton(label = "Navet", command=(text))
first.add_radiobutton(label = "Pomme", command=(text))
first.add_radiobutton(label = "Tomate", command=(text))

#Mainmenu
mainmenu.add_cascade(label="Aliments", menu=first)


#Loop
maFenetre.config(menu=mainmenu)
maFenetre.mainloop()
