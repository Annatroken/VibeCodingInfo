from arena import Arena

from lehrer.mathelehrer import Mathelehrer
from lehrer.deutschlehrer import Deutschlehrer

arena = Arena("Bücherkeller")

spieler1 = Mathelehrer("Herr Euler")
spieler2 = Deutschlehrer("Herr Goethe")

arena.kampf_starten(spieler1, spieler2)