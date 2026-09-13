# PyQt6 LineEdit
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 390, 40)
        self.button.setGeometry(400, 10, 100 , 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.button.setStyleSheet("font-size: 15px;"
                                     "font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter Your name")            # background text in the textbox
        self.button.clicked.connect(self.submit)                        # connecting the button to do a function "submit"

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
