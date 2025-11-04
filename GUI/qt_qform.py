from PyQt6.QtWidgets import *
import sys 

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oppmeldingsskjema')
        self.setGeometry(100,100,300,100)

        layout=QFormLayout()
        self.setLayout(layout)

        layout.addRow('navn:', QLineEdit(self))
        layout.addRow('epost:', QLineEdit(self))
        layout.addRow('passord:', QLineEdit(self))
        layout.addRow('bekreft passord:', QLineEdit(self))

        self.show()

#-----------------
if __name__ == '__main__':
    app=QApplication([])
    vindu = Hovedvindu()
    sys.exit(app.exec())