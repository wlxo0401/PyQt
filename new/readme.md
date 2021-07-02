# 목차

[0. 개요](#0-개요)

[1. PyQt](#1-PyQt)   
 - [PyQt란?](#pyqt란) 

[2. 시작하기 전](#2-시작하기-전)
 - [아나콘다 설치](#아나콘다-설치)
 - [VSC 설치](#vsc-설치)
 - [PyQt5 설치](#pyqt5-설치)   
 - [PyQt6 설치](#pyqt6-설치)   

[3. Qt Designer](#3-qt-designer)   
 - [Qt Designer 실행](#qt-designer-실행)
 - [창 생성](#창-생성)
 - [구역 설명](#구역-설명)

[4. 시작](#4-시작)
 - [준비 코드](#준비-코드)
 - [기타 사항](#기타-사항)

[5. 사용방법](#5-사용방법)
 - [QLayout](https://github.com/)
 - [위젯]
   [QFrame]
   [QPushButton]


# 0. 개요

PyQt(PySide)를 공부하면서 배운 정보나 기술을 정리하기 위해서 작성을 합니다.
전문적인 지식이 아닌 배우는 입장이기 때문에 글, 프로그램, 알고리즘 등 많이 
부족합니다. 기본 위젯들은 검색하면 쉽게 찾을 수 있기 때문에 간단하게 정리하고 GUI 프로그램을 만들면서 짜집기로 만든 코드 같은 것도 정리할 생각입니다.
이론 적인 부분은 틀렸다 생각하시고 코드만 가볍게 보시면 됩니다.

잘못된 정보는 바로 알려주세요.

```
주의

- 틀린 내용이 있을 수 있습니다. 
- 사용한 위주로 정리되었습니다.
- 개인적인 용도로 필력 수준이 떨어지고 남들이 보기 불편합니다.
- 코드가 정리되지 못하고 긴게 많습니다.
- 더 좋은 방법은 많습니다.
- 더 좋은 자료 많습니다.
```

# 1. PyQt

> 작성일자 2021-06-28 ~    
> 작성자 : 김지태   
> 참고 1 : https://wikidocs.net/book/2944   
> 참고 2 : https://www.youtube.com/c/WandersonIsMe   
> 참고 3 : https://het.as.utexas.edu/HET/Software/html/stylesheet-reference.html   
> 참고 4 : https://doc.qt.io/qt-5/qtcore-index.html   
> 참고 5 : https://github.com/PyQt5/PyQt   
> 참고 6 : https://namu.wiki/w/Qt(%ED%94%84%EB%A0%88%EC%9E%84%EC%9B%8C%ED%81%AC)
<hr>

## PyQt란?

우선 "PyQt" 이름은 기존 Qt(큐트)에서 Python 이름을 합친 것으로 보인다. Qt는 C++에서 사용 가능한 GUI 라이브러리로 시작했다. 크로스플랫폼이 가능하다. 
그것을 Python에서 사용하게 나온 라이브러리가 PyQt이다.

PyQt는 Qt를 만든 곳이 아닌 다른 곳에서 Python을 위해서 바인딩한 것이다. Qt를 만든 곳에서 뒤 늦게 만든 것이 PySide이며 둘은 다른 라이센스를 적용하고 있다.

처음엔 PySide가 부족하다고 했지만 이젠 둘이 많이 비슷하다고 한다. 사실 코딩할때도 PyQt자리에 PySide를 작성하면 된다. 그래서 하나만해도 둘다 할 정도로 편하다고 한다. 간단한 것들은 그렇게 테스트를 해보았는데 아직까지 크게 만든 것을 PySide로 만든 적이 없어서 100% 인지는 장담은 못하겠다.


> 크로스플랫폼 지원 : Windows, Linux, OSX, Android, IOS

> 나무위키 혹은 Qt사이트에는 Qt를 사용한 유명한 프로그램 혹은 제품들을 볼 수 있다.

# 2. 시작하기 전

## 아나콘다 설치

아나콘다는 파이썬을 사용하면서 가상환경에서 프로그램을 작성할 수 있게 도와준다. 가상환경이라는게 거창해보이지만 독립적인 공간을 생성해준다고 보면 된다.
사실 없어도되지만 그 독립적인 공간을 사용하다보면 엄청 편하다. 아나콘다가 아파트라면 독립공간은 1가구가 사는 집이라고 생각하면 편하다.

그 독립적인 구간은 프로젝트 마다 생성하거나하는 방법으로 필요한 라이브러리들을 프로젝트마다 관리가 가능하다. 파이썬만 그냥 컴퓨터에 설치하고 사용할 경우 삭제를 하거나 재설치할때 불편하지만 아나콘다는 그 독립공간 하나만 삭제해주면된다. 처음이 불편하지 나중에는 정말 편하니 꼭 아나콘다를 사용하는 것이 좋다.

위 내용은 PyQt뿐만 아니라 파이썬을 사용한다면 그냥 쓰자

![아나콘다 홈페이지](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/anaconda_install/0-0.PNG)

[아나콘다 홈페이지](https://www.anaconda.com/products/individual) 에 접속해서 바로 다운로드 버튼을 눌러도 가능하다.

![아나콘다 다운로드](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/anaconda_install/0-1.PNG)

화면하단에는 운영체제별로 선택이 가능하다.

![다운로드 방법](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/anaconda_install/1.PNG)

![다운로드 방법](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/anaconda_install/2.PNG)

![다운로드 방법](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/anaconda_install/3.PNG)

대부분 개인적으로 사용할태니 Just Me를 클릭한다.

사실 All Users라고하면 어떤게 다른지 해본적은 없다. 

![다운로드 방법](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/anaconda_install/4.PNG)

경로는 뭐 시키는대로 설정하는 것이 좋아 보인다.

![아나콘다 설치](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/anaconda_install/5.PNG)

개인적으로 위에만 체크해서 사용한다.
여러번 재설치를하고 결국 이렇게 설치하는 법을 유지하는데 이유는 기억이 안난다.

![아나콘다 설치](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/anaconda_install/6.PNG)

![아나콘다 설치](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/anaconda_install/7.PNG)

![아나콘다 설치](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/anaconda_install/8.PNG)

설치 완료

아나콘다는 기본적으로 설치가 끝나면 각각 독립된 공간을 만들어주면서 사용해야한다.
그걸 가상환경을 사용한다고 하는데 VSC를 설치하고 진행하면된다.


## VSC 설치

![아나콘다 설치](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/VSC/1.PNG)

[Visual Studio Code 홈페이지](https://code.visualstudio.com/)에 접속해서 바로 다운로드 버튼을 눌러도 가능하다.

VSC는 설치는 간단하기에 따로 설명을 추가하지는 않는다.


## VSC를 가상환경 생성

![터미널 열기](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/create_env/1.PNG)

터미널 열기
상단 메뉴 터미널 - 새 터미널

VSC는 터미널 기능을 지원하는데 쉽게 생각하면 cmd가 되는 것이라고 생각하자
기본 사용법은 알아야하니 검색을 통해서 익혀두는게 좋음.

![콘다 버전 확인하기](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/create_env/2.PNG)

```
conda --version
```
설치된 콘다 버전을 확인 가능하다.

![콘다 업데이트](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/create_env/3.PNG)

```
conda update conda
```
콘다 업데이트를 가능하게 한다.

![콘다 가상환경 설치](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/create_env/4.PNG)

```python
conda create --name [가상환경이름] python=[파이썬 버전]
```
위와 같은 방법으로 가상환경 생성이 가능하다. 이름과 사용하고 싶은 파이썬 버전만 입력해도 자동으로 설치가 된다.

![콘다 가상환경 실행](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/create_env/5.PNG)

```
activate TestEnv
```
내가 생성한 가상환경을 실행시키는 것이다.
여기서 라이브러리를 설치하고 지우고해도 다른 가상환경 혹은 컴퓨터에 바로 깔린 파이썬은 영향을 받지 않는다.

가상환경은 활성화, 비활성화, 삭제, 생성 등 다양하게 사용 가능하다. 그러니 conda 사용법을 익히는게 좋아보인다.


## PyQt5 설치 
```
pip install PyQt5
```
PyQt5를 기준으로 작성

## PyQt6 설치
```
pip install PyQt6
```


# 3. Qt Designer   
## Qt Designer 실행
![콘다 가상환경 실행](https://github.com/wlxo0401/PyQt/blob/main/new/Etc/readme_image/qt_designer/1.PNG)

```
designer
```
터미널 창 혹은 프로그램 검색해서 designer를 치면 바로 실행된다.

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

# 4. 시작
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