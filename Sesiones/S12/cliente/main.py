# cliente/main.py
import sys
from PyQt5.QtWidgets import QApplication
from ventana_juego import PongWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PongWindow()
    sys.exit(app.exec_())