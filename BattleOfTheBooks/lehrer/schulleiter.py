from lehrer import Lehrer


class Schulleiter(Lehrer):

    def __init__(self, name):
        super().__init__(name, "Schulleitung")

    def spezial_faehigkeit(self, gegner):

        print("Unangekündigte Konferenz!")

        gegner.energie -= 30

        if gegner.energie < 0:
            gegner.energie = 0

        print(f"{gegner.name} verliert 30 Energie.")