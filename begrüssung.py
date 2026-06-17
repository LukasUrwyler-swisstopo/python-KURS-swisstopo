def hallo():
    name = input("Bitte geben Sie ihr Vorname ein ")
    while True:
        try:
            if len(name) == 0:
                print("Die Eingabe darf nicht NULL sein")
        except:
            print("Bitte gib einen neuen Namen ein")
        break
    if name[0] == "A":
        print("Bravo, dein Name ist ganz vorne im Alphabet")
        return
    print(f"Hallo {name}")

hallo()