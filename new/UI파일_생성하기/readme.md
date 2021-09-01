[PyQt] 02 - Python GUI 프로그램 | PyQt UI 생성 및 연결 

# 개요

PyQt란, Qt의 레이아웃에 Python의 코드를 연결하여 GUI 프로그램을 만들 수 있게 해주는 프레임워크를 말한다.

즉 UI는 PyQt 프레임워크가 Qt 위젯 및 UI를 구현하게 도와주고, 내부 기능은 Python을 활용한다.

# UI 사용 구조

![UI 사용 구조](1png)

그림을 제대로 그린지는 모르겠지만 큰틀은 이렇고 다음 설명들과 함께 보면 이해되리라 생각된다.

# UI 생성 방법

UI 생성 방법은 ```Qt Desinger```, ```코드 작성```으로 두가지 방법을 사용한다.

## 코드 작성

![코드 작성](2png)

코드를 이용해서 UI를 배칠할 수 있습니다.

## Qt Desginer

![Qt Desinger 이미지](3png)

Qt Designer 프로그램을 이용해서 UI를 보고 배치할 수 있는 장점이 있습니다.

## 장단점

**코드 작성**   
코드를 이용해서 작성하면 python 코드로 기능을 추가할 때 각 UI 위젯들을 변수에 넣어서 사용하기 때문에
자동완성이나 눈으로 찾아서 보는게 편합니다. 

**Qt Designer**
프로그램을 사용해서 UI를 배치하기 때문에 눈으로 보면서 쉽게 UI를 만들 수 있습니다. 
연결하는 방법은 UI형식과 PY형식 두 가지로 나뉩니다.

UI 형식은 Qt Designer에서 바로 생성된 형태이며 코드상에서 불러오면 PyQt가 변환을 자동으로해서 연결시켜줍니다.
하지만 프로그램 배포할 때 UI파일이 따로 보여질 확률이 크기 때문에 저는 추천하지 않습니다.

PY 형식은 Qt Designer에서 생성된 UI형식 파일을 python 코드로 변경해주어서 ```코드 작성``` 방법과 같은 식으로 사용된다.
코드로 변환되기 때문에 프로그램 배포할 때 UI 양식을 숨길 수 있다.


# UI 생성

## 코드 방법
```python
import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 타이틀바 내용 설정
        self.setWindowTitle('PyQt5')
        # 실행 위치
        self.move(300, 300)
        # 사이즈
        self.resize(400, 200)

        # 버튼 생성
        btn = QPushButton("버튼1", self)

        # 레이아웃 생성
        layout = QHBoxLayout()
        # 레이아웃에 버튼 넣기
        layout.addWidget(btn)
        # 최상위 UI에 생성한 Layout 넣기
        self.setLayout(layout)

        # 보여주기
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
```
> 위에 코드만 입력하면 실행이 가능하다.   

 ```코드 방법```은 Python 파일 하나만있으면 UI 작성도하고 기능도 구현하면서 UI변수를 바로바로 보면서 적용하는 장점이 있다. 

 하지만 실행하기 전에는 눈에 보이지 않아서 UI 배치가 어렵고 UI 구현에서도 에러가 발생할 수 있으니 방법이 있다는 것만 알고 넘어가는 것을 추천한다.

![코드방법 실행](1gif)

## Qt Designer

### 공통 구간

![Qt Designer 메인](4png)

원하는 폼을 선택해주세요. 저는 항상 Main Window로 시작하고 필요시 Dialog를 추가하는 방법으로 합니다.

![Qt Designer 작업](2gif)

UI를 배피하고 설정하고 ```Ctrl+R```을 누르면 미리보기가 실행된다.
최종적으로 완료된다고 느껴지면 자신이 정한 폴더에 저장한다. 

![ui파일](5png)

생성된 UI파일

 ### UI 형식

![UI형식 실행](3gif)

```python
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("./ui/untitled.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.show()
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
```

UI 위치를 제대로 적어준다면 위에 코드로 바로 실행이 가능하다. 

하지만 기능을 구현하는 동안 각 위젯들 이름을 기억해야한다.


### PY 형식

UI형식을 PY형식으로 바꾸기 위해서는 변환 작업이 필요한다.

![cmd실행](4gif)

UI파일이 존재하는 곳으로 이동해서 CMD 창을 실행시켜준다.

![cmd실행](5gif)

환경변수가 설정되어 Python이 바로 실행된다면 그냥 하고 Anaconda같은 환경을 사용한다면 PyQt라이브러리가 깔린 가상환경을 실행한다.

![cmd실행](6gif)

```python
python -m PyQt5.uic.pyuic -x [변환대상.ui] -o [변환완료이름.py]
```
위에 코드를 이용해 변환을 진행하면 py 파일이 생성된다.

```python
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
        # UI 준비
        main_ui.setupUi(self)
        # 화면을 보여준다.
        self.show()

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
```

UI파일은 PY파일로 변환했기 때문에 평소 Python import하듯이 클래스를
추가해주면 바로 사용이 가능하다.

![py파일](7gif)

방법만 다를 뿐 같은 결과를 출력한다.

![py파일](8gif)

import를 하기 때문에 변수, 메소드가 자동완성이되어서 편하게 코딩이 가능하다.