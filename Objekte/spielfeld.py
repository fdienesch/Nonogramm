__author__ = 'danielscheuch'
from random import randint

class Spielfeld:
    """
    Spielfeldobjekt
    """
    laenge = 15
    felder = laenge*laenge

    def __init__(self, schwierigkeit):
        """
        Konstruktor
        """
        self.spielfeld = self.makeSpielfeld(schwierigkeit)

    @property
    def getspielfeld(self):
        """
        Spielfeld
        :return: SPielfeld
        """
        return self.spielfeld

    def makeSpielfeld(self, schwierigkeit):
        """
        Generiert durch Zufall das gewünschte Feld
        :param schwierigkeit: Schwierigkeit des Felds
        :return: das generierte Spielfeld
        """
        spielfeld = []
        for x in range(self.felder):
            random = randint(0,10)
            if schwierigkeit == 1:
                if random > 9:
                    spielfeld.append(1)
                else:
                    spielfeld.append(0)

            elif schwierigkeit == 2:
                if random > 7:
                    spielfeld.append(1)
                else:
                    spielfeld.append(0)

            elif schwierigkeit == 3:
                if random > 5:
                    spielfeld.append(1)
                else:
                    spielfeld.append(0)

            elif schwierigkeit == 4:
                if random > 3:
                    spielfeld.append(1)
                else:
                    spielfeld.append(0)

            elif schwierigkeit == 5:
                if random > 2:
                    spielfeld.append(1)
                else:
                    spielfeld.append(0)
        return spielfeld

    def checkHorizontal(self):
        """
        Prüft das SPielfeld für die Zahlen horizontal die für die User als Angabe nötig sind
        :return:werte für die angabe horizontal

        """
        out = []
        row = []
        z = 0
        for x in range(1, len(self.spielfeld)+1):
            if self.spielfeld[x-1] == 1:
                z = z+1
            elif self.spielfeld[x-1] == 0:
                if z != 0:
                    row.append(z)
                z = 0
            if x%self.laenge == 0 and x != 0:
                if z != 0:
                    row.append(z)
                z = 0
                out.append(row)
                row = []
        return out

    def checkVertikal(self):
        """
         Prüft das SPielfeld für die Zahlen vertikal die für die User als Angabe nötig sind
        :return: werte für die angabe vertikal
        """
        out = []
        row = []
        z = 0
        for x in range(self.laenge):
            for y in range(self.laenge):
                if self.spielfeld[x+y*self.laenge] == 1:
                    z = z+1
                elif self.spielfeld[x+y*self.laenge] == 0:
                    if z != 0:
                        row.append(z)
                    z = 0
            else:
                if z != 0:
                    row.append(z)
                z = 0
                out.append(row)
                row = []
        return out

    def checkSpielfeld(self):
        """
        prüft generiertes spielfeld für die eingabe
        :return: array mit 2 stellen das array enthaltet mit jeweiligen angaben
        """
        return [self.checkHorizontal(), self.checkVertikal()]

    def __str__(self):
        """
        toString Methode
        :return: Output String (x/y)
        """
        out = ""
        for x in range(1, len(self.spielfeld)+1):
            if x%self.laenge == 0 and x is not 0:
                out += str(self.spielfeld[x-1]) + "\n"
            else:
                out += str(self.spielfeld[x-1])
        return out