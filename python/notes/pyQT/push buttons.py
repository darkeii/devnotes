import sys

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click here", self)
        self.label = QLabel("Hi !", self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px")
        self.button.clicked.connect(self. on_click)

        self.label.setGeometry(200, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px")

    def on_click(self):
        print("button clicked !!!")
        self.button.setText("Clicked!")              # other def wont understand "button" variable if it is not constructed as "self.buttton" in def __init__ (constructor)
        self.button.setDisabled(True)                # disables the button after click
        self.label.setText("Bye !")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
