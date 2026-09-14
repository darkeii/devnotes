# PyQt setStyleSheet()
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()               # since we are using layouts... we dont need to .setGeometry()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)       #
        hbox.addWidget(self.button2)       # layout added in the widget
        hbox.addWidget(self.button3)       #

        central_widget.setLayout(hbox)          # we cant directly add the layout in our constructor class because it alrdy has a layout of the parent class "QMainWindow"
                                                # so we first add the layout to a widget.. then we add that widget to our constructor class of "MainWindow" via self.initUI()

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")   # to make changes to a specific one... we have to provide an object name to that widget.
        self.button3.setObjectName("button3")


        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 15px;
                border: 3px solid;
                border-radius: 15px;
            }

            QPushButton#button1{
                background-color: hsl(12, 98%, 40%);
            }

            QPushButton#button2{
                background-color: hsl(118, 78%, 40%);
            }

            QPushButton#button3{
                background-color: hsl(234, 83%, 40%);
            }



            QPushButton#button1:hover{
                background-color: hsl(12, 98%, 60%);
            }

            QPushButton#button2:hover{
                background-color: hsl(118, 78%, 60%);
            }

            QPushButton#button3:hover{
                background-color: hsl(234, 83%, 60%);
            }


            """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
