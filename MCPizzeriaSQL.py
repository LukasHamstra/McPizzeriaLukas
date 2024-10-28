# Vul hier de naam van je programma in:
# McPizzerio
#
# Vul hier jullie namen in:
# Lukas Hamstra
# Lukas Hamstra
# en Lukas Hamstra


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3, os

# os.remove("MCPizzeria.db") ## Remove DB file so I don't have to manually everytime.
os.system('cls') ## Clean console.

with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen
 

### ---------  Functie definities  -----------------

def maakTabellenAan():
 # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
 cursor.execute("""
                CREATE TABLE IF NOT EXISTS tbl_pizzas(
                gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
                gerechtNaam TEXT NOT NULL,
                gerechtPrijs REAL NOT NULL);""")
 print("Tabel 'tbl_pizzas' aangemaakt.")

 cursor.execute("""
                CREATE TABLE IF NOT EXISTS tbl_klanten(
                klantNr INTEGER PRIMARY KEY AUTOINCREMENT,
                klantAchternaam TEXT);""")
 print("Tabel 'tbl_klanten' aangemaakt.")

def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam) #SQL om ALLE gegevens te halen
    opgehaalde_gegevens = cursor.fetchall() #sla gegevens op in een variabele
    print("Tabel " + tabel_naam + ":", opgehaalde_gegevens) #druk gegevens af

def voegPizzaToe(naam_nieuwe_pizza, prijs_nieuwe_pizza):
    cursor.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?, ? )", (naam_nieuwe_pizza, prijs_nieuwe_pizza))
    db.commit() #gegevens naar de database wegschrijven
    print("Pizzas toegevoegd:", naam_nieuwe_pizza)

def verwijderPizza(gerechtNaam):
    cursor.execute("DELETE FROM tbl_pizzas WHERE gerechtNaam = ?", (gerechtNaam,))
    print("Gerecht verwijderd uit 'tbl_pizzas':", gerechtNaam )
    db.commit() #gegevens naar de database wegschrijven

def pasGerechtAan(gerechtID, nieuweGerechtNaam, nieuwePrijs):
    cursor.execute("UPDATE tbl_pizzas SET gerechtNaam = ?, gerechtPrijs = ? WHERE gerechtID = ?", (nieuweGerechtNaam, nieuwePrijs, gerechtID ))
    db.commit() #gegevens naar de database wegschrijven
    print("Gerecht aangepast")

def voegKlantToe(naam_nieuwe_klant):
    cursor.execute("INSERT INTO tbl_klanten VALUES(NULL, ?)", (naam_nieuwe_klant,))
    db.commit()
    print("Klant toegevoegd:", naam_nieuwe_klant)



### --------- Hoofdprogramma  ---------------
# maakTabellenAan()
# voegPizzaToe("Margarita", 9.50)
# voegPizzaToe("Hawaii", 12.25)
# voegPizzaToe("Salami", 10.00)
# verwijderPizza("Hawaii")
# pasGerechtAan(3, "Salamiiii", 19.25)
# printTabel("tbl_pizzas")

# voegKlantToe("Janssen")
# voegKlantToe("Pietersen")   
# printTabel("tbl_klanten")
