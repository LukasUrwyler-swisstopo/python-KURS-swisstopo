datei = r"personen.txt"
with open(datei, "r") as lesezugriff:
    inhalt = lesezugriff.readlines()
print(inhalt)

nachnamen = []

for zeile in inhalt:
    form = zeile.strip()
    teile = form.split(" ")
    teile_sort = sorted(teile)
    # print(teile)
    nachname = teile_sort[1]
    nachnamen.append(nachname)