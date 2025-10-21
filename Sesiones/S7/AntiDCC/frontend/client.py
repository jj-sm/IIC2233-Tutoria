import sys
import os
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QDialog, QWidget, QLabel, QPushButton, QApplication,
                             QHBoxLayout, QVBoxLayout, QDesktopWidget)


class VotesWindow(QWidget):
    # TODO: crea una señal llamada sig_votos que emita el nombre del candidato seleccionado

    sig_votos = pyqtSignal(str)
    def __init__(self, parent=None) -> None:
        # TODO: Recuerda añadir la lógica para que un usuario no pueda votar más de una vez

        super().__init__()
        self.parent: QWidget = parent
        self.init_gui()


    def tlp(self, path: str) -> str:
        """
        Esta funcion les permitira testear desde este archivo o desde main para cargar las imagenes
        """
        if self.parent is not None:
            # from main
            return os.path.join('frontend', path)
        return path

    def init_gui(self) -> None:
        """
        Inicia el UI
        # TODO: Coloca un título a la ventana
        """
        self.main_layout()
        self.center()

    def main_layout(self) -> None:
        """
        Esta función da la forma de la ventana de bienvenida
        # TODO: Completa la función agregando QLabels, QButtons y Layouts
        #       para que se vea como en el enunciado para cada candidato.
        """

        self.setWindowTitle("Votaciones Pangüin't")

        main_vbox = QVBoxLayout()

        titulo = QLabel('AntiDCC Conteo de Votos')
        titulo.setAlignment(Qt.AlignCenter)
        mensaje_generico = QLabel('Vota por tu candidato preferido ~')
        mensaje_generico.setAlignment(Qt.AlignCenter)

        main_vbox.addWidget(titulo)
        main_vbox.addWidget(mensaje_generico)
        # CANDIDATOS
        ## Candidato <Flip Flop>
        flipflop = self.create_candiate_box("Flip Flop", "resources/01.png")
        main_vbox.addLayout(flipflop)


        ## Candidato <Los 3 Mishqueteros>
        los_3_mishqueteros = self.create_candiate_box("Los 3 Mishqueteros", "resources/02.png")
        main_vbox.addLayout(los_3_mishqueteros)

        # -------------------------------------------------

        ## Candidato <IIC2233.pop()>


        ## Candidato <y Perry?>


        # -------------------------------------------------


        # -------------------------------------------------


        # TODO: Botón volver
        boton_regresar = QPushButton("Regresar")
        boton_regresar.clicked.connect(self.return_to_welcome)
        main_vbox.addWidget(boton_regresar)
        
        self.setLayout(main_vbox)
        


    def center(self):
        width, height = QDesktopWidget().availableGeometry().width(), QDesktopWidget().availableGeometry().height()
        width_real = (width - 400) // 2
        height_real = (height - 200) // 2
        self.move(width_real, height_real)

    
    def create_candiate_box(self, nombre, path) -> QVBoxLayout:
        vbox = QVBoxLayout()
        imagen = QLabel()
        imagen.setPixmap(QPixmap(self.tlp(path)))
        imagen.setFixedSize(100, 100)
    
        btn = QPushButton(nombre)

        vbox.addWidget(imagen)
        vbox.addWidget(btn)

        # btn.clicked.connect())
        return vbox


    def popup_msg(self) -> None:
        dialog = QDialog(self)
        dialog.setWindowTitle("Voto registrado")
        dialog_layout = QVBoxLayout()
        msg_label = QLabel("Gracias por votar por el Candidato")
        msg_label.setAlignment(Qt.AlignCenter)
        dialog_layout.addWidget(msg_label)
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(dialog.accept)
        dialog_layout.addWidget(ok_button)
        dialog.setLayout(dialog_layout)
        dialog.exec_()


    def error_msg(self) -> None:
        dialog = QDialog(self)
        dialog.setWindowTitle("Ya votaste")
        dialog_layout = QVBoxLayout()
        msg_label = QLabel("Vuelve al menú de bienvenida")
        msg_label.setAlignment(Qt.AlignCenter)
        dialog_layout.addWidget(msg_label)
        ok_button = QPushButton("Volver")
        ok_button.clicked.connect(self.return_to_welcome)
        dialog_layout.addWidget(ok_button)
        dialog.setLayout(dialog_layout)
        dialog.exec_()


    def return_to_welcome(self) -> None:
        """
        # TODO: Crea una funcion que permita regresar a la ventana de bienvenida
        Se devuelve a la ventana de bienvenida
        """
        if self.parent is not None:
            self.parent.show()
        self.close()


    def manage_voting(self, candidate: str) -> None:
        # TODO: Recuerda añadir la lógica para que un usuario no pueda votar más de una vez
        # TODO: Emite la señal sig_votos con el nombre del candidato seleccionado
        # Si ya votó invoca self.error_msg(), sino invoca self.popup_msg()
        ...

if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
        sys.__excepthook__ = hook


    def handle_signal(*args) -> None:
        print(*args)

    app = QApplication([])
    ventana = VotesWindow()
    ventana.show()
    sys.exit(app.exec())