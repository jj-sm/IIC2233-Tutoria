# 3.py
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

class Animacion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actividad 4 — Punto animado")

        self.card_vx = 2
        self.card_vy = 1

        self.dragging = False
        self.last_mouse_pos = None

        self.init_layout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.move_card)
        self.timer.start(30)


    def move_card(self):
        if self.dragging:
            return 

        x_pos = self.card.x() + self.card_vx
        y_pos = self.card.y() + self.card_vy

        if x_pos + self.card.width() > self.width() or x_pos < 0:
            self.card_vx *= -1

        if y_pos + self.card.height() > self.height() or y_pos < 0:
            self.card_vy *= -1

        self.card.move(x_pos, y_pos)

    def mousePressEvent(self, event):
        if self.card.geometry().contains(event.pos()):
            self.dragging = True
            self.timer.stop()
            self.last_mouse_pos = event.pos()
            self.card_offset = event.pos() - self.card.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            new_pos = event.pos() - self.card_offset
            self.card.move(new_pos)

            # compute velocity from drag movement
            dx = event.pos().x() - self.last_mouse_pos.x()
            dy = event.pos().y() - self.last_mouse_pos.y()

            # store for release
            self.card_vx = dx
            self.card_vy = dy

            self.last_mouse_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if self.dragging:
            self.dragging = False
            self.timer.start()
            
    def init_layout(self):
        self.setMinimumSize(300, 300)

        self.card = QLabel(self)
        self.card.setPixmap(QPixmap("Sesiones/S11/Parte 3/resources/card_clubs_K.png"))
        self.card.setFixedSize(100, 100)
        self.card.setScaledContents(True)

        


app = QApplication(sys.argv)
ventana = Animacion()
ventana.resize(400, 200)
ventana.show()
app.exec_()
