from PyQt5.QtCore import QTimer, QObject
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys, datetime

class Reloj(QObject):
    def __init__(self):
        super().__init__()
        self.inicializar()

    
    def inicializar(self):
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
w.stop()



    
    

# app = QApplication(sys.argv)
# w = Reloj()
# w.show()
# app.exec_()