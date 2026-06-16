punkte = [
    {'name': 'A', 'ost': 2600100, 'nord': 1200200},
    {'name': 'B', 'ost': 2601500, 'nord': 1201000},
    {'name': 'C', 'ost': 2599800, 'nord': 1199500},
    {'name': 'D', 'ost': 2600800, 'nord': 1200600},
    {'name': 'E', 'ost': 2602000, 'nord': 1198000},
]

bbox = {'ost_min': 2600000, 'ost_max': 2601000,
        'nord_min': 1200000, 'nord_max': 1201000}

anzahl_innerhalb = 0
anzahl_ausserhalb = 0

for p in punkte:
    if bbox["ost_min"] <= p["ost"] and bbox["nord_min"] <= p["nord"] and bbox["ost_max"] >= p["ost"] and bbox["nord_max"] >= p["nord"]:
        print(f"{p["name"]} befindet sich innerhalb der Boundingbox")
        anzahl_innerhalb += 1
    else:
        print(f"{p["name"]} liegt ausserhalb der Boundingbox")
        anzahl_ausserhalb += 1

print(f"die {anzahl_innerhalb} Punkte innerhalb der bbox")
print(f"die {anzahl_ausserhalb} Punkte ausserhalb der bbox")