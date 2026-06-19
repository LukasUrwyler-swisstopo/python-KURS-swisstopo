from multiprocessing.util import info


class Orthophoto:
    def __init__(self, name, epsg, bandanzahl, BIT):
        self.name = name
        self.epsg = epsg
        self.bandanzahl = bandanzahl
        self.bits = BIT

    def info(self):
        print(f"{self.name} | EPSG:{self.epsg} | {self.bandanzahl} Bänder | {self.bits} Bit")

    def bit_tiefe(self):
        print(f"{self.bits} Bit entsprechen einer Farbtiefe von {2 ** self.bits} Farben.")

DOP16 = Orthophoto("Orthophoto_2024", 2056, 4, 16)
DOP8 = Orthophoto("Orthophoto_2024", 2056, 4, 8)

DOP16.info()
DOP16.bit_tiefe()
