from PyQt6.QtWidgets import *
import sys 

app = QApplication(sys.argv)

vindu = QWidget()

vindu.setWindowTitle('hello world')
vindu.resize(300,1000)
vindu.move(700,300)

vindu.show()

sys.exit(app.exec())