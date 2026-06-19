from datetime import datetime

tage = {
    "Monday": "Montag", "Tuesday": "Dienstag", "Wednesday": "Mittwoch",
    "Thursday": "Donnerstag", "Friday": "Freitag", "Saturday": "Samstag",
    "Sunday": "Sonntag"
}

datum = input("Geburtsdatum eingeben (TT.MM.JJJJ): ")
geburtstag = datetime.strptime(datum, "%d.%m.%Y").date()

wochentag = tage[geburtstag.strftime("%A")]
print(f"Du wurdest an einem {wochentag} geboren.")

dreissigster = geburtstag.replace(year=geburtstag.year + 30)
wochentag_30 = tage[dreissigster.strftime("%A")]
print(f"Deinen 30. Geburtstag feierst du an einem {wochentag_30}.")