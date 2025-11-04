import sys
import random
import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget
from dvd import DVDLogo, DVD_PATH
from clock import Clock


class MovimientoThread(QThread):
    actualizar = pyqtSignal(tuple, QColor)

    def __init__(self, ancho: int, alto: int, velocidad: int=1, dimensiones_logo: tuple[int,int]=(120, 80)):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        self.velocidad = velocidad
        self.dimensiones_logo = dimensiones_logo
        self.x, self.y = 100, 100
        self.dx, self.dy = 4 * self.velocidad, 3 * self.velocidad
        self.running = True
        self.color = self._random_color()


    def run(self):
        color = self._random_color()
        while self.running:
            self.x += self.dx
            self.y += self.dy

            self.collisions()

            # Emit new position and color
            self.actualizar.emit((self.x, self.y), self.color)
            time.sleep(0.02)


    def collisions(self):
        """
        Esta funcion detecta colisiones con los bordes de la ventana
        y cambia la direccion del movimiento y el color del logo
        """
        if self.x <= 0 or self.x >= self.ancho - 120:
            self.dx = -self.dx
            self.color = self._random_color()

        if self.y <= 0 or self.y >= self.alto - 80:
            self.dy = -self.dy
            self.color = self._random_color()


    @staticmethod
    def _random_color():
        """Genera un Color Aleatorio"""
        return QColor(
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )


    def stop(self):
        self.running = False
        self.wait()


class Pantalla(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DVD Screensaver")
        self.resize(1280, 720)
        self.initialize()


    def initialize(self):
        # Logo
        self.logo = DVDLogo(DVD_PATH)
        self.logo.setParent(self)

        # Movimiento (QThread)
        self.thread = MovimientoThread(1280, 720)
        self.thread.actualizar.connect(self.mover_logo)
        self.thread.start()

        # Reloj
        self.reloj = Clock(self, color="red")
        self.reloj.move(10, 10)

    def mover_logo(self, punto, color):
        self.logo.move(*punto)
        self.logo.set_color(color)

    def stop_window(self, event):
        self.thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Pantalla()
    ventana.show()
    sys.exit(app.exec_())
