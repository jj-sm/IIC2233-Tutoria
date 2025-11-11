# actividad1.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt
import time

class ContadorThread(QThread):
    actualizar_tiempo = pyqtSignal(float)
    corriendo = True

    def run(self):
        segundos = 0
        while True:
            if self.corriendo:
                segundos += 0.1
                self.actualizar_tiempo.emit(round(segundos, 1))
            time.sleep(0.1)

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Actividad 1 — Reloj con pausa")
        self.setMinimumSize(200, 100)
        self.init_window()


    def init_window(self):
        self.label = QLabel("0")
        self.label.setAlignment(Qt.AlignCenter)
        self.boton = QPushButton("Pausar")

        h_box = QHBoxLayout()
        v_box = QVBoxLayout()

        h_box.addWidget(self.label)
        v_box.addLayout(h_box)
        v_box.addWidget(self.boton)
        self.setLayout(v_box)

        self.thread = ContadorThread()
        self.thread.actualizar_tiempo.connect(self.actualizar_label)
        self.thread.start()

        self.boton.clicked.connect(self.toggle)


    def actualizar_label(self, valor):
        self.label.setText(str(valor))

    def toggle(self):
        self.thread.corriendo = not self.thread.corriendo
        self.boton.setText("Reanudar" if not self.thread.corriendo else "Pausar")

app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
app.exec_()
