from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys 

class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('grid layout')
        self.setGeometry(100,100,700,300)

        layout=QGridLayout()
        self.setLayout(layout)

        min_label=QLabel()
        min_label.setText('dette er en layout')
        layout.addWidget(min_label,0,0)

        min_inputlinje=QLineEdit()
        min_inputlinje.setPlaceholderText('skriv noe')
        layout.addWidget(min_inputlinje,0,1)

        min_radioknapp = QRadioButton('radioknapp')
        layout.addWidget(min_radioknapp,1,2)

        min_checkbox = QCheckBox('en avkrysningsboks')
        layout.addWidget(min_checkbox,1,1)
        
        min_combobox=QComboBox()
        min_combobox.setPlaceholderText('velg en alternativ')
        min_combobox.addItem('valg 1')
        min_combobox.addItem('valg 2')
        layout.addWidget(min_combobox,1,0)

        min_tekst=QTextEdit()
        min_tekst.setPlaceholderText('skriv noe her')
        layout.addWidget(min_tekst,2,1)

        min_beskjed=QMessageBox()
        min_beskjed.setText('dette er en melding til deg')
        layout.addWidget(min_beskjed,2,0)
        
        min_slider=QSlider()
        min_slider.setRange(10,80)
        layout.addWidget(min_slider,2,2)

        self.show()

#-----------------
if __name__ == '__main__':
    app=QApplication([])
    vindu = Hovedvindu()
    sys.exit(app.exec())