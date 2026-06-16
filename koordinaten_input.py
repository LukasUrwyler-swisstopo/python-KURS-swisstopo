Schweiz = [
    {"X_min": 2480000, "Y_min": 1070000},
    {"X_max": 2840000, "Y_max": 1300000}
]

X = float(input("Bitte geben Sie die Koordinate (LV95) 'X' ein "))
Y = float(input("Bitte geben Sie die Koordinate (LV95) 'Y' ein "))

print(f"die Koordinaten sind E {X} / N {Y:}")

if X >= Schweiz[0]["X_min"] and Y >= Schweiz[0]["Y_min"] and X <= Schweiz[1]["X_max"] and Y <= Schweiz[1]["Y_max"]:
    print(f"Punkt {X}, {Y} liegt innerhalb der Schweiz")