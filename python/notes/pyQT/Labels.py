# PyQT6 introduction

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class MainWIndow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1000, 500)               # (x, y, width, height)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #00FF00;"
                            "background-color: #586760;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # label.setAlignment(Qt.AlignmentFlag.AlignTop)             # Vertically top
        # label.setAlignment(Qt.AlignmentFlag.AlignBottom)          # Vertically bottom
        # label.setAlignment(Qt.AlignmentFlag.AlignVCenter)         # Vertically Center

        # label.setAlignment(Qt.AlignmentFlag.AlignRight)           # Hor. Right
        # label.setAlignment(Qt.AlignmentFlag.AlignLeft)            # Hor. Left
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter)         # Hor. Center

        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)        # Applying multiple alignments.

def main():
    app = QApplication(sys.argv)        # object
    window = MainWIndow()               # object
    window.show()
    sys.exit(app.exec())               # app object has a built-in .exec_() method ... for executing user inputs

if __name__ == "__main__":
    main()



