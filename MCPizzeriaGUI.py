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

def zoekKlant():
    #haal de ingevoerde_klantnaam op uit het invoerveld en gebruik dit om met SQL de klant in database te vinden
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    print(gevonden_klanten) # om te testen
    invoerveldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
    invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
    for rij in gevonden_klanten: #voor elke rij dat de query oplevert
        #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
        invoerveldKlantNr.insert(END, rij[0]) 
        #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
        invoerveldKlantnaam.insert(END, rij[1]) 

def toonMenuInListbox():
    listboxMenu.delete(0, END) #maak de listbox leeg
    listboxMenu.insert(0, "ID Gerecht Prijs")
    pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
    for regel in pizza_tabel:
        listboxMenu.insert(END, regel) #voeg elke regel uit resultaat in listboxMenu

### functie voor het selecteren van een rij uit de listbox en deze in een andere veld te plaatsen
def haalGeselecteerdeRijOp(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxMenu.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst) 
    #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerveldGeselecteerdePizza.delete(0, END) 
    #zet tekst in veld
    invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst[1]) 

#voeg de bestelling van klant met gekozen pizza en aantal toe 
#in de winkelwagentabel
#en toon de bestelling in de listbox op het scherm
def voegToeAanWinkelWagen():
    klantNr = invoerveldKlantNr.get()
    gerechtID = ingevoerde_pizza.get()
    aantal = aantalGekozen.get()
    MCPizzeriaSQL.voegToeAanWinkelWagen(klantNr, gerechtID, aantal )
    winkelwagen_tabel = MCPizzeriaSQL.vraagOpGegevensWinkelWagenTabel()
    listboxWinkelwagen.delete(0, END) #listbox eerst even leeg maken
    for regel in winkelwagen_tabel:
        listboxWinkelwagen.insert(END, regel)


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

invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

knopZoekKlantnaam = Button(venster, text="Zoek klant", width=12, command=zoekKlant)
knopZoekKlantnaam.grid(row=1, column=4)

knopToonPizzas = Button(venster, text="Toon alle pizza’s", width=12, command=toonMenuInListbox)
knopToonPizzas.grid(row=3, column=4)

labelAllePizzas = Label(venster, text="Menu:")
labelAllePizzas.grid(row=3, column=0, sticky="NW")

listboxMenu = Listbox(venster, height=6, width=50)
listboxMenu.grid(row=3, column=1, rowspan=5, columnspan=2, sticky="W")
listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

scrollbarlistbox = Scrollbar(venster)
scrollbarlistbox.grid(row=1, column=2, rowspan=6, sticky="E")
listboxMenu.config(yscrollcommand=scrollbarlistbox.set)
scrollbarlistbox.config(command=listboxMenu.yview)

labelGekozenPizza = Label(venster, text="Gekozen pizza:")
labelGekozenPizza.grid(row=8, column=0, sticky="W")

ingevoerde_pizza= StringVar()
invoerveldGeselecteerdePizza = Entry(venster, textvariable=ingevoerde_pizza)
invoerveldGeselecteerdePizza.grid(row=8, column=1, sticky="W")

labelHoeveelheidPizza = Label(venster, text="Aantal:")
labelHoeveelheidPizza.grid(row=9, column=0, sticky="W")

aantalGekozen = IntVar()
aantalGekozen.set(1)
optionMenuPizzaHoeveelheid = OptionMenu(venster, aantalGekozen, 1, 2, 3)
optionMenuPizzaHoeveelheid.grid(row=9, column=1, sticky="W")

knopVoegToe = Button(venster, text="Voeg toe", width=12, command=voegToeAanWinkelWagen)
knopVoegToe.grid(row=10, column=4, sticky="NW")

labelWinkelwagen = Label(venster, text="Winkelmand:")
labelWinkelwagen.grid(row=10, column=0, sticky="NW")

listboxWinkelwagen = Listbox(venster, height=6, width=50)
listboxWinkelwagen.grid(row=10, column=1, rowspan=6, columnspan=2, sticky="W")

knopSluit = Button(venster, text="Sluiten", width=12, command=venster.destroy)
knopSluit.grid(row=17, column=4)

#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
