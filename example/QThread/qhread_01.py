import sys
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("./ui/qthread_ui_01.ui")[0]

# 쓰레드 생성 ex) class 쓰레드이름(QThread)
class thread_001(QThread):
    # 시그널 생성 괄호 안에는 넘겨줄 변수 타입
    value_signal = pyqtSignal(int)

    # 쓰레드 시작시 수행
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        print(f'thread id {int(QThread.currentThreadId())}')

        for i in range(1, 101):
            print(f"value : {i}")
            self.value_signal.emit(i)
            QThread.sleep(1)




#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()