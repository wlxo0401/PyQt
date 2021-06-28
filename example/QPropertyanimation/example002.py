from PyQt5 import uic
from PyQt5.QtCore import QEasingCurve, QPropertyAnimation, QRect, Qt

from PyQt5.QtWidgets import QMainWindow

form_class = uic.loadUiType("./ui/example001.ui")[0]

class mainwindow(QMainWindow, form_class):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.ani0(int(self.lineEdit.text())))
        self.show()
    






