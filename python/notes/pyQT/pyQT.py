# PyQT6 introduction

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QIcon

class MainWIndow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(0, 0, 1000, 500)
        self.setWindowIcon(QIcon("pewdiepie.jpg"))

def main():
    app = QApplication(sys.argv)        # object
    window = MainWIndow()               # object
    window.show()
    sys.exit(app.exec())               # app object has a built-in .exec_() method ... for executing user inputs

if __name__ == "__main__":
    main()



