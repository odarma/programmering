from PyQt6.QtWidgets import *
import sys 

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('oppmeldingsskjema')
        self.setGeometry(100,100,300,100)

        layout=QFormLayout()
        self.setLayout(layout)

        layout.addRow('navn:', QLineEdit())
        layout.addRow('epost:', QLineEdit())
        layout.addRow('passord:', QLineEdit(echoMode=QLineEdit.EchoMode.Password))
        layout.addRow('bekreft passord:', QLineEdit(echoMode=QLineEdit.EchoMode.Password))
        layout.addRow(QPushButton('meld deg opp'))

        self.show()

#-----------------
if __name__ == '__main__':
    app=QApplication([])
    vindu = Hovedvindu()
    sys.exit(app.exec())