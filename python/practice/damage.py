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
    def __init__(self, hp):
        super().__init__()
        self.attack_button = QPushButton("Attack")
        self.heal_button = QPushButton("Heal")
        self.health = QLabel("100")
        self.hp = hp
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        layout.addWidget(self.attack_button, 0, 1)
        layout.addWidget(self.heal_button, 1, 1)
        layout.addWidget(self.health, 2, 1)

        self.health.setAlignment(Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)

        self.attack_button.clicked.connect(self.attack)
        self.heal_button.clicked.connect(self.heal)

        #CSS

        self.attack_button.setObjectName("attack")
        self.heal_button.setObjectName("heal")
        self.health.setObjectName("attack")

        self.setStyleSheet("""
            QPushButton{
                font-size: 25px;
                font-family: Arial;
                padding: 30px;
                border: 5px solid #111111;
                border-radius: 40px;
            }

            QPushButton#attack{
                background-color: hsl(12, 100%, 30%);
            }

            QPushButton#attack:hover{
                background-color: hsl(12, 100%, 40%);
            }

            QPushButton#heal{
                background-color: hsl(109, 100%, 30%);
            }

            QPushButton#heal:hover{
                background-color: hsl(109, 100%, 40%);
            }

            QLabel{
                font-size: 25px;
                padding: 30px
            }
            """)

    def attack(self):
        self.hp -= random.randint(0,15)
        print(self.hp)

    def heal(self):
        self.hp += random.randint(0,15)
        print(self.hp)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(hp=100)
    window.show()
    sys.exit(app.exec())
