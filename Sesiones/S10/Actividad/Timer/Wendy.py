from PyQt5.QtCore import QTimer, QObject
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys, datetime
import time

class Reloj(QObject):
    def __init__(self):
        super().__init__()
        self.running = True
        self.initialize()

    def initialize(self) -> None:
        if self.running:
            self.timer = QTimer()
            self.timer.setInterval(1000) 
            self.timer.timeout.connect(self.actualizar_hora)
            self.timer.start()
    
    def actualizar_hora(self):
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        print(hora_actual)

    def stop(self) -> None:
        self.running = False

app = QApplication(sys.argv)
w = Reloj()
app.exec_()
time.sleep(3)
w.stop()
