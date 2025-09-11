from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self,app_title:str,width:int,height:int):
        super().__init__()

        self.setWindowTitle(app_title)

        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(width, height))
        layout = QVBoxLayout()
        layout.addWidget(button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # Set the central widget of the Window.
