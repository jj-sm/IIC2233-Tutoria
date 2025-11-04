import sys
import random
import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget
from dvd import DVDLogo, DVD_PATH
from clock import Clock


class MovimientoThread(QThread):
    actualizar = ...

    def __init__(self, ancho: int, alto: int, velocidad: int=1, dimensiones_logo: tuple[int,int]=(120, 80)):
        super().__init__()
        ...

    def run(self):
        ...


    def collisions(self):
        """
        Esta funcion detecta colisiones con los bordes de la ventana
        y cambia la direccion del movimiento y el color del logo
        """
        ...


    @staticmethod
    def _random_color():
        """Genera un Color Aleatorio"""
        return QColor(
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )


    def stop(self):
        ...


class Pantalla(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DVD Screensaver")
        self.resize(1280, 720)
        self.initialize()


    def initialize(self):
        ...

    def mover_logo(self, punto, color):
        ...

    def stop_window(self, event):
        self.thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Pantalla()
    ventana.show()
    sys.exit(app.exec_())
