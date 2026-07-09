from lehrer import Lehrer


class Mathelehrer(Lehrer):

    def __init__(self, name):
        super().__init__(name, "Mathematik")

    def spezial_faehigkeit(self, gegner):
        print(f"{self.name} benutzt Formelsturm!")
        gegner.lebenspunkte -= 30