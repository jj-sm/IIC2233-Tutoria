import sys
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel
)
from PyQt5.QtCore import pyqtSignal

class VentanaCliente(QWidget):
    # Señal para enviar el voto (candidato 'A' o 'B') al Backend
    senal_votar = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Votación - Cliente")
        self.inicializar_gui()
        self.conectar_senales()

    def inicializar_gui(self):
        # ----------------------------------------------------
        # 🛑 SOLUCIÓN ESTUDIANTE 1: Inicializar Widgets y Layout
        # ----------------------------------------------------

        # 1. Crear el layout principal (QVBoxLayout)
        vbox_principal = QVBoxLayout(self)

        # 2. Crear un QLabel para el título
        label_titulo = QLabel("¡Emite tu Voto!")
        label_titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        label_titulo.setFixedHeight(40) 

        # 3. Crear los QPushButtons para los candidatos A y B
        self.boton_votar_a = QPushButton("Votar por Candidato A")
        self.boton_votar_b = QPushButton("Votar por Candidato B")
        
        # 4. Agregar widgets al layout
        vbox_principal.addWidget(label_titulo)
        vbox_principal.addWidget(self.boton_votar_a)
        vbox_principal.addWidget(self.boton_votar_b)

        self.setLayout(vbox_principal)

    def conectar_senales(self):
        # ----------------------------------------------------
        # 🛑 SOLUCIÓN ESTUDIANTE 2: Conectar Botones a la Señal de Voto
        # ----------------------------------------------------
        
        # 1. Conectar el click del botón A a un slot que emita la señal con "A"
        self.boton_votar_a.clicked.connect(lambda: self.senal_votar.emit("A"))

        # 2. Conectar el click del botón B a un slot que emita la señal con "B"
        self.boton_votar_b.clicked.connect(lambda: self.senal_votar.emit("B"))