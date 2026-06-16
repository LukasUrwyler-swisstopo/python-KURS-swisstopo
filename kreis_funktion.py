import math


def fläche(Radius):
    return (Radius * Radius) * math.pi

def umfang(Radius):
    return (Radius * 2) * math.pi

def durchmesser(Radius):
    return Radius * 2

while True:
    try:
        Radius = float(input("Geben Sie bitte den Radius in Meter an: "))
        break
    except ValueError:
        print("Ungültige Eingabe, bitte eine Zahl eingeben.")

Fläche_res = fläche(Radius)
Umfang_res = umfang(Radius)
durchmesser_res = durchmesser(Radius)

print(Fläche_res)
print(Umfang_res)
print(durchmesser_res)