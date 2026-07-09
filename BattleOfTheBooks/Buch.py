class Buch:

    def __init__(self, titel, bonus):

        self.titel = titel
        self.bonus = bonus

    def verwenden(self, lehrer):

        lehrer.angriff += self.bonus