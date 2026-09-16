# Python PyQt6 Digital Clock

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #CSS
        self.time_label.setObjectName("time_label")
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)

        self.setStyleSheet(f"""
            QWidget{{
                background-color: black;
            }}

            QLabel#time_label{{
                font-size: 150px;
                color: hsl(110, 100%, 67%);
                font-family: {font_family}
            }}
            """)


        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)    #
        self.timer.start(1000)                          # updates the clock every 1000ms = 1 sec

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DigitalClock()
    window.show()
    sys.exit(app.exec())
