# Datei: kreis_funktion.py
import math

def fläche(Radius):
    return (Radius * Radius) * math.pi

def umfang(Radius):
    return (Radius * 2) * math.pi

def durchmesser(Radius):
    return Radius * 2

if __name__ == "__main__":
    while True:
        try:
            Radius = float(input("Geben Sie bitte den Radius in Meter an: "))
            break
        except ValueError:
            print("Ungültige Eingabe, bitte eine Zahl eingeben.")

    print(fläche(Radius))
    print(umfang(Radius))
    print(durchmesser(Radius))