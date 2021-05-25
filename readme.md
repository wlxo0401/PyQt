# PyQt

## PyQt란?
PyQt란, Qt의 레이아웃에 Python의 코드를 연결하여 GUI 프로그램을 만들 수 있게 해주는 프레임워크를 의미합니다. PyQt는 C++의 Cross Platform GUI Framework인 Qt를 영국의 Riverbank Computing에서 Python 모듈로 변환해주는 툴을 만들어주며 시작되었습니다. 현재는 PyQt4버전과 PyQt5버전이 주로 사용되고 있습니다.



## PyQt의 특징
Python에도 PyGTK, PySide, Tkinter등 다양한 GUI Framework가 존재합니다. 하지만 이런 GUI Framework들은 사용하기도 어렵고, 시각적으로 예쁘지 않다는 단점이 있습니다.

PyQt는 이러한 Framework들과 다르게 시각적으로도 괜찮은 디자인을 보여주면서 Qt Designer라는 프로그램을 이용하여 프로그램을 손쉽게 설계할 수 있다는 장점이 있습니다. 이러한 이유로 이 책에서는 PyQt를 이용하여 GUI 프로그램을 만들어보도록 하겠습니다.

[출처](https://wikidocs.net/35478)

## PyQt5 설치 
```
pip install PyQt5
```
PyQt5를 기준으로 작성

## PyQt6 설치
```
pip install PyQt6
```

# Qt Desinger

- PyQt 및 PySide UI를 쉽게 짜게해주는 프로그램  

## 창 생성

![영상정보 미리 로드](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/1.PNG) 

메인화면 모습

![영상정보 미리 로드](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/2.PNG)

새로운 윈도우를 만들어주기 위해서

```파일 - 새폼``` 클릭

![영상정보 미리 로드](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/3.PNG)

원하는 폼을 선택 처음에는 보통 ```Main Window``` 선택

## 구역 설명

![영상정보 미리 로드](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/4.PNG)

1. 생성된 폼
2. 사용 가능한 도구들 모음
3. 생성된 폼에 추가된 도구들 모음
4. 스타일 설정

나머지는 사용을 안해봐서 모르겠음

# 기본 사용법

```
import sys

from main import MainWindow
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
```
- run.py


```
from PyQt5 import uic
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QMainWindow

form_class = uic.loadUiType("./ui_main.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()
```
- main.py

# 사용법

## 도구



## 잡기술

### -프레임(타이틀바, title bar) 없애기 
![영상정보 미리 로드](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/6.PNG)
```
self.setWindowFlag(Qt.FramelessWindowHint)
```
타이틀바를 없애고 custom하기 위해서 사용 가능
프레임이 없어진 만큼 윈도우 기본 API(닫기, 최소화, 최대화, aero snap 등등)은 스스로 구현해야 함

### -프레임 및 배경 없애기
![영상정보 미리 로드](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/5.PNG)
```
self.setAttribute(Qt.WA_TranslucentBackground)
self.setWindowFlag(Qt.FramelessWindowHint)
```
프레임 show() 이전에 넣으면 없어짐

