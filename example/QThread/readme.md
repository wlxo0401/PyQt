# QThread

## 쓰레드 기본

![쓰레드 기본](https://github.com/wlxo0401/PyQt/blob/main/readmeimg/22.gif) 

``` python
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

    # 쓰레드 동작
    def run(self):
        # 쓰레드 ID 확인
        print(f'thread id {int(QThread.currentThreadId())}')

        # 임시 for문
        for i in range(1, 11):
            print(f"value : {i}")
            self.value_signal.emit(i)
            QThread.sleep(1)
        print("끝")



#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 버튼 연결
        self.pushButton.clicked.connect(self.start)
    
        # 쓰레드 선언
        self._thread = thread_001()
        # 쓰레드 종료하면 연결
        self._thread.finished.connect(self.finished_thread)
        # 쓰레드에서 들어온 신호 value_signal이면 연결
        self._thread.value_signal.connect(self.value)

    # 끝나는 신호
    def finished_thread(self):
        print("끝쓰레드")
        self._thread.deleteLater

    # 값 변환 이벤트
    def value(self, pro):
        self.progressBar.setValue(pro)

    # 시작 이벤트
    def start(self):
        if not self._thread.isRunning():
            print(f'main id {int(QThread.currentThreadId())}')
            # 쓰레드 시작
            self._thread.start()
    
    # 창 종료 이벤트
    def closeEvent(self, event):
        print("종료")
        if self._thread.isRunning():
            print("close")
            # 쓰레드 종료
            self._thread.quit()
        
        del self._thread
        super(WindowClass, self).closeEvent(event)


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
```