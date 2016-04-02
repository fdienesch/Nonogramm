__author__ = 'daniel'
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.nonoControl import NonoController

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = NonoController()
    myapp.show()
    sys.exit(app.exec_())