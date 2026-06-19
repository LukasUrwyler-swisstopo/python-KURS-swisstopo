import random

def eigene_zahlen():
    zahlen = set()
    while len(zahlen) < 6:
        try:
            zahl = int(input(f"Zahl {len(zahlen)+1}/6 (1-42): "))
            if 1 <= zahl <= 42:
                zahlen.add(zahl)
            else:
                print("Zahl muss zwischen 1 und 42 sein.")
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")
    return zahlen

def zufallszahlen():
    zahlen = set()
    while len(zahlen) < 6:
        zahlen.add(random.randint(1, 42))
    return zahlen

set_liste = eigene_zahlen()
lotto_zahlen = zufallszahlen()

print(f"Dein Tipp:       {sorted(set_liste)}")
print(f"Gezogene Zahlen: {sorted(lotto_zahlen)}")

if lotto_zahlen == set_liste:
    print("Du hast das Lotto gewonnen!")
else:
    treffer = set_liste & lotto_zahlen
    print(f"Treffer: {len(treffer)} → {sorted(treffer)}")