__author__ = 'daniel'
from Objekte.spielfeld import Spielfeld
class NonoModel:

    """
    MVC pattern: Creates a model - mvc pattern.
    """
    def __init__(self, parent=None):
        """
        Model dient zur Datenhaltung

        :param difficult: schwierigkeit
        :param rgb - rgb farbcode
        :param nonogram - Spielfeld für den user
        :param feld - user eingabe feld
        :param angabe - angabe für den user zur lösung
        :return:
        """
        self.difficult = 1
        self.gradR = 0
        self.gradG = 0
        self.gradB = 0
        self.nonogram = Spielfeld(self.difficult)
        self.feld = [None] * self.nonogram.felder
        self.offeneFelder = 0
        self.angabe = self.nonogram.checkSpielfeld()
        pass
