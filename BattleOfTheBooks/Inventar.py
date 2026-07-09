class Inventar:

    def __init__(self):

        self.buecher = []

    def buch_hinzufuegen(self, buch):

        self.buecher.append(buch)

    def anzeigen(self):

        for buch in self.buecher:
            print(buch.titel)