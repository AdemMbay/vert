
from tkinter import *
from math import *


class Fenetre(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculatrice Tkinter")

        # Initialisation :
        self.textvar = StringVar()
        self.operation = ""

        # Affichage :
        self.outpout = Entry(width=15, textvar=self.textvar, bg="powder blue", borderwidth=10,
                             font=("Courier New", 35, 'bold'))
        self.outpout.grid(row=1, column=1, columnspan=5)
        # Placement du curseur sur la fenetre d'entrée
        self.outpout.focus()

        # Clear :
        self.boutonclear = Button(padx=14, pady=14, text="C", font=("Courier New", 12, 'bold'),
                                  command=self.clearbutton, background="light gray", borderwidth=10)
        self.boutonclear.grid(row=6, column=3, columnspan=1)

        # Chiffres :
        self.bouton0 = Button(padx=14, pady=14, text="0", font=("Courier New", 12, 'bold'),
                              command=lambda: self.clickbutton(0), background="light gray", borderwidth=4, fg="black")
        self.bouton0.grid(row=5, column=2, columnspan=1)

        self.bouton1 = Button(padx=14, pady=14, text="1", font=("Courier New", 12, 'bold'),
                              command=lambda: self.clickbutton(1), background="light gray", borderwidth=4)
        self.bouton1.grid(row=4, column=3, columnspan=1)

        self.bouton2 = Button(padx=14, pady=14, text="2", font=("Courier New", 12, 'bold'),
                              command=lambda: self.clickbutton(2), background="light gray", borderwidth=4)
        self.bouton2.grid(row=4, column=2, columnspan=1)

        self.bouton3 = Button(padx=14, pady=14, text="3", font=("Courier New", 12, 'bold'),
                              command=lambda: self.clickbutton(3), background="light gray", borderwidth=4)
        self.bouton3.grid(row=4, column=1, columnspan=1)

        self.bouton4 = Button(padx=14, pady=14, text="4", font=("Courier New", 12, 'bold'),
                              command=lambda: self.clickbutton(4), background="light gray", borderwidth=4)
        self.bouton4.grid(row=3, column=1, columnspan=1)

        self.bouton5 = Button(padx=14, pady=14, text="5", font=("Courier New", 12, 'bold'),
                              command=lambda: self.clickbutton(5), background="light gray", borderwidth=4)
        self.bouton5.grid(row=3, column=2, columnspan=1)

        self.bouton6 = Button(padx=14, pady=14, text="6", font=("Courier New", 12, 'bold'),
                              command=lambda: self.clickbutton(6), background="light gray", borderwidth=4)
        self.bouton6.grid(row=3, column=3, columnspan=1)

        self.bouton7 = Button(padx=14, pady=14, text="7", font=("Courier New", 12, 'bold'),
                              command=lambda: self.clickbutton(7), background="light gray", borderwidth=4)
        self.bouton7.grid(row=2, column=1, columnspan=1)

        self.bouton8 = Button(padx=14, pady=14, text="8", font=("Courier New", 12, 'bold'),
                              command=lambda: self.clickbutton(8), background="light gray", borderwidth=4)
        self.bouton8.grid(row=2, column=2, columnspan=1)

        self.bouton9 = Button(padx=14, pady=14, text="9", font=("Courier New", 12, 'bold'),
                              command=lambda: self.clickbutton(9), background="light gray", borderwidth=4)
        self.bouton9.grid(row=2, column=3, columnspan=1)

        self.boutonpi = Button(padx=14, pady=14, text="π", font=("Courier New", 12, 'bold'),
                               command=lambda: self.clickbutton("pi"), background="light gray", borderwidth=4)
        self.boutonpi.grid(row=6, column=1, columnspan=1)
