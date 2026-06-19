import tkinter as tk


fenster = tk.Tk()
fenster.title("Farbwechsler")
fenster.config(bg="black")
fenster.minsize(200, 200)
fenster.maxsize(600, 600)

def farbe_wechseln():
    aktuelle_farbe = fenster.cget("bg")
    neue_farbe = "white" if aktuelle_farbe == "black" else "black"
    fenster.config(bg=neue_farbe)

button = tk.Button(fenster, text="Schalter", command=farbe_wechseln)
button.pack(padx=100, pady=100)

fenster.mainloop() 

