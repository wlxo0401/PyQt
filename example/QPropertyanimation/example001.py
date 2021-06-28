from PyQt5 import uic
from PyQt5.QtCore import QEasingCurve, QPropertyAnimation, QRect, Qt

from PyQt5.QtWidgets import QMainWindow

form_class = uic.loadUiType("./ui/example001.ui")[0]

class mainwindow(QMainWindow, form_class):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.ani0(int(self.lineEdit.text())))
        self.show()
    
    def ani0(self, duration):
        self.animation_0 = QPropertyAnimation(self.frame_0, b"geometry")
        self.animation_0.setDuration(duration)
        self.animation_0.setStartValue(QRect(20, 20, 40, 40))
        self.animation_0.setEndValue(QRect(1050, 20, 70, 70))
        self.animation_0.setEasingCurve(QEasingCurve.Linear)
        self.animation_0.start()
        self.ani1(duration)
    
    def ani1(self, duration):
        self.animation_1 = QPropertyAnimation(self.frame_1, b"geometry")
        self.animation_1.setDuration(int(duration))
        self.animation_1.setStartValue(QRect(20, 100, 40, 40))
        self.animation_1.setEndValue(QRect(1050, 100, 70, 70))
        self.animation_1.setEasingCurve(QEasingCurve.InQuad)
        self.animation_1.start()
        self.ani2(duration)

    def ani2(self, duration):
        self.animation_2 = QPropertyAnimation(self.frame_2, b"geometry")
        self.animation_2.setDuration(int(duration))
        self.animation_2.setStartValue(QRect(20, 180, 40, 40))
        self.animation_2.setEndValue(QRect(1050, 180, 70, 70))
        self.animation_2.setEasingCurve(QEasingCurve.OutQuad)
        self.animation_2.start()
        self.ani3(duration)

    def ani3(self, duration):
        self.animation_3 = QPropertyAnimation(self.frame_3, b"geometry")
        self.animation_3.setDuration(int(duration))
        self.animation_3.setStartValue(QRect(20, 260, 40, 40))
        self.animation_3.setEndValue(QRect(1050, 260, 70, 70))
        self.animation_3.setEasingCurve(QEasingCurve.InOutQuad)
        self.animation_3.start()
        self.ani4(duration)

    def ani4(self, duration):
        self.animation_4 = QPropertyAnimation(self.frame_4, b"geometry")
        self.animation_4.setDuration(int(duration))
        self.animation_4.setStartValue(QRect(20, 340, 40, 40))
        self.animation_4.setEndValue(QRect(1050, 340, 70, 70))
        self.animation_4.setEasingCurve(QEasingCurve.OutInQuad)
        self.animation_4.start()
        self.ani5(duration)

    def ani5(self, duration):
        self.animation_5 = QPropertyAnimation(self.frame_5, b"geometry")
        self.animation_5.setDuration(int(duration))
        self.animation_5.setStartValue(QRect(20, 420, 40, 40))
        self.animation_5.setEndValue(QRect(1050, 420, 70, 70))
        self.animation_5.setEasingCurve(QEasingCurve.InCubic)
        self.animation_5.start()
        self.ani6(duration)

    def ani6(self, duration):
        self.animation_6 = QPropertyAnimation(self.frame_6, b"geometry")
        self.animation_6.setDuration(int(duration))
        self.animation_6.setStartValue(QRect(20, 500, 40, 40))
        self.animation_6.setEndValue(QRect(1050, 500, 70, 70))
        self.animation_6.setEasingCurve(QEasingCurve.OutCubic)
        self.animation_6.start()
        self.ani7(duration)

    def ani7(self, duration):
        self.animation_7 = QPropertyAnimation(self.frame_7, b"geometry")
        self.animation_7.setDuration(int(duration))
        self.animation_7.setStartValue(QRect(20, 580, 40, 40))
        self.animation_7.setEndValue(QRect(1050, 580, 70, 70))
        self.animation_7.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation_7.start()
        self.ani8(duration)

    def ani8(self, duration):
        self.animation_8 = QPropertyAnimation(self.frame_8, b"geometry")
        self.animation_8.setDuration(int(duration))
        self.animation_8.setStartValue(QRect(20, 660, 40, 40))
        self.animation_8.setEndValue(QRect(1050, 660, 70, 70))
        self.animation_8.setEasingCurve(QEasingCurve.OutInCubic)
        self.animation_8.start()
        self.ani9(duration)
    
    def ani9(self, duration):
        self.animation_9 = QPropertyAnimation(self.frame_9, b"geometry")
        self.animation_9.setDuration(int(duration))
        self.animation_9.setStartValue(QRect(20, 740, 40, 40))
        self.animation_9.setEndValue(QRect(1050, 740, 70, 70))
        self.animation_9.setEasingCurve(QEasingCurve.InQuart)
        self.animation_9.start()
        self.ani10(duration)

    def ani10(self, duration):
        self.animation_10 = QPropertyAnimation(self.frame_10, b"geometry")
        self.animation_10.setDuration(int(duration))
        self.animation_10.setStartValue(QRect(20, 820, 40, 40))
        self.animation_10.setEndValue(QRect(1050, 820, 70, 70))
        self.animation_10.setEasingCurve(QEasingCurve.OutQuart)
        self.animation_10.start()
        self.ani11(duration)

    def ani11(self, duration):
        self.animation_11 = QPropertyAnimation(self.frame_11, b"geometry")
        self.animation_11.setDuration(int(duration))
        self.animation_11.setStartValue(QRect(20, 900, 40, 40))
        self.animation_11.setEndValue(QRect(1050, 900, 70, 70))
        self.animation_11.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation_11.start()
        self.ani12(duration)

    def ani12(self, duration):
        self.animation_12 = QPropertyAnimation(self.frame_12, b"geometry")
        self.animation_12.setDuration(int(duration))
        self.animation_12.setStartValue(QRect(20, 980, 40, 40))
        self.animation_12.setEndValue(QRect(1050, 980, 70, 70))
        self.animation_12.setEasingCurve(QEasingCurve.OutInQuart)
        self.animation_12.start()
        self.ani13(duration)


    def ani13(self, duration):
        self.animation_13 = QPropertyAnimation(self.frame_13, b"geometry")
        self.animation_13.setDuration(int(duration))
        self.animation_13.setStartValue(QRect(20, 1060, 40, 40))
        self.animation_13.setEndValue(QRect(1050, 1060, 70, 70))
        self.animation_13.setEasingCurve(QEasingCurve.InQuint)
        self.animation_13.start()
        self.ani14(duration)

    def ani14(self, duration):
        self.animation_14 = QPropertyAnimation(self.frame_14, b"geometry")
        self.animation_14.setDuration(int(duration))
        self.animation_14.setStartValue(QRect(20, 1140, 40, 40))
        self.animation_14.setEndValue(QRect(1050, 1140, 70, 70))
        self.animation_14.setEasingCurve(QEasingCurve.OutQuint)
        self.animation_14.start()
        self.ani15(duration)

    def ani15(self, duration):
        self.animation_15 = QPropertyAnimation(self.frame_15, b"geometry")
        self.animation_15.setDuration(int(duration))
        self.animation_15.setStartValue(QRect(20, 1220, 40, 40))
        self.animation_15.setEndValue(QRect(1050, 1220, 70, 70))
        self.animation_15.setEasingCurve(QEasingCurve.InOutQuint)
        self.animation_15.start()
        self.ani16(duration)

    def ani16(self, duration):
        self.animation_16 = QPropertyAnimation(self.frame_16, b"geometry")
        self.animation_16.setDuration(int(duration))
        self.animation_16.setStartValue(QRect(20, 1300, 40, 40))
        self.animation_16.setEndValue(QRect(1050, 1300, 70, 70))
        self.animation_16.setEasingCurve(QEasingCurve.OutInQuint)
        self.animation_16.start()
        self.ani17(duration)

    def ani17(self, duration):
        self.animation_17 = QPropertyAnimation(self.frame_17, b"geometry")
        self.animation_17.setDuration(int(duration))
        self.animation_17.setStartValue(QRect(20, 1380, 40, 40))
        self.animation_17.setEndValue(QRect(1050, 1380, 70, 70))
        self.animation_17.setEasingCurve(QEasingCurve.InSine)
        self.animation_17.start()
        self.ani18(duration)

    def ani18(self, duration):
        self.animation_18 = QPropertyAnimation(self.frame_18, b"geometry")
        self.animation_18.setDuration(int(duration))
        self.animation_18.setStartValue(QRect(20, 1460, 40, 40))
        self.animation_18.setEndValue(QRect(1050, 1460, 70, 70))
        self.animation_18.setEasingCurve(QEasingCurve.OutSine)
        self.animation_18.start()
        self.ani19(duration)

    def ani19(self, duration):
        self.animation_19 = QPropertyAnimation(self.frame_19, b"geometry")
        self.animation_19.setDuration(int(duration))
        self.animation_19.setStartValue(QRect(20, 1540, 40, 40))
        self.animation_19.setEndValue(QRect(1050, 1540, 70, 70))
        self.animation_19.setEasingCurve(QEasingCurve.InOutSine)
        self.animation_19.start()
        self.ani20(duration)

    def ani20(self, duration):
        self.animation_20 = QPropertyAnimation(self.frame_20, b"geometry")
        self.animation_20.setDuration(int(duration))
        self.animation_20.setStartValue(QRect(20, 1620, 40, 40))
        self.animation_20.setEndValue(QRect(1050, 1620, 70, 70))
        self.animation_20.setEasingCurve(QEasingCurve.OutInSine)
        self.animation_20.start()
        self.ani21(duration)

    def ani21(self, duration):
        self.animation_21 = QPropertyAnimation(self.frame_21, b"geometry")
        self.animation_21.setDuration(int(duration))
        self.animation_21.setStartValue(QRect(20, 1700, 40, 40))
        self.animation_21.setEndValue(QRect(1050, 1700, 70, 70))
        self.animation_21.setEasingCurve(QEasingCurve.InExpo)
        self.animation_21.start()
        self.ani22(duration)

    def ani22(self, duration):
        self.animation_22 = QPropertyAnimation(self.frame_22, b"geometry")
        self.animation_22.setDuration(int(duration))
        self.animation_22.setStartValue(QRect(20, 1780, 40, 40))
        self.animation_22.setEndValue(QRect(1050, 1780, 70, 70))
        self.animation_22.setEasingCurve(QEasingCurve.OutExpo)
        self.animation_22.start()
        self.ani23(duration)

    def ani23(self, duration):
        self.animation_23 = QPropertyAnimation(self.frame_23, b"geometry")
        self.animation_23.setDuration(int(duration))
        self.animation_23.setStartValue(QRect(20, 1860, 40, 40))
        self.animation_23.setEndValue(QRect(1050, 1860, 70, 70))
        self.animation_23.setEasingCurve(QEasingCurve.InOutExpo)
        self.animation_23.start()
        self.ani24(duration)

    def ani24(self, duration):
        self.animation_24 = QPropertyAnimation(self.frame_24, b"geometry")
        self.animation_24.setDuration(int(duration))
        self.animation_24.setStartValue(QRect(20, 1940, 40, 40))
        self.animation_24.setEndValue(QRect(1050, 1940, 70, 70))
        self.animation_24.setEasingCurve(QEasingCurve.OutInExpo)
        self.animation_24.start()
        self.ani25(duration)

    def ani25(self, duration):
        self.animation_25 = QPropertyAnimation(self.frame_25, b"geometry")
        self.animation_25.setDuration(int(duration))
        self.animation_25.setStartValue(QRect(20, 2020, 40, 40))
        self.animation_25.setEndValue(QRect(1050, 2020, 70, 70))
        self.animation_25.setEasingCurve(QEasingCurve.InCirc)
        self.animation_25.start()
        self.ani26(duration)

    def ani26(self, duration):
        self.animation_26 = QPropertyAnimation(self.frame_26, b"geometry")
        self.animation_26.setDuration(int(duration))
        self.animation_26.setStartValue(QRect(20, 2100, 40, 40))
        self.animation_26.setEndValue(QRect(1050, 2100, 70, 70))
        self.animation_26.setEasingCurve(QEasingCurve.OutCirc)
        self.animation_26.start()
        self.ani27(duration)

    def ani27(self, duration):
        self.animation_27 = QPropertyAnimation(self.frame_27, b"geometry")
        self.animation_27.setDuration(int(duration))
        self.animation_27.setStartValue(QRect(20, 2180, 40, 40))
        self.animation_27.setEndValue(QRect(1050, 2180, 70, 70))
        self.animation_27.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation_27.start()
        self.ani28(duration)

    def ani28(self, duration):
        self.animation_28 = QPropertyAnimation(self.frame_28, b"geometry")
        self.animation_28.setDuration(int(duration))
        self.animation_28.setStartValue(QRect(20, 2260, 40, 40))
        self.animation_28.setEndValue(QRect(1050, 2260, 70, 70))
        self.animation_28.setEasingCurve(QEasingCurve.OutInCirc)
        self.animation_28.start()
        self.ani29(duration)

    def ani29(self, duration):
        self.animation_29 = QPropertyAnimation(self.frame_29, b"geometry")
        self.animation_29.setDuration(int(duration))
        self.animation_29.setStartValue(QRect(20, 2340, 40, 40))
        self.animation_29.setEndValue(QRect(1050, 2340, 70, 70))
        self.animation_29.setEasingCurve(QEasingCurve.InElastic)
        self.animation_29.start()
        self.ani30(duration)

    def ani30(self, duration):
        self.animation_30 = QPropertyAnimation(self.frame_30, b"geometry")
        self.animation_30.setDuration(int(duration))
        self.animation_30.setStartValue(QRect(20, 2420, 40, 40))
        self.animation_30.setEndValue(QRect(1050, 2420, 70, 70))
        self.animation_30.setEasingCurve(QEasingCurve.OutElastic)
        self.animation_30.start()
        self.ani31(duration)

    def ani31(self, duration):
        self.animation_31 = QPropertyAnimation(self.frame_31, b"geometry")
        self.animation_31.setDuration(int(duration))
        self.animation_31.setStartValue(QRect(20, 2500, 40, 40))
        self.animation_31.setEndValue(QRect(1050, 2500, 70, 70))
        self.animation_31.setEasingCurve(QEasingCurve.InOutElastic)
        self.animation_31.start()
        self.ani32(duration)

    def ani32(self, duration):
        self.animation_32 = QPropertyAnimation(self.frame_32, b"geometry")
        self.animation_32.setDuration(int(duration))
        self.animation_32.setStartValue(QRect(20, 2580, 40, 40))
        self.animation_32.setEndValue(QRect(1050, 2580, 70, 70))
        self.animation_32.setEasingCurve(QEasingCurve.OutInElastic)
        self.animation_32.start()
        self.ani33(duration)

    def ani33(self, duration):
        self.animation_33 = QPropertyAnimation(self.frame_33, b"geometry")
        self.animation_33.setDuration(int(duration))
        self.animation_33.setStartValue(QRect(20, 2660, 40, 40))
        self.animation_33.setEndValue(QRect(1050, 2660, 70, 70))
        self.animation_33.setEasingCurve(QEasingCurve.InBack)
        self.animation_33.start()
        self.ani34(duration)

    def ani34(self, duration):
        self.animation_34 = QPropertyAnimation(self.frame_34, b"geometry")
        self.animation_34.setDuration(int(duration))
        self.animation_34.setStartValue(QRect(20, 2740, 40, 40))
        self.animation_34.setEndValue(QRect(1050, 2740, 70, 70))
        self.animation_34.setEasingCurve(QEasingCurve.OutBack)
        self.animation_34.start()
        self.ani35(duration)

    def ani35(self, duration):
        self.animation_35 = QPropertyAnimation(self.frame_35, b"geometry")
        self.animation_35.setDuration(int(duration))
        self.animation_35.setStartValue(QRect(20, 2820, 40, 40))
        self.animation_35.setEndValue(QRect(1050, 2820, 70, 70))
        self.animation_35.setEasingCurve(QEasingCurve.InOutBack)
        self.animation_35.start()
        self.ani36(duration)

    def ani36(self, duration):
        self.animation_36 = QPropertyAnimation(self.frame_36, b"geometry")
        self.animation_36.setDuration(int(duration))
        self.animation_36.setStartValue(QRect(20, 2900, 40, 40))
        self.animation_36.setEndValue(QRect(1050, 2900, 70, 70))
        self.animation_36.setEasingCurve(QEasingCurve.OutInBack)
        self.animation_36.start()
        self.ani37(duration)

    def ani37(self, duration):
        self.animation_37 = QPropertyAnimation(self.frame_37, b"geometry")
        self.animation_37.setDuration(int(duration))
        self.animation_37.setStartValue(QRect(20, 2980, 40, 40))
        self.animation_37.setEndValue(QRect(1050, 2980, 70, 70))
        self.animation_37.setEasingCurve(QEasingCurve.InBounce)
        self.animation_37.start()
        self.ani38(duration)

    def ani38(self, duration):
        self.animation_38 = QPropertyAnimation(self.frame_38, b"geometry")
        self.animation_38.setDuration(int(duration))
        self.animation_38.setStartValue(QRect(20, 3060, 40, 40))
        self.animation_38.setEndValue(QRect(1050, 3060, 70, 70))
        self.animation_38.setEasingCurve(QEasingCurve.OutBounce)
        self.animation_38.start()
        self.ani39(duration)

    def ani39(self, duration):
        self.animation_39 = QPropertyAnimation(self.frame_39, b"geometry")
        self.animation_39.setDuration(int(duration))
        self.animation_39.setStartValue(QRect(20, 3140, 40, 40))
        self.animation_39.setEndValue(QRect(1050, 3140, 70, 70))
        self.animation_39.setEasingCurve(QEasingCurve.InOutBounce)
        self.animation_39.start()
        self.ani40(duration)

    def ani40(self, duration):
        self.animation_40 = QPropertyAnimation(self.frame_40, b"geometry")
        self.animation_40.setDuration(int(duration))
        self.animation_40.setStartValue(QRect(20, 3220, 40, 40))
        self.animation_40.setEndValue(QRect(1050, 3220, 70, 70))
        self.animation_40.setEasingCurve(QEasingCurve.OutInBounce)
        self.animation_40.start()











