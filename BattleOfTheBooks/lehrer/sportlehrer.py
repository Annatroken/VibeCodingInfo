from lehrer import Lehrer


class Sportlehrer(Lehrer):

    def __init__(self, name):
        super().__init__(name, "Sport")

    def spezial_faehigkeit(self, gegner):
        print(f"{self.name} benutzt Sprint-Angriff!")

        self.angreifen(gegner)

        if not gegner.ist_besiegt():
            self.angreifen(gegner)