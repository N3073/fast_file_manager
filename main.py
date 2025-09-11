from PyQt5.QtWidgets import QApplication, QWidget
from src.MainWindow import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow("Fast file manager",1000,600)
window.show()
def main():
    print("Starting fast-file-manager!")
    app.exec()


if __name__ == "__main__":
    main()
