from tkinter import *
from tkinter import ttk

class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.pen_color = 'black'
        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)

    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y

    def add_line(self, event):
        self.create_line(self.lastx, self.lasty, event.x, event.y,
                         fill=self.pen_color, width=2)
        self.save_posn(event)

    def set_color(self, color):
        self.pen_color = color


root = Tk()
root.title("Sketchpad")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

toolbar = Frame(root, pady=4)
toolbar.grid(column=0, row=0, sticky=(W, E))

Label(toolbar, text="Stiftfarbe:").pack(side=LEFT, padx=6)

sketch = Sketchpad(root, bg='white')
sketch.grid(column=0, row=1, sticky=(N, W, E, S))

for name, color in [("Schwarz", "black"), ("Rot", "red"), ("Blau", "blue")]:
    Button(
        toolbar, text=name, bg=color, fg='white',
        command=lambda c=color: sketch.set_color(c),
        width=8
    ).pack(side=LEFT, padx=2)

root.mainloop()
