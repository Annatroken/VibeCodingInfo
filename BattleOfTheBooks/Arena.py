class Arena:

    def __init__(self, name):

        self.name = name
        self.runde = 1

    def kampf_starten(self, spieler1, spieler2):

        while not spieler1.ist_besiegt() and not spieler2.ist_besiegt():

            print(f"--- Runde {self.runde} ---")

            spieler1.angreifen(spieler2)

            if spieler2.ist_besiegt():
                break

            spieler2.angreifen(spieler1)

            self.runde += 1

        if spieler1.ist_besiegt():
            print(f"{spieler2.name} gewinnt!")

        else:
            print(f"{spieler1.name} gewinnt!")