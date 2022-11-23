import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QPushButton, QSpinBox, QMainWindow
from ui_file import Ui_MainWindow
from PyQt5.QtGui import QColor, QPainter
import random


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_ellipce(qp)
        qp.end()

    def draw_ellipce(self, qp):
        lenna = random.choice(range(201))
        qp.setBrush(QColor(random.choice(range(256)), random.choice(range(256)), random.choice(range(256))))
        qp.drawEllipse(random.choice(range(600)), random.choice(range(400)), lenna, lenna)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())