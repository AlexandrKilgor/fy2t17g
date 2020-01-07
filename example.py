import sys
from PyQt5.QtCore    import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)
from PyQt5.QtGui     import QKeyEvent

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Voltage')
        self.initUI()

    def keyPressEvent(self, a0: QKeyEvent):
        print('pressed')

    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.lcd.display(40)
        sld = QSlider(Qt.Horizontal, self)
        sld.setValue(40)

        sld.setPageStep(1)                     # <--- Это свойство содержит шаг страницы.

        sld.setTickInterval(5)                      
        sld.setRange(15, 45)
        sld.setFocusPolicy(Qt.StrongFocus)
        sld.setTickPosition(QSlider.TicksBothSides) 
        sld.setSingleStep(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(sld)
        self.setLayout(vbox)

        sld.valueChanged[int].connect(self.lcd.display)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
