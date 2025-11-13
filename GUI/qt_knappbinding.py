from PyQt6.QtWidgets import *
import sys 

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('test av knappbinding')
        self.setGeometry(100,100,300,100)

        layout=QVBoxLayout()
        self.setLayout(layout)

        knapp = QPushButton()
        knapp.setText('min knapp')
        knapp.clicked.connect(self.knapp_trykket)
        layout.addWidget(knapp)

        self.show()

    def knapp_trykket(self):
        print('knapp ble trykket')

#-----------------
if __name__ == '__main__':
    app=QApplication([])
    vindu = Hovedvindu()
    sys.exit(app.exec())