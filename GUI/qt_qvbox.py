from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys 

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 5, 120, 100)
        self.setWindowTitle('QVBoxLayout-test')
        layout = QVBoxLayout()
        self.setLayout(layout)

        button1 = QPushButton('knapp 1')
        button2 = QPushButton()
        button2.setText('knapp 2')
        button3 = QPushButton('knapp 3')

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        layout.setSpacing(50)
        layout.setContentsMargins(100,100,100,100)

        self.show()

#-----------------
if __name__ == '__main__':
    app=QApplication([])
    vindu = Hovedvindu()
    sys.exit(app.exec())