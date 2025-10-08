import sys
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel
)
from PyQt5.QtCore import pyqtSignal

class VentanaCliente(QWidget):
    senal_votar = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Votación - Cliente")
        print("Cliente: Ventana inicializada.")
        self.inicializar_gui()
        self.conectar_senales()

    def inicializar_gui(self):
        # TODO ESTUDIANTE 1: Inicializar Widgets y Layout
        print("Cliente: Inicializando GUI.")
        vbox_principal = QVBoxLayout(self)
        label_titulo = QLabel("¡Emite tu Voto!")
        label_titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        label_titulo.setFixedHeight(40) 
        self.boton_votar_a = QPushButton("Votar por Candidato A")
        self.boton_votar_b = QPushButton("Votar por Candidato B")
        vbox_principal.addWidget(label_titulo)
        vbox_principal.addWidget(self.boton_votar_a)
        vbox_principal.addWidget(self.boton_votar_b)
        self.setLayout(vbox_principal)

    def conectar_senales(self):
        # TODO ESTUDIANTE 2: Conectar Botones a la Señal de Voto
        print("Cliente: Conectando señales de voto.")
        self.boton_votar_a.clicked.connect(lambda: self.emitir_voto("A"))
        self.boton_votar_b.clicked.connect(lambda: self.emitir_voto("B"))

    def emitir_voto(self, candidato):
        print(f"Cliente: Votando por {candidato}")
        self.senal_votar.emit(candidato)