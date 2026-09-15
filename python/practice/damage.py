# 2. The HP Tracker (Easy-Medium)

# OOP Concept: State management and multiple signals.

# The Task: Build a window with one QLabel displaying "100" (your HP),
# and two QPushButtons underneath it: "Take Damage (-10)" and "Use Potion (+20)".

# The Logic: Create an instance variable self.hp = 100. Connect the Damage button to a method that subtracts 10,
# and the Potion button to a method that adds 20. Update the label text automatically every time the math happens.
# Prevent the HP from going above 100 or below 0.


import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QGridLayout
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.attack_button = QPushButton("Attack", self)
        self.heal_button = QPushButton("Heal", self)
        self.health = QLabel("100", self)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        layout.addWidget(self.attack_button)
        layout.addWidget(self.heal_button)
        layout.addWidget(self.health)


        central_widget.setLayout(layout)





        self.attack_button.clicked.connect(self.attack)
        self.heal_button.clicked.connect(self.heal)


    def attack(self):
        pass

    def heal(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
