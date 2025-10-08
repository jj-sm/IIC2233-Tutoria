import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QDesktopWidget, QLineEdit,
                             QPushButton, QLabel, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt


class MiVentana(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_superior_izq, y_superior_izq, ancho, alto)
        self.setGeometry(0,0,300,300)
        self.setMinimumSize(300, 300)
        self.setMaximumSize(600, 600)

        self.inicializador()

        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.center()

        # Podemos dar nombre a la ventana (Opcional).
        self.setWindowTitle('Mi Primera Ventana')

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


    def inicializador(self) -> None:
        main_v_box = QVBoxLayout()
        h_box = QHBoxLayout()
        v_box = QVBoxLayout()

        self.boton_1 = QPushButton('Botón 1', self)
        self.label = QLabel('Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto Texto'
                       ' Texto Texto Texto Texto Texto Texto Texto Texto', self)
        self.label.setWordWrap(True)
        self.line_edit = QLineEdit('Texto Inicial', self)
        self.boton_1.clicked.connect(self.cambiar_texto)

        h_box_2 = QHBoxLayout()
        h_box_2.addWidget(self.boton_1)
        h_box_2.addWidget(self.line_edit)

        v_box.addWidget(self.label)
        h_box.addLayout(v_box)

        main_v_box.addLayout(h_box_2)
        main_v_box.addLayout(h_box)

        self.setLayout(main_v_box)

    def cambiar_texto(self) -> None:
        print('Botón presionado')
        texto = self.line_edit.text()
        self.label.setText(texto)




if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())

