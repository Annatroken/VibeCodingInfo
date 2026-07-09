class Lehrer:

    def __init__(self, name, fach):

        self.name = name
        self.fach = fach

        self.lebenspunkte = 100
        self.energie = 100

        self.angriff = 20
        self.verteidigung = 10

    def angreifen(self, gegner):

        schaden = self.angriff - gegner.verteidigung

        if schaden < 1:
            schaden = 1

        gegner.lebenspunkte -= schaden

        print(f"{self.name} greift {gegner.name} an.")

    def ist_besiegt(self):
        return self.lebenspunkte <= 0

    def spezial_faehigkeit(self, gegner):
        pass