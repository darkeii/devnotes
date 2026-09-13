# PyQt6 radio buttons
#
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QMainWindow,
    QRadioButton,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("VisaCard", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("GiftCard", self)

        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)

        # constructing Groups of the RadioButtons
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 40, 300, 50)
        self.radio3.setGeometry(0, 80, 300, 50)

        self.radio4.setGeometry(0, 120, 300, 50)
        self.radio5.setGeometry(0, 160, 300, 50)

        self.setStyleSheet("QRadioButton{"
                            "font-size: 40px"
                            "font-family: Arial;"
                            "padding: 20px;"
                            "}")

        # Adding Radiobuttons to their respective groups ... 1 & 2
        # Group 1
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        # Group 2
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        # setting up what exactly happens when radio button is pressed/changed
        self.radio1.toggled.connect(self.radio_button_changed)              # format : self.(var).(monitor_function).connect(slot)
        self.radio2.toggled.connect(self.radio_button_changed)              # slot : the usr_defined func. which is called/runs when a change is monitored
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_button = self.sender()                          # sender() method will return the widget that sent the signal
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")       # .text() will return the text inside that widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
