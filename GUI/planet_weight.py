import sys, random 
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

planeter = ['merkur','venus', 'jorden', 'mars', 'jupiter', 'saturn', 'uranus','neptun']
tyngdekraft = [3.7,8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

planetbilde = [
'/home/oam/Dokumenter/GitHub/programmering/GUI/bilder/sun.png', 
'/home/oam/Dokumenter/GitHub/programmering/GUI/bilder/merkur.png', 
'/home/oam/Dokumenter/GitHub/programmering/GUI/bilder/venus.png', 
'/home/oam/Dokumenter/GitHub/programmering/GUI/bilder/jorden.png', 
'/home/oam/Dokumenter/GitHub/programmering/GUI/bilder/mars.png', 
'/home/oam/Dokumenter/GitHub/programmering/GUI/bilder/jupiter.png', 
'/home/oam/Dokumenter/GitHub/programmering/GUI/bilder/saturn.png', 
'/home/oam/Dokumenter/GitHub/programmering/GUI/bilder/uranus.png', 
'/home/oam/Dokumenter/GitHub/programmering/GUI/bilder/neptun.png']


class Hovedvindu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('vekt av planeter')
        self.setGeometry(100,100,500,400)
        vinduikon = QIcon(planetbilde[0])
        self.setWindowIcon(vinduikon)

        layout=QGridLayout()
        self.setLayout(layout)

        topplabel=QLabel('hva er din vekt på en annen planet?')
        layout.addWidget(topplabel,0,0,1,2,alignment=Qt.AlignmentFlag.AlignCenter)

        self.skjema = QFormLayout()
        self.meny = QComboBox()
        self.meny.setPlaceholderText('velg en planet...')
        self.meny.addItem('tilfeldig planet')
        for planet in planeter:
            self.meny.addItem(planet)
        self.meny.activated.connect(self.oppdater_bilde)
        self.skjema.addRow(self.meny)

        self.vekt = QDoubleSpinBox()
        self.vekt.setDecimals(1)
        self.vekt.setPrefix('din vekt i kg:        ')
        self.skjema.addRow(self.vekt)
        self.regne_ut_knapp = QPushButton('regn ut')
        self.regne_ut_knapp.clicked.connect(self.regne_ut)
        self.skjema.addRow(self.regne_ut_knapp)
        layout.addLayout(self.skjema,1,0)

        self.bunntekst = QLabel('velg en planet og skriv inn din vekt!')
        layout.addWidget(self.bunntekst,2,0,1,2,alignment=Qt.AlignmentFlag.AlignCenter)

        self.bilde = QLabel()
        self.pixmap = QPixmap('/home/oam/Dokumenter/GitHub/programmering/GUI/bilder/sun.png')
        self.pixmap = self.pixmap.scaled(256,256)
        self.bilde.setPixmap(self.pixmap)
        layout.addWidget(self.bilde,1,1)

        self.show()

    def oppdater_bilde(self):
        self.pixmap = QPixmap(planetbilde[self.meny.currentIndex()])
        self.pixmap = self.pixmap.scaled(256,256)
        self.bilde.setPixmap(self.pixmap)

    def regne_ut(self):
        self.planetnummer = self.meny.currentIndex
        if self.planetnummer == 0:
            self.planetnummer == random.randrange(0,len(planeter))
            self.ny_vekt=beregn_vekt(self.vekt.value(),tyngdekraft[self.planetnummer])
            self.bunntekst.setText(f'du fikk planeten {planeter[self.planetnummer]}! din vekt på denne planeten, med tyngdekraft {tyngdekraft[self.planetnummer]}, ville vært {self.ny_vekt}')
            self.pixmap = QPixmap(planetbilde[self.planetnummer + 1])
            self.pixmap = self.pixmap.scaled(256,256)
            elf.bilde.setPixmap(self.pixmap)
        else:
            pass

    def beregn_vekt(din_vekt, planettyngdekraft, jordtyngdekraft=9.807):
        beregnet_vekt = (din_vekt/jordtyngdekraft)*planettyngdekraft
        return round(beregnet_vekt, 2)
#-----------------
if __name__ == '__main__':
    app=QApplication([])
    vindu = Hovedvindu()
    sys.exit(app.exec())