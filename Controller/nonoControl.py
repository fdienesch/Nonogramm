__author__ = 'floriandienesch-danielscheuch'

import sys, random
from random import randint
from PyQt5 import QtCore, QtWidgets, QtWidgets, QtGui
from View.nonoView import Ui_Dialog
from Model.nonoModel import NonoModel
from Objekte.spielfeld import Spielfeld

class NonoController(QtWidgets.QMainWindow):
    """
    MVC pattern: Creates a controller - mvc pattern.
    """
    def __init__(self, parent=None):
        """
        Create a new controller with a object MyView
        and a object MyModel using the mvc pattern.
        :param parent:
        """
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.model = NonoModel()
        self.offeneFelder = self.model.nonogram.felder
        self.ui.setupUi(self, self)
        for x in range(16):
            for y in range(16):
                self.ui.spielfeld.setItem(x, y, QtWidgets.QTableWidgetItem())

    def setRechts(self, rechts):
        """
        Setzt die rechten Angaben für den User
        :param rechts: Liste der Angabe
        :return:
        """
        for x in range(len(rechts)):
            for y in range(len(rechts[x])):
                self.ui.rechts.setItem(x, y, QtWidgets.QTableWidgetItem(str(rechts[x][y])))

    def setOben(self, oben):
        """
        Setzt die oberen Angaben für den User
        :param oben: Liste der Angabe
        :return:
        """
        for x in range(len(oben)):
            for y in range(len(oben[x])):
                self.ui.oben.setItem(8 - len(oben[x]) + y, x, QtWidgets.QTableWidgetItem(str(oben[x][y])))

    def changeBg(self, row, column):
        """
        Methode changeBg
        Diese Methode aendert die Hintergrundfarbe von einer spezifischen
        Flaeche wenn man darauf klickt
        führt die statistik
        :param row: row of that tile
        :param column: column of that tile
        :return:
        """
        #print("Zeile %d und Spalte %d" % (row, column))
        if self.ui.spielfeld.item(row, column).background() == QtGui.QColor('white'):
            self.model.feld[row * self.model.nonogram.laenge + column] = 1
            self.ui.spielfeld.item(row, column).setBackground(QtGui.QColor('blue'))

        elif self.ui.spielfeld.item(row, column).background() == QtGui.QColor('blue'):
            self.model.feld[row * self.model.nonogram.laenge + column] = 0
            self.ui.spielfeld.item(row, column).setBackground(QtGui.QColor('orange'))

        elif self.ui.spielfeld.item(row, column).background() == QtGui.QColor('orange'):
            self.model.feld[row * self.model.nonogram.laenge + column] = None
            self.ui.spielfeld.item(row, column).setBackground(QtGui.QColor('white'))

        else:
            self.model.feld[row * self.model.nonogram.laenge + column] = 1
            self.ui.spielfeld.item(row, column).setBackground(QtGui.QColor('blue'))

        self.offeneFelder = self.model.nonogram.felder
        for x in range(0, len(self.model.feld)):
            if self.model.feld[x] == self.model.nonogram.spielfeld[x]:
                self.offeneFelder -= 1
        self.ui.textBrowserFelderOffen.setText(str(self.offeneFelder))

    def loesung(self):
        """
        Method loesung
        Zeigt die Loesung an indem die Spielflaechen gefaerbt werden
        :return:
        """
        for x in range(self.model.nonogram.laenge):
            for y in range(self.model.nonogram.laenge):
                if self.model.nonogram.spielfeld[x * self.model.nonogram.laenge + y] == 1:
                    self.ui.spielfeld.item(x, y).setBackground(QtGui.QColor('blue'))
                elif self.model.nonogram.spielfeld[x * self.model.nonogram.laenge + y] == 0:
                    self.ui.spielfeld.item(x, y).setBackground(QtGui.QColor('orange'))

    def neustart(self):
        """
        Methode neustart
        Setzt alle Spielzuege sowie Statisiken zurueck
        :return:
        """
        self.ui.spielfeld.clear()
        for x in range(16):
            for y in range(16):
                self.ui.spielfeld.setItem(x, y, QtWidgets.QTableWidgetItem())
                self.ui.oben.setItem(x, y, QtWidgets.QTableWidgetItem())
                self.ui.rechts.setItem(x, y, QtWidgets.QTableWidgetItem())

        self.offeneFelder = self.model.nonogram.felder
        self.ui.textBrowserFelderOffen.setText(str(self.offeneFelder))

        self.model.nonogram = Spielfeld(self.model.difficult)
        self.model.angabe = self.model.nonogram.checkSpielfeld()

        self.setOben(self.model.angabe[1])
        self.setRechts(self.model.angabe[0])

    def changeDifficulty(self, item):
        """
        Methode changeDifficulty
        Aendert den Schwierigkeitsgrad
        :param item:
        :return:
        """
        if item == 0:
            self.model.difficult = 1

        elif item == 1:
            self.model.difficult = 2

        elif item == 2:
            self.model.difficult = 3

        elif item == 3:
            self.model.difficult = 4

        elif item == 4:
            self.model.difficult = 5

    def flash(self, grad):
        self.model.gradR = grad
        self.setStyleSheet(("#Dialog {""background: rgb("+str(self.model.gradR)+", "+str(self.model.gradG)+", "+str(self.model.gradB)+");""}"))
        return grad

    def flashG(self, grad):
        self.model.gradG = grad
        self.setStyleSheet(("#Dialog {""background: rgb("+str(self.model.gradR)+", "+str(self.model.gradG)+", "+str(self.model.gradB)+");""}"))

    def flashB(self, grad):
        self.model.gradB = grad
        self.setStyleSheet(("#Dialog {""background: rgb("+str(self.model.gradR)+", "+str(self.model.gradG)+", "+str(self.model.gradB)+");""}"))

    def stock(self):
        self.setStyleSheet(("#Dialog {background: rgb(255, 183, 227);""}"))
