from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
import sys 

class Vindu(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300,300)
        self.setWindowTitle('noe')

        label = QLabel()
        label.setText('hallo')
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(label)

        label_image = QLabel()
        pixmap = QPixmap("/home/oam/Dokumenter/GitHub/programmering/GUI/pony.jpg")
        label_image.setPixmap(pixmap)
        layout.addWidget(label_image)

#-----------------
app=QApplication([])
vindu = Vindu()
vindu.show()
sys.exit(app.exec())