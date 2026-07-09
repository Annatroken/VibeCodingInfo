class Buch:

    def __init__(self, titel, angriff=0, verteidigung=0, energie=0):

        self.titel = titel
        self.angriff = angriff
        self.verteidigung = verteidigung
        self.energie = energie

    def verwenden(self, lehrer):

        lehrer.angriff += self.angriff
        lehrer.verteidigung += self.verteidigung
        lehrer.energie += self.energie

        print(f"{lehrer.name} benutzt '{self.titel}'.")