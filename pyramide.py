# for-Schleifen
hoehe = 15

for i in range(hoehe):
    liste = "X" * i
    print(liste)

for u in range(hoehe):
    liste2 = " " * (hoehe - u) + "X" * u
    print(liste2)

for j in range(hoehe):
    liste3 = " " * (hoehe - j) + "X" * (2 * j - 1)
    print(liste3)

