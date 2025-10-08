
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QMouseEvent

# Ventana que emite señales
class VentanaEmite(QWidget):
    # Definimos las señales como atributos de clase
    senal_simple = pyqtSignal()           # Signal sin argumentos
    senal_texto = pyqtSignal(str)         # Signal que envía texto
    senal_coordenadas = pyqtSignal(int, int)  # Signal que envía dos ints

    def __init__(self):
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):
        self.label = QLabel("Haz click en la ventana", self)
        self.label.move(20,10)
        self.label.resize(self.label.sizeHint())

        self.entrada = QLineEdit(self)
        self.entrada.move(20, 60)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle("Ventana Emite")
        self.setMouseTracking(True)
        self.show()

    def mousePressEvent(self, event: QMouseEvent):
        self.senal_simple.emit()
        self.senal_texto.emit(self.entrada.text())

    def mouseMoveEvent(self, event: QMouseEvent):
        self.senal_coordenadas.emit(event.pos().x(), event.pos().y())


# Ventana que recibe señales
class VentanaRecibe(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):
        self.label1 = QLabel("", self)
        self.label1.move(20, 10)
        self.label1.resize(self.label1.sizeHint())

        self.label2 = QLabel("", self)
        self.label2.move(20, 40)
        self.label2.resize(self.label2.sizeHint())

        self.label3 = QLabel("", self)
        self.label3.move(20, 70)
        self.label3.resize(self.label3.sizeHint())

        self.setGeometry(700,300,300,150)
        self.setWindowTitle("Ventana Recibe")
        self.show()

    # Slots
    def slot_simple(self):
        self.label1.setText("Se presionó la ventana")
        self.label1.resize(self.label1.sizeHint())

    def slot_texto(self, texto):
        self.label2.setText(f"Texto recibido: {texto}")
        self.label2.resize(self.label2.sizeHint())

    def slot_coordenadas(self, x: int, y: int):
        self.label3.setText(f"Posición mouse: {x}, {y}")
        self.label3.resize(self.label3.sizeHint())


if __name__ == "__main__":
    app = QApplication([])

    emite = VentanaEmite()
    recibe = VentanaRecibe()

    # Conexión de signals a slots
    emite.senal_simple.connect(recibe.slot_simple)
    emite.senal_texto.connect(recibe.slot_texto)
    emite.senal_coordenadas.connect(recibe.slot_coordenadas)

    sys.exit(app.exec())