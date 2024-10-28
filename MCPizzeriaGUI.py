# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
# McPizzerio
#
# Vul hier jullie namen in:
# Lukas Hamstra
# Lukas Hamstra
# en Lukas Hamstra


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------


### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

labelIntro = Label(venster, text="Welkom!")
labelIntro.grid(row=0, column=0, sticky="W")

labelIntro = Label(venster, text="Klantnaam:")
labelIntro.grid(row=1, column=0, sticky="W")

ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

labelIntro = Label(venster, text="Klantnummer:")
labelIntro.grid(row=2, column=0, sticky="W")

invoerveldKlantNr = Entry(venster, state="disabled")
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

knopSluit = Button(venster, text="Sluiten", width=12, command=venster.destroy)
knopSluit.grid(row=17, column=4)

#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
