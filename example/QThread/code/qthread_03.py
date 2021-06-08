import ctypes
import win32con
import sys

from win32process import SuspendThread
from win32process import ResumeThread

from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("../ui/qthread_ui_01.ui")[0]


# 쓰레드 동작용 코드
class Worker(QThread):
    # 값 변화를 알리기 위한 변수
    valueChanged = pyqtSignal(int)
    handle = -1

    # 쓰레드 메인 동작 코드
    def run(self):
        try:
            self.handle = ctypes.windll.kernel32.OpenThread(  # @UndefinedVariable
                win32con.PROCESS_ALL_ACCESS, False, int(QThread.currentThreadId()))
        except Exception as e:
            print('get thread handle failed', e)
        print('thread id', int(QThread.currentThreadId()))
        for i in range(1, 101):
            print('value', i)
            self.valueChanged.emit(i)
            QThread.sleep(1)

# 코드상 메인 부분
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 버튼 클릭 이벤트 연결
        self.pushButton.clicked.connect(self.start)
    
        # 쓰레드 선언
        self._thread = thread_001()
        # 쓰레드 종료하면 연결
        self._thread.finished.connect(self.finished_thread)
        # 쓰레드에서 들어온 신호 value_signal이면 연결
        self._thread.value_signal.connect(self.value)

    # 시작 이벤트
    def start(self):
        if not self._thread.isRunning():
            print(f'main id {int(QThread.currentThreadId())}')
            # 쓰레드 시작
            self._thread.start()

    # 쓰레드 동작에서 값 변환 이벤트
    def value(self, pro):
        self.progressBar.setValue(pro)
    
    # 쓰레드 끝나는 신호
    def finished_thread(self):
        self._thread.deleteLater

    # 창 종료 이벤트
    def closeEvent(self, event):
        # 쓰레드 동작 여부 확인
        if self._thread.isRunning():
            # 쓰레드 종료
            self._thread.quit()
        # 쓰레드 삭제
        del self._thread
        super(WindowClass, self).closeEvent(event)

# 파이썬 실행시 제일 먼저 수행
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()