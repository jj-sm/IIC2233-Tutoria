import sys
from PyQt5.QtWidgets import QWidget, QApplication

class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_superior_izq, y_superior_izq, ancho, alto)
        self.setGeometry(200, 100, 300, 300)

        # Podemos dar nombre a la ventana (Opcional).
        self.setWindowTitle('Mi Primera Ventana')


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())





