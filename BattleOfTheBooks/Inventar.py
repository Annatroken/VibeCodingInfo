class Inventar:

    def __init__(self):

        self.buecher = []

    def buch_hinzufuegen(self, buch):

        self.buecher.append(buch)

        print(f"{buch.titel} wurde hinzugefügt.")

    def buch_entfernen(self, buch):

        if buch in self.buecher:
            self.buecher.remove(buch)

    def anzeigen(self):

        print("Inventar:")

        if len(self.buecher) == 0:
            print("Keine Bücher vorhanden.")

        for buch in self.buecher:
            print("-", buch.titel)

    def buch_verwenden(self, nummer, lehrer):

        if nummer < len(self.buecher):

            buch = self.buecher[nummer]

            buch.verwenden(lehrer)

            self.buecher.remove(buch)