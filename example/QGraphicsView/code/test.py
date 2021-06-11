import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
                             QPushButton, QVBoxLayout, QWidget, QSlider)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
class CWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 전체 폼 박스
        formbox = QHBoxLayout()
        self.setLayout(formbox)
        # 좌, 우 레이아웃박스
        left = QVBoxLayout()
        right = QVBoxLayout()
        # 그룹박스2
        gb = QGroupBox('펜 설정')
        left.addWidget(gb)
        grid = QGridLayout()
        gb.setLayout(grid)
        label = QLabel('펜 색상')
        grid.addWidget(label, 1, 0)
        self.pencolor = QColor(0, 0, 0)
        self.penbtn = QPushButton()
        self.penbtn.setStyleSheet('background-color: rgb(0,0,0)')
        self.penbtn.clicked.connect(self.showColorDlg)
        grid.addWidget(self.penbtn, 1, 1)
        label = QLabel('펜 굵기')
        grid.addWidget(label, 2, 0)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(3)
        self.slider.setMaximum(21)
        self.slider.setValue(5)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(1)
        self.slider.setSingleStep(1)
        grid.addWidget(self.slider)
        # 그룹박스4
        gb = QGroupBox('지우개')
        left.addWidget(gb)
        hbox = QHBoxLayout()
        gb.setLayout(hbox)
        self.checkbox = QCheckBox('지우개')
        self.checkbox.stateChanged.connect(self.checkClicked)
        hbox.addWidget(self.checkbox)
        left.addStretch(1)
        # 우 레이아웃 박스에 그래픽 뷰 추가
        self.view = CView(self)
        right.addWidget(self.view)
        # 전체 폼박스에 좌우 박스 배치
        formbox.addLayout(left)
        formbox.addLayout(right)
        formbox.setStretchFactor(left, 0)
        formbox.setStretchFactor(right, 1)
        self.setGeometry(100, 100, 800, 500)
    def checkClicked(self):
        pass
    def createExampleGroup(self):
        groupBox = QGroupBox("Slider Example")
        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(1)
        vbox = QVBoxLayout()
        vbox.addWidget(slider)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)
        return groupBox
    def showColorDlg(self):
        # 색상 대화상자 생성
        color = QColorDialog.getColor()
        sender = self.sender()
        # 색상이 유효한 값이면 참, QFrame에 색 적용
        self.pencolor = color
        self.penbtn.setStyleSheet('background-color: {}'.format(color.name()))
# QGraphicsView display QGraphicsScene
class CView(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.items = []
        self.start = QPointF()
        self.end = QPointF()
        self.setRenderHint(QPainter.HighQualityAntialiasing)
    def moveEvent(self, e):
        rect = QRectF(self.rect())
        rect.adjust(0, 0, -2, -2)
        self.scene.setSceneRect(rect)
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # 시작점 저장
            self.start = e.pos()
            self.end = e.pos()
    def mouseMoveEvent(self, e):
        # e.buttons()는 정수형 값을 리턴, e.button()은 move시 Qt.Nobutton 리턴
        if e.buttons() & Qt.LeftButton:
            self.end = e.pos()
            if self.parent().checkbox.isChecked():
                pen = QPen(QColor(255, 255, 255), 10)
                path = QPainterPath()
                path.moveTo(self.start)
                path.lineTo(self.end)
                self.scene.addPath(path, pen)
                self.start = e.pos()
                return None
            pen = QPen(self.parent().pencolor, self.parent().slider.value())
            # Path 이용
            path = QPainterPath()
            path.moveTo(self.start)
            path.lineTo(self.end)
            self.scene.addPath(path, pen)
            # 시작점을 다시 기존 끝점으로
            self.start = e.pos()
    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File",
                QDir.currentPath())
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer",
                        "Cannot load %s." % fileName)
                return
            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0
            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()
            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    w.show()
    sys.exit(app.exec_())