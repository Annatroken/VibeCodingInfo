from lehrer import Lehrer


class Deutschlehrer(Lehrer):

    def __init__(self, name):
        super().__init__(name, "Deutsch")

    def spezial_faehigkeit(self, gegner):
        print(f"{self.name} benutzt Rechtschreibkorrektur!")

        gegner.angriff -= 5

        if gegner.angriff < 5:
            gegner.angriff = 5

        print(f"{gegner.name} verliert 5 Angriff.")