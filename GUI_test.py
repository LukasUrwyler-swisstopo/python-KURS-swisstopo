import tkinter as tk

window = tk.Tk()
window.title("Title")
window.config(bg="dark gray")
window.minsize(400, 400)
window.maxsize(600, 600)

widgets = [tk.Label, tk.Button, tk.Entry, tk.Checkbutton]

for widget in widgets:
    try:
        w = widget(window, text=widget.__name__)
    except tk.TclError:
        w = widget(window)

    w.pack(padx=10, pady=10, fill="x")

window.mainloop()