
# 1. The Server Toggle (Easy)

# OOP Concept: Instance variables (self) and Methods (Slots).

# The Task: Create a QMainWindow with a QLabel (Text: "Server: OFFLINE") and a QPushButton (Text: "Boot Server").

# The Logic: When clicked, a method inside your class should change the label text to "Server: ONLINE" and change the button's text to "Shut Down".
# Hint: You will need a boolean instance variable like self.is_online = False to track the state.


import sys
import time
from PyQt6.QtWidgets import QApplication, QLabel, QLayout, QPushButton, QWidget, QMainWindow, QVBoxLayout
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_online = False
        self.button = QPushButton("ON", self)
        self.label = QLabel("server is OFF", self)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.button.clicked.connect(self.on_click)

        vbox = QVBoxLayout()

        vbox.addWidget(self.button)
        vbox.addWidget(self.label)

        central_widget.setLayout(vbox)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #CSS
        self.button.setStyleSheet("background-color: hsl(234, 67%, 66%);"
                                  "font-size: 30px;"
                                  "font-family: Arial;"
                                  "padding: 15px;"
                                  "margin: 20px;")

        self.label.setStyleSheet("font-size: 20px;"
                                 "font-family: Arial;")

    def on_click(self):
        if self.is_online:
            self.button.setText("ON")
            self.label.setText("server is OFF")
            self.is_online = False

        elif not self.is_online:
            self.button.setText("OFF")
            self.label.setText("server is ON")
            self.is_online = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
