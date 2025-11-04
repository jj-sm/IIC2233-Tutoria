from PyQt5.QtCore import QThread

class HiloPyQt(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(3):
            print(f"QThread ejecutando... {i}")
            self.msleep(1000)  # versión segura de sleep

hilo_qt = HiloPyQt()
hilo_qt.start()
hilo_qt.wait()