# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/floriandienesch/Desktop/nonoUI.ui'
#
# Created: Sun Jan 25 17:29:48 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1280, 711)
        Dialog.setStyleSheet(_fromUtf8("#Dialog {\n"
"    background: rgb(255, 183, 227);\n"
"}"))
        self.oben = QtGui.QTableWidget(Dialog)
        self.oben.setEnabled(False)
        self.oben.setGeometry(QtCore.QRect(20, 10, 451, 241))
        self.oben.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.oben.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.oben.setRowCount(8)
        self.oben.setColumnCount(15)
        self.oben.setObjectName(_fromUtf8("oben"))
        self.oben.horizontalHeader().setVisible(False)
        self.oben.horizontalHeader().setDefaultSectionSize(30)
        self.oben.horizontalHeader().setHighlightSections(True)
        self.oben.verticalHeader().setVisible(False)
        self.spielfeld = QtGui.QTableWidget(Dialog)
        self.spielfeld.setGeometry(QtCore.QRect(20, 270, 451, 361))
        self.spielfeld.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spielfeld.setAcceptDrops(False)
        self.spielfeld.setAutoFillBackground(False)
        self.spielfeld.setFrameShape(QtGui.QFrame.NoFrame)
        self.spielfeld.setFrameShadow(QtGui.QFrame.Plain)
        self.spielfeld.setLineWidth(0)
        self.spielfeld.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.spielfeld.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.spielfeld.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.spielfeld.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.spielfeld.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.spielfeld.setRowCount(15)
        self.spielfeld.setColumnCount(15)
        self.spielfeld.setObjectName(_fromUtf8("spielfeld"))
        self.spielfeld.horizontalHeader().setVisible(False)
        self.spielfeld.horizontalHeader().setDefaultSectionSize(30)
        self.spielfeld.horizontalHeader().setMinimumSectionSize(4)
        self.spielfeld.verticalHeader().setVisible(False)
        self.spielfeld.verticalHeader().setDefaultSectionSize(24)
        self.spielfeld.verticalHeader().setMinimumSectionSize(20)
        self.rechts = QtGui.QTableWidget(Dialog)
        self.rechts.setEnabled(False)
        self.rechts.setGeometry(QtCore.QRect(490, 270, 241, 361))
        self.rechts.setAutoFillBackground(False)
        self.rechts.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rechts.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.rechts.setRowCount(15)
        self.rechts.setColumnCount(8)
        self.rechts.setObjectName(_fromUtf8("rechts"))
        self.rechts.horizontalHeader().setVisible(False)
        self.rechts.horizontalHeader().setDefaultSectionSize(30)
        self.rechts.horizontalHeader().setMinimumSectionSize(4)
        self.rechts.verticalHeader().setVisible(False)
        self.rechts.verticalHeader().setDefaultSectionSize(24)
        self.rechts.verticalHeader().setMinimumSectionSize(20)
        self.buttonLoesung = QtGui.QPushButton(Dialog)
        self.buttonLoesung.setGeometry(QtCore.QRect(390, 640, 85, 32))
        self.buttonLoesung.setObjectName(_fromUtf8("buttonLoesung"))
        self.buttonNeustart = QtGui.QPushButton(Dialog)
        self.buttonNeustart.setGeometry(QtCore.QRect(640, 640, 92, 32))
        self.buttonNeustart.setObjectName(_fromUtf8("buttonNeustart"))
        self.comboSchwierigkeit = QtGui.QComboBox(Dialog)
        self.comboSchwierigkeit.setGeometry(QtCore.QRect(490, 640, 133, 26))
        self.comboSchwierigkeit.setObjectName(_fromUtf8("comboSchwierigkeit"))
        self.comboSchwierigkeit.addItem(_fromUtf8(""))
        self.comboSchwierigkeit.addItem(_fromUtf8(""))
        self.comboSchwierigkeit.addItem(_fromUtf8(""))
        self.comboSchwierigkeit.addItem(_fromUtf8(""))
        self.comboSchwierigkeit.addItem(_fromUtf8(""))
        self.labelFelderOffen = QtGui.QLabel(Dialog)
        self.labelFelderOffen.setGeometry(QtCore.QRect(20, 640, 71, 21))
        self.labelFelderOffen.setObjectName(_fromUtf8("labelFelderOffen"))
        self.textBrowserFelderOffen = QtGui.QTextBrowser(Dialog)
        self.textBrowserFelderOffen.setEnabled(False)
        self.textBrowserFelderOffen.setGeometry(QtCore.QRect(180, 640, 181, 31))
        self.textBrowserFelderOffen.setObjectName(_fromUtf8("textBrowserFelderOffen"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.buttonLoesung.setText(_translate("Dialog", "Lösung", None))
        self.buttonNeustart.setText(_translate("Dialog", "Neustart", None))
        self.comboSchwierigkeit.setItemText(0, _translate("Dialog", "EASY", None))
        self.comboSchwierigkeit.setItemText(1, _translate("Dialog", "MEDIUM", None))
        self.comboSchwierigkeit.setItemText(2, _translate("Dialog", "HARD", None))
        self.comboSchwierigkeit.setItemText(3, _translate("Dialog", "EXPERT", None))
        self.comboSchwierigkeit.setItemText(4, _translate("Dialog", "IMPOSSIBLE", None))
        self.labelFelderOffen.setText(_translate("Dialog", "Felder offen:", None))

