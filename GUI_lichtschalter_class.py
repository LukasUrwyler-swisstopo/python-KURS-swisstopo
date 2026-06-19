from tkinter import Tk, Button, Label

class Lichtschalter:
    def __init__(self):
        self.fenster = Tk()
        self.fenster.title("Farbwechsler")
        self.fenster.config(bg="black")
        self.fenster.geometry("400x400")
        self.is_on = False

        self.label = Label(master=self.fenster, text="Licht ist aus", font=("Arial", 16), bg="black", fg="white")
        self.label.pack(padx=20, pady=20)

        self.button = Button(self.fenster, text="Schalter", command=self.farbe_wechseln)
        self.button.pack(padx=100, pady=100)

        self.fenster.mainloop()

    def farbe_wechseln(self):
        self.is_on = not self.is_on
        neue_farbe = "white" if self.is_on else "black"
        self.fenster.config(bg=neue_farbe)
        self.label.config(
            text="Licht ist an" if self.is_on else "Licht ist aus",
            bg=neue_farbe,
            fg="black" if self.is_on else "white"
        )


lichtschalter = Lichtschalter()
