import math

def kreisfunktion1(Radius):
    fläche = (Radius * Radius) * math.pi
    umfang = (Radius * 2) * math.pi
    print(f"der Durchmesser des Kreises ist {Radius * 2} m")
    print(f"die Fläche des Kreises ist {fläche:.2f} m2")
    print(f"der Umfang des Kreises ist {umfang:.2f} m")

while True:
    try:
        Radius = float(input("Geben Sie bitte den Radius in Meter an: "))
        break
    except ValueError:
        print("Ungültige Eingabe, bitte eine Zahl eingeben.")

kreisfunktion1(Radius)