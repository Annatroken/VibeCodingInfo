from buch import Buch
from lehrer.mathelehrer import Mathelehrer

spieler = Mathelehrer("Herr Euler")

buch = Buch("Mathematik-Lexikon", angriff=20)

spieler.inventar.buch_hinzufuegen(buch)

spieler.inventar.anzeigen()

spieler.inventar.buch_verwenden(0, spieler)

print(spieler.angriff)