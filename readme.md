# PyQt

> 작성일자 2021-05-26 ~    
> 작성자 : 김지태   
> 참고 1 : https://wikidocs.net/book/2944   
> 참고 2 : https://www.youtube.com/c/WandersonIsMe

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

![창생성](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/1.PNG) 

메인화면 모습

![창생성](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/2.PNG)

새로운 윈도우를 만들어주기 위해서

```파일 - 새폼``` 클릭

![창생성](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/3.PNG)

원하는 폼을 선택 처음에는 보통 ```Main Window``` 선택

## 구역 설명

![창생성](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/4.png)

1. 생성된 폼
2. 사용 가능한 도구들 모음
3. 생성된 폼에 추가된 도구들 모음
4. 스타일 설정

나머지는 사용을 안해봐서 모르겠음   
<br>
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

메인 코드를 불러오기 위해서 실행되는 코드   
굳이 필요는 없음

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

메인 코드 ui를 연결하고 코드를 실행하고 등등   
<br>

# 사용법

## 도구

### 레이아웃(Layout)
![레이아웃](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/1.gif)

1. 수평으로 배치(horizontal Layout)   
가로 방향으로 배치
2. 수직으로 배치(Vertical Layout)   
세로 방향으로 배치
3. 격자형으로 배치(Grid Layout)   
바둑판 형식으로 배치
4. 폼 레이아웃으로 배치(form Layout)   
회원가입같은 느낌으로 배치?

### 프레임(QFrame)
![프레임(타이틀바, title bar) 없애기 ](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/8.PNG)

html에서 div로 틀을 만들어 나가듯이 pyqt에서도 frame으로 틀을 잡아가면서
하는게 편해보인다. frame 추가 후 레이아웃 적용과 마진 및 스페이스 그리고 최대 사이즈
설정으로 좀 더 디테일한 디자인이 가능해진다.

### 버튼(QPushButton)
![버튼(QPushButton)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/7.PNG)

클릭하면 동작을 수행 
```
self.[버튼위젯이름].clicked.connect(연결되는 기능)
```
![버튼 기능](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/3.gif)

### 라디오버튼(QRadioButton)
![라디오버튼(QRadioButton)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/7.gif)

setText(), text()를 통해서 라디오 버튼 텍스트도 읽고 쓰기 가능

라디오 버튼 토글(클릭)
```
self.라디오 위젯 이름].toggled.connect([기능])
self.라디오 위젯 이름].clicked.connect([기능])
```
> 위 두개다 사용 가능

라디오 버튼 자동으로 체크를 걸기
```
self.[라디오 위젯 이름].setChecked(True)
```
> 체크를 다른 기능들을 통해서 자동으로 걸기 가능

체크 여부 확인
```
self.[라디오 위젯 이름].isChecked()
```
> 체크 여부를 확인하여 if문등 사용 가능 True False로 알려줌

### 레이블(QLabel)
![레이블](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/4.gif)

텍스트 입/출력

레이블 내용 받아오기 str 형식으로 받아옴
```
self.[레이블 위젯 이름].text()
```

레이블 내용 바꾸기 str 형식으로
```
self.[레이블 위젯 이름].setText([넣을 내용 str만 가능])
```

예시

```
self.pushButton.clicked.connect(self.one)
self.pushButton_2.clicked.connect(self.two)
```
버튼 두개를 두 함수와 연결

```
def one(self):
    self.content = self.label.text()

def two(self):
    self.label_2.setText(self.content)
```
```one```함수에서 레이블 내용을 가지고온다. 
```two```함수에서 레이블 내용을 넣어준다.

### 라인에디트(QLineEdit)
![라인에디트(QLineEdit)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/5.gif)

텍스트 입/출력
사용법은 레이블과 같음

라인에디트 내용 받아오기
```
self.[라인 에디트 이름].text()
```

라인데이트 내용 바꾸기
```
self.[라인 에디트 이름].setText([넣을 내용 str만 가능])
```

계산기 예시

```
self.pushButton_2.clicked.connect(self.sum)
self.pushButton_3.clicked.connect(self.reset)
```
버튼 두개를 각각 더하기와 리셋 함수를 연결

```
def sum(self):
    # 라인 에디트에서 수를 받아옴
    a = self.lineEdit.text()
    b = self.lineEdit_2.text()

    # 더하기 진행 int 형식으로 변환 필요
    sum_result = int(a) + int(b)

    # 레이블에 출력
    self.label.setText(str(sum_result))

def reset(self):
    # 초기화는 정적으로 내용을 채워주는 방법으로
    self.lineEdit.setText("0")
    self.lineEdit_2.setText("0")
    self.label.setText("더하기 답")
```
![라인에디트(QLineEdit)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/6.gif)

텍스트 변화를 인지해서 자동으로 기능 수행
```
self.[라인 에디트 이름].textChanged.connect([기능])
```

라인에디트에서 엔터를 클릭해서 기능 수행
```
self.[라인 에디트 이름].returnPressed.connect([기능])
```


## 잡기술

### 레이아웃 꼭 적용하기
![레이아웃 꼭 적용하기](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/2.gif)

레이아웃을 적용해야 프로그램 사이즈가 바뀌어도 동적으로 도구들이 사이즈가 변함


### 프레임(타이틀바, title bar) 없애기 
![프레임(타이틀바, title bar) 없애기 ](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/6.PNG)
```
self.setWindowFlag(Qt.FramelessWindowHint)
```
타이틀바를 없애고 custom하기 위해서 사용 가능
프레임이 없어진 만큼 윈도우 기본 API(닫기, 최소화, 최대화, aero snap 등등)은 </br>스스로 구현해야 함

### 프레임 및 배경 없애기
![프레임 및 배경 없애기](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/5.PNG)
```
self.setAttribute(Qt.WA_TranslucentBackground)
self.setWindowFlag(Qt.FramelessWindowHint)
```
show() 이전에 넣으면 없어짐

## 스타일