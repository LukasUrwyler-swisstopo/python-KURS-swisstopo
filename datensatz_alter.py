import time

eingabe = input("Bitte gib das Aufnahmedatum eines Datensatzes (Format: TT.MM.JJJJ) ")
aktuelle_zeit = time.time()

datum = time.strptime(eingabe, "%d.%m.%Y")
sekunden = time.mktime(datum)
differenz = aktuelle_zeit - sekunden

if differenz >= 31560000:
    print("Achtung: Datensatz ist älter als 1 Jahr,  bitte auf Aktualität prüfen.")
else:
    print("die Daten sind aktuell ")