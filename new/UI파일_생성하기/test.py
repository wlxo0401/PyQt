import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# PY 형식 파일 import 
from ui.untitled import Ui_MainWindow

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow):
    def __init__(self) :
        QMainWindow.__init__(self)

        # UI 선언
        main_ui = Ui_MainWindow()
        # UI 설정
        main_ui.setupUi(self)

        # 화면을 보여준다.
        self.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()