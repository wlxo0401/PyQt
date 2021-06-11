# 목차
[1. PyQt](#1-PyQt)   
 - [PyQt란?](#pyqt란)
 - [PyQt의 특징](#pyqt의-특징)   
 - [PyQt5 설치](#pyqt5-설치)   
 - [PyQt6 설치](#pyqt6-설치)   

[2. Qt Desinger](#2-Qt-Desinger)   
 - [창 생성](#창-생성)
 - [구역 설명](#구역-설명)

[3. 시작하기 전](#3-시작하기-전)
 - [준비 코드](#준비-코드)
 - [기타 사항](#기타-사항)

[4. 사용방법](#4-사용방법)
 - [도구](#도구)   
  [1.레이아웃(QLayout)](#레이아웃qlayout)   
  [2.프레임(QFrame)](#프레임qframe)   
  [3.버튼(QPushButton)](#버튼qpushbutton)   
  [4.라디오버튼(QRadioButton)](#라디오버튼qradiobutton)   
  [5.체크박스(QCheckBox)](#체크박스qcheckbox)   
  [5.레이블(QLabel)](#레이블qlabel)     
  [6.라인에디트(QLineEdit)](#라인에디트qlineedit)   
  [7.리스트위젯(QListWidget)](#리스트위젯qlistwidget)   
  [8.슬라이더(QHorizontalSlider, QVerticalSlider), 다이얼(QDial)](#슬라이더qhorizontalslider-qverticalslider-다이얼qdial)   
  [9.스택(QStackedWidget)](#스택qstackedwidget)   
  [10.메세지박스(QMessageBox)](#메세지박스qmessagebox)
 - [잡기술](#잡기술)   
  [1.레이아웃 꼭 적용하기](#레이아웃-꼭-적용하기)   
  [2.프레임(타이틀바, title bar) 없애기](#프레임타이틀바-title-bar-없애기)   
  [3.프레임 및 배경 없애기](#프레임-및-배경-없애기)  
  [4.체크박스(QCheckBox)로 다른 체크박스 키고 끄기](#체크박스qcheckbox로-다른-체크박스-키고-끄기)  
  [5.위젯 활성화/비활성화(껏다 키기)](#위젯-활성화비활성화껏다-키기)  
  [6.툴팁(ToolTip)](#툴팁tooltip)    
  [7.사진 넣기(QPixmap)](#사진-넣기qpixmap)
 - [스타일](#스타일)   
  [1.적용방법](#적용방법)   
  [2.종류](#종류)   
   - [color](#color)
   - [border-color](#border-color)
   - [border-width](#border-width)
   - [border-style](#border-style)
   - [border-radius](#border-radius)
   - [hover(마우스 올렸을 때)](#hover마우스-올렸을-때)
   - [pressed(마우스 누르기(클릭) 상황)](#pressed마우스-누르기클릭-상황)


# 1. PyQt

> 작성일자 2021-05-26 ~    
> 작성자 : 김지태   
> 참고 1 : https://wikidocs.net/book/2944   
> 참고 2 : https://www.youtube.com/c/WandersonIsMe   
> 참고 3 : https://het.as.utexas.edu/HET/Software/html/stylesheet-reference.html   
> 참고 4 : https://doc.qt.io/qt-5/qtcore-index.html   
> 참고 5 : https://github.com/PyQt5/PyQt
<hr>

```
주의

- 틀린 내용이 있을 수 있습니다. 
- 사용한 위주로 정리되었습니다.
- 더 좋은 방법은 많습니다.
- 개인적인 용도로 필력 수준이 떨어지고 남들이 보기 불편합니다.
- 더 좋은 자료 많습니다.
```

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

# 2. Qt Desinger

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

# 3. 시작하기 전
## 준비 코드
```python
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

```python
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

## 기타 사항
> 특수한 위젯만 사용 가능한 메소드가 아니면 다양하게 적용 가능합니다.   
> ex) text(), setText(), clicked 등등   
> 
> 프레임(틀) 기능하는 위젯 안에는 다른 위젯을 추가로 넣을 수 있습니다.   
> ex) layout, frame, groupbox, stacked Widget 등등
>
> 프레임 안에 위젯을 넣을 경우 스타일 적용할 때 구분을 잘해야함

# 4. 사용방법

## 도구

### 레이아웃(QLayout)
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
self.[버튼위젯 이름].clicked.connect(기능)
```
![버튼 기능](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/3.gif)

### 라디오버튼(QRadioButton)
![라디오버튼(QRadioButton)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/7.gif)

> setText(), text()를 통해서 라디오 버튼 텍스트도 읽고 쓰기 가능   
> 라디오버튼은 다중 선택이 불가능합니다.

라디오 버튼 토글(클릭)
```python
self.[라디오위젯 이름].toggled.connect([기능])
self.[라디오위젯 이름].clicked.connect([기능])
```
> 위 두개다 사용 가능

라디오 버튼 자동으로 체크를 걸기
```python
self.[라디오위젯 이름].setChecked(True)
```
> 체크를 다른 기능들을 통해서 자동으로 걸기 가능

체크 여부 확인
```python
self.[라디오위젯 이름].isChecked()
```
> 체크 여부를 확인하여 if문등 사용 가능 True False로 알려줌

### 체크박스(QCheckBox)
![체크박스(QCheckBox)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/13.gif)
```python
self.[체크박스 이름].stateChanged.connect([기능])
```
> 체크박스 여부만 알고 있으면 다른 위젯들과 같이 조합해서 사용 가능합니다.

예시
```python
# 놀이를 고르는 체크 박스 두개
self.checkBox.stateChanged.connect(self.work)
self.checkBox_2.stateChanged.connect(self.work)

# 음식을 고르는 체크 박스 두개
self.checkBox_3.stateChanged.connect(self.work)
self.checkBox_4.stateChanged.connect(self.work)

# 정보를 담을 리스트. 체크박스 활용은 각자 다릅니다.
self.game = list()
self.food = list()
```

```python
def work(self):
        if self.checkBox.isChecked():
            if self.checkBox.text() not in self.game:
                self.game.append(self.checkBox.text())
        else:
            if self.checkBox.text() in self.game:
                self.game.remove(self.checkBox.text())

        if self.checkBox_2.isChecked():
            if self.checkBox_2.text() not in self.game:
                self.game.append(self.checkBox_2.text())
        else:
            if self.checkBox_2.text() in self.game:
                self.game.remove(self.checkBox_2.text())
        
        if self.checkBox_3.isChecked():
            if self.checkBox_3.text() not in self.food:
                self.food.append(self.checkBox_3.text())
        else:
            if self.checkBox_3.text() in self.food:
                self.food.remove(self.checkBox_3.text())

        if self.checkBox_4.isChecked():
            if self.checkBox_4.text() not in self.food:
                self.food.append(self.checkBox_4.text())
        else:
            if self.checkBox_4.text() in self.food:
                self.food.remove(self.checkBox_4.text())
        
        self.label.setText(f"나는 {self.game}가 좋아요. 점심으로 {self.food}를 먹었어요.")
```
> 체크 박스 여부에 따라 리스트 삽입/제거를 수행하고 그대로 레이블에 출력하는 코드   
> 더 좋은 방법이 있을 수 있지만 간단하게 생각해본 내용입니다.   
> 체크박스는 라디오버튼과 다르게 다중 선택이 가능합니다.

### 레이블(QLabel)
![레이블](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/4.gif)

텍스트 입/출력

레이블 내용 받아오기 str 형식으로 받아옴
```python
self.[레이블위젯 이름].text()
```

레이블 내용 바꾸기 str 형식으로
```python
self.[레이블위젯 이름].setText([넣을 내용 str만 가능])
```

예시

```python
self.pushButton.clicked.connect(self.one)
self.pushButton_2.clicked.connect(self.two)
```
버튼 두개를 두 함수와 연결

```python
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
```python
self.[라인에디트 이름].text()
```

라인데이트 내용 바꾸기
```python
self.[라인에디트 이름].setText([넣을 내용 str만 가능])
```

계산기 예시
```python
self.pushButton_2.clicked.connect(self.sum)
self.pushButton_3.clicked.connect(self.reset)
```
버튼 두개를 각각 더하기와 리셋 함수를 연결

```python
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
```python
self.[라인에디트 이름].textChanged.connect([기능])
```

라인에디트에서 엔터를 클릭해서 기능 수행
```python
self.[라인에디트 이름].returnPressed.connect([기능])
```

### 리스트위젯(QListWidget)
![리스트위젯(QListWidget)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/12.gif)
> 리스트는 위젯(Widget)과 뷰(view)가 있는데 위젯이 더 간편한 것 같음   
> 사용법은 같으나 편리함 정도 차이가 있음
```python
# 한번 클릭
self.[리스트위젯 이름].itemClicked.connect([기능])

# 더블 클릭
self.[리스트위젯 이름].itemDoubleClicked.connect([기능])

# 항목 변경
self.[리스트위젯 이름].currentItemChanged.connect([기능])
```
> 리스트위젯 클릭 이벤트를 담당하는 신호

```python
# 선택된 리스트위젯 아이템 번호
self.[리스트위젯 이름].currentRow()

# 선택된 리스트위젯 객체 반환
self.[리스트위젯 이름].currentItem()

# row번째 리스트위젯 객체 반환
self.[리스트위젯 이름].item(row)
```
> 리스트 목록 정보를 가지고오는 함수들이다.
> 객체반환은 함수 뒤에 ```.text()```를 하면 텍스트를 가지고옴

```python
# 리스트위제위젯에 항목을 추가합니다.
self.[리스트위젯 이름].addItem(String)

# row번 자리에 항목을 추가합니다.
self.[리스트위젯 이름].insertItem(row, String)

# row번 자리 항목으로 가지고 옵니다.
self.[리스트위젯 이름].tatkeItem(row)

# 리스트위젯을 초기화합니다.
self.[리스트위젯 이름].clear()
```
> 리스트 위젯에 항목들을 컨트롤합니다. 조합을 통하여 다양하게 사용가능   
> Qt Designer를 통하여 다양한 속성 조절이 가능합니다.

예시
```python
# 버튼을 통하여 기능들을 연결합니다.
self.pushButton.clicked.connect(self.add_item)
self.pushButton_2.clicked.connect(self.insert_item)
self.pushButton_3.clicked.connect(self.take_item)
self.pushButton_4.clicked.connect(self.clear)
self.pushButton_5.clicked.connect(self.item_row)

# 리스트위젯 클릭을 통하여 기능 연결
self.listWidget.itemClicked.connect(self.one_click)
self.listWidget.itemDoubleClicked.connect(self.double_click)
self.listWidget.currentItemChanged.connect(self.change_item)
```

```python
def add_item(self):
    self.listWidget.addItem(self.lineEdit.text())
def insert_item(self):
    self.listWidget.insertItem(int(self.lineEdit_2.text()), self.lineEdit.text())
def take_item(self):
    self.listWidget.takeItem(int(self.lineEdit_3.text()))
def clear(self):
    self.listWidget.clear()
def item_row(self):
    self.label_4.setText(self.listWidget.item(int(self.lineEdit_4.text())).text())

def one_click(self):
    self.label_2.setText(str(self.listWidget.currentRow()))
    self.label_3.setText(self.listWidget.currentItem().text())
def double_click(self):
    self.label_5.setText(str(self.listWidget.currentRow()))
    self.label_6.setText(self.listWidget.currentItem().text())
def change_item(self):
    self.label_8.setText(str(self.listWidget.currentRow()))
    self.label_9.setText(self.listWidget.currentItem().text())
```
> 각 기능들 사용 예시입니다.

### 슬라이더(QHorizontalSlider, QVerticalSlider), 다이얼(QDial)
![슬라이더(Horizontal Slider, Vertical Slider), 다이얼(Dial)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/19.gif)   
```python
self.[슬라이더, 다이얼 위젯 이름].value()
self.[슬라이더, 다이얼 위젯 이름].minimum()
self.[슬라이더, 다이얼 위젯 이름].maximum()
self.[슬라이더, 다이얼 위젯 이름].singleStep()
self.[슬라이더, 다이얼 위젯 이름].pageStep()
```
> 값들 받아오기
> Value : 슬라이더, 다이얼의 값을 의미   
> Minimum : 슬라이더, 다이얼이 가질 수 있는 가장 작은 값   
> Maximum : 슬라이더, 다이얼이 가질 수 있는 가장 큰 값   
> SingleStep : Slider를 옮기거나, 방향키를 눌러 이동할 수 있는 최소한의 값
> PageStep : 크게 크게 움직인 다면 이동할 수 있는 값 ex) 마우스로 빈공간 클릭, page up, page down 같은

![슬라이더(Horizontal Slider, Vertical Slider), 다이얼(Dial)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/30.PNG)
> Qt Designer로 설정 가능


![슬라이더(Horizontal Slider, Vertical Slider), 다이얼(Dial)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/18.gif)
```python
# 위젯이 움직이면 기능 수행
self.[슬라이더, 다이얼 위젯 이름].sliderMoved.connect([기능])

# 위젯 값이 바뀌면 기능 수행
self.[슬라이더, 다이얼 위젯 이름].valueChanged.connect([기능])

# 위젯 범위가 변경되면 수행
self.[슬라이더, 다이얼 위젯 이름].rangeChanged.connect([기능])
```
> 슬라이더가 움직여야 반응, 값이 바뀌기만해도 반응, 슬라이더 최대 최소 범위가 바뀌면 다시 작동
> 하는 3가지 신호가 있다.

![슬라이더(Horizontal Slider, Vertical Slider), 다이얼(Dial)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/20.gif) 
```python
self.[슬라이더, 다이얼 위젯 이름].setMaximum([설정 최대 수])
self.[슬라이더, 다이얼 위젯 이름].setMinimum([설정 최소 수])
self.[슬라이더, 다이얼 위젯 이름].setSingleStep([움직일때 최소 수])
self.[슬라이더, 다이얼 위젯 이름].setPageStep([움직일때 최소 수])
self.[슬라이더, 다이얼 위젯 이름].setRange([시작 수], [끝 수])
self.[슬라이더, 다이얼 위젯 이름].setValue([바로 적용할 수])
```
> 상태 변경 

### 스택(QStackedWidget)
![스택(Stacked Widget)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/21.gif) 
```python
self.[스택위젯 이름].setCurrentIndex([스택 페이지 번호])
```
> 스택 페이지를 입력해주면 간단하게 페이지를 이동할 수 있다.

### 메세지박스(QMessageBox)
| information | about | warning |
|----|----|----|
| ![information](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/31.PNG) | ![about](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/32.PNG) | ![warning](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/33.PNG) |

| critical | question |
|----|----|
| ![critical](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/34.PNG) | ![question](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/35.PNG) |

```python
from PyQt5.QtWidgets import QMessageBox

QMessageBox.information(self, "타이틀입니다.", "안녕하세요. information 메세지 입력입니다.")
QMessageBox.about(self, "타이틀입니다.", "안녕하세요. about 메세지 입력입니다.")
QMessageBox.warning(self, "타이틀입니다.", "안녕하세요. warning 메세지 입력입니다.")
QMessageBox.critical(self, "타이틀입니다.", "안녕하세요. critical 메세지 입력입니다.")
QMessageBox.question(self, "타이틀입니다.", "안녕하세요. question 메세지 입력입니다.")
```

> 메세지를 표현하는 가장 기본 

[출처](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=huntingbear21&logNo=221825482802)

## 잡기술

### 레이아웃 꼭 적용하기
![레이아웃 꼭 적용하기](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/2.gif)

레이아웃을 적용해야 프로그램 사이즈가 바뀌어도 동적으로 도구들이 사이즈가 변함


### 프레임(타이틀바, title bar) 없애기 
![프레임(타이틀바, title bar) 없애기 ](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/6.PNG)
```python
self.setWindowFlag(Qt.FramelessWindowHint)
```
타이틀바를 없애고 custom하기 위해서 사용 가능
프레임이 없어진 만큼 윈도우 기본 API(닫기, 최소화, 최대화, aero snap 등등)은 </br>스스로 구현해야 함

### 프레임 및 배경 없애기
![프레임 및 배경 없애기](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/5.PNG)
```python
self.setAttribute(Qt.WA_TranslucentBackground)
self.setWindowFlag(Qt.FramelessWindowHint)
```
show() 이전에 넣으면 없어짐

### 체크박스(QCheckBox)로 다른 체크박스 키고 끄기
![체크박스(QCheckBox)로 다른 체크박스 키고 끄기](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/14.gif)
```python
# 체크 풀기
self.[체크박스위젯 이름].setChecked(False)

# 체크 하기
self.[체크박스위젯 이름].setChecked(True)
```
> 위 함수로 간단하게 체크를 대신 켜고 끄기가 가능하다.

### 위젯 활성화/비활성화(껏다 키기)
![위젯 활성화/비활성화(껏다 키기)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/15.gif)
```python
# 비활성화
self.[위젯 이름].setDisabled(True)

# 활성화
self.[위젯 이름].setEnabled(True)
```
> 체크박스 또는 버튼이나 특정 상황에 위젯을 껏다 켜기를 수행할 수 있습니다.

### 툴팁(ToolTip)
![툴팁(ToolTip)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/16.gif)

> Qt Designer에서 설정 가능

![툴팁(ToolTip)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/17.gif)

```python
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtGui import QFont
```
```python
self.pushButton.setToolTip("버튼입니다. <br> 버튼22 <br> <b>두꺼운 글씨</b>")
QToolTip.setFont(QFont('SansSerif', 30))
```
> Qt Designer가 아닌 소스코드 상으로도 툴팁을 추가할 수 있습니다.

### 사진 넣기(QPixmap)

## 스타일

### 적용 방법
![스타일 적용 방법](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/9.PNG)

> 방법 1 : 원하는 위젯 우클릭 후 "styleSheet 바꾸기" 선택  

![스타일 적용 방법](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/11.PNG)

> 방법 1 : 원하는 스타일 적용

![스타일 적용 방법](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/10.PNG)

> 방법 2 : 오른쪽 속성창에서 바로 입력 가능

```python
self.[위젯 이름].setStyleSheet(
    "[위젯 종류] {color: white; background-color: rgb(58, 58, 58);}"
    "[위젯 종류]:[위젯 상황] { background-color:rgb(10, 10, 10); }"
)
```
> 방법 3 : 소스코드상에서 디자인 적용하기

<hr>

![기본 사항](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/12.PNG)

> 위젯 디자인을 적용할 때, 상위와 하위 위젯 연관성을 잘 생각해야합니다.
> 위 사진은 프레임 속에 버튼을 넣은 예시 이미지 입니다.

![기본 사항](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/8.gif)

> 상위 위젯에서 단순하게 ```background-color: rgb(255, 156, 158);``` 식으로 입력하면
> 하위 위젯들도 공통 속성이 존재하면 동시에 적용됩니다.
>
> 위젯마다 스타일을 주는 것이 맞지만 미리 사전 정의를 하면서 진행하는 것이 좋습니다.
> 아래가 그 예시입니다.

![기본 사항](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/9.gif)

```
QFrame {
	background-color: rgb(147, 120, 255);
}
```
```
QPushButton {
	background-color: rgb(164, 255, 79);
}
```
> 각각 위젯에 스타일을 적용한 모습입니다.

```
background-color: #ffffff;
```
> 색상은 ```rgb(255, 255, 255);``` 또는 ```#FFFFFF``` 방법으로 입력 가능합니다.

### 종류

#### background-color
![백그라운드 컬러](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/13.PNG)
```
QPushButton {
	background-color: #ffffff;
}
```
> 위젯 배경색 변경

#### color
![컬러](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/14.PNG)
```
QPushButton {
	color: rgb(255, 211, 76);
}
```
> 위젯 내용색 변경

#### border-color
![border-color](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/28.PNG)
```
QPushButton{
	border-color: rgb(255, 200, 28);	
	border-style : solid;
	border-width : 5px
}
```
> ```border-color: rgb(255, 200, 28);```, ```border-color: #FFFFFF;``` 두 방법으로 테두리 색 지정 가능

#### border-width
| 1px | 10px |  
|----|----| 
|![border-width](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/15.PNG) | ![border-width](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/16.PNG) |
```
QPushButton{
	border-color: rgb(255, 134, 28);	
	border-style : solid;
	border-width : 1px
}
```
> ```border-width : 1px``` 태두리 두깨를 설정 가능

#### border-style
| dashed | dot-dash | dot-dot-dash | dotted |
|----|----|----|----|
| ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/17.PNG) | ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/18.PNG) | ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/19.PNG) | ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/20.PNG) |

| double | groove | inset | outset |
|----|----|----|----|
| ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/21.PNG) | ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/22.PNG) | ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/23.PNG) | ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/24.PNG) |

| ridge | solid | none |
|----|----|----|
| ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/25.PNG) | ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/26.PNG) | ![border-style](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/27.PNG) |
```
QPushButton{
	border-color: rgb(255, 200, 28);	
	border-style : solid;
	border-width : 10px
}
```
> ```border-style : solid;``` 테두리 스타일 설정

#### border-radius
![border-radius](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/29.PNG)
```
QPushButton{
	border-color: rgb(255, 200, 28);	
	border-style : solid;
	border-width : 5px;
	border-radius : 30px;
}
```
> ```border-radius : 30px;``` 으로 테두리 코너 적용 가능

#### hover(마우스 올렸을 때)
![hover(마우스 올렸을 때)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/10.gif)
```
QPushButton{
	border-color: rgb(255, 200, 28);	
	border-style : solid;
	border-width : 5px;
	border-radius : 30px;
}

QPushButton:hover{
	background-color : rgb(200, 255, 30);
	border-color : rgb(255, 200, 28);	
	border-style : solid;
	border-width : 5px;
	border-radius : 30px;
}
```
> ```QPushButton:hover```와 같이 위젯에 hover 스타일 추가, 호버 상황 여부로 스타일 설정하는게 좋음

#### pressed(마우스 누르기(클릭) 상황)
![pressed(마우스 누르기(클릭) 상황)](https://github.com/wlxo0401/Python_PyQt/blob/main/readmeimg/11.gif)
```
QPushButton{
	border-color: rgb(255, 200, 28);	
	border-style : solid;
	border-width : 5px;
	border-radius : 30px;
}

QPushButton:hover{
	background-color : rgb(200, 255, 30);
	border-color : rgb(255, 200, 28);	
	border-style : solid;
	border-width : 5px;
	border-radius : 30px;
}

QPushButton:pressed {
	background-color : rgb(200, 100, 30);
	border-color : rgb(255, 200, 28);	
	border-style : solid;
	border-width : 5px;
	border-radius : 30px;
}
```
> ```QPushButton:pressed```와 같이 위젯에 pressed 스타일 추가, 눌름 상황 여부로 스타일 설정하는게 좋음