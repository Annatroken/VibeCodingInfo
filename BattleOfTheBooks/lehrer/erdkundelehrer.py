from lehrer import Lehrer


class Erdkundelehrer(Lehrer):

    def __init__(self, name):
        super().__init__(name, "Erdkunde")

    def spezial_faehigkeit(self, gegner):

        print(f"{self.name} löst einen Vulkanausbruch aus!")

        gegner.lebenspunkte -= 25