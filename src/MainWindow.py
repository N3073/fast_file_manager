from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self,app_title:str,width:int,height:int):
        super().__init__()

        self.setWindowTitle(app_title)


        self.setFixedSize(QSize(width, height))
        layout = QVBoxLayout()
        top_bar = QHBoxLayout()
        central_bar = QHBoxLayout()
        layout.addLayout(top_bar)
        layout.addLayout(central_bar)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # Set the central widget of the Window.
