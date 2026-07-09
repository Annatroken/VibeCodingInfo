import random

from lehrer import Lehrer


class Chemielehrer(Lehrer):

    def __init__(self, name):
        super().__init__(name, "Chemie")

    def spezial_faehigkeit(self, gegner):

        schaden = random.randint(15, 40)

        print(f"{self.name} führt einen explosiven Versuch durch!")

        gegner.lebenspunkte -= schaden

        print(f"{gegner.name} erhält {schaden} Schaden.")