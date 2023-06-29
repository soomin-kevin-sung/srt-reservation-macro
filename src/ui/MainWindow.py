from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SRT 예약 매크로')
        self.setFixedSize(QSize(250, 500))

        self.setCentralWidget(QPushButton('HelloWorld'))
