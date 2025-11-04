from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys, time

class Worker(QThread):
    progreso = pyqtSignal(int)

    def run(self):
        for i in range(1, 6):
            time.sleep(1)
            self.progreso.emit(i * 20)

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Progreso: 0%")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.worker = Worker()
        self.worker.progreso.connect(self.actualizar_label)
        self.worker.start()

    def actualizar_label(self, valor):
        self.label.setText(f"Progreso: {valor}%")

app = QApplication(sys.argv)
v = Ventana()
v.show()
app.exec_()