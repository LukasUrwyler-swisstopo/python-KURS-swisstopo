import math

Radius = float(input("geben Sie bitte den Radius in meter an "))

fläche = (Radius * Radius) * math.pi
umfang = (Radius *2) * math.pi
print(f"der Durchmesser des Kreises ist {Radius * 2} m")
print(f"die Fläche des Kreises ist {fläche} m2")
print(f"der Umfang des Kreises ist {umfang} m")

                 
            