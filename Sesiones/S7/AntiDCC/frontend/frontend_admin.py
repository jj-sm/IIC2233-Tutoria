import sys
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
)
from PyQt5.QtCore import Qt, pyqtSignal

class VentanaAdmin(QWidget):
    senal_iniciar_conteo = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Administración y Conteo")
        print("Admin: Ventana inicializada.")
        self.inicializar_gui()

    def inicializar_gui(self):
        # TODO ESTUDIANTE 4: Inicializar Widgets para Conteo y Layout
        print("Admin: Inicializando GUI.")
        vbox_principal = QVBoxLayout(self)
        self.boton_iniciar = QPushButton("Iniciar Conteo Asíncrono")
        self.boton_iniciar.clicked.connect(self.emitir_conteo)
        self.label_conteo_a = QLabel("Candidato A: 0 votos")
        self.label_conteo_b = QLabel("Candidato B: 0 votos")
        self.label_estado = QLabel("Estado: Listo para contar")
        vbox_principal.addWidget(self.boton_iniciar)
        vbox_principal.addWidget(QLabel("--- Resultados ---"))
        vbox_principal.addWidget(self.label_conteo_a)
        vbox_principal.addWidget(self.label_conteo_b)
        vbox_principal.addWidget(QLabel("--- Estado del Hilo ---"))
        vbox_principal.addWidget(self.label_estado)
        self.setLayout(vbox_principal)

    def emitir_conteo(self):
        print("Admin: Botón de conteo presionado.")
        self.senal_iniciar_conteo.emit()

    def actualizar_conteo(self, resultados):
        # TODO ESTUDIANTE 4: Actualizar resultados en la GUI
        print(f"Admin: Recibiendo resultados {resultados}")
        self.label_conteo_a.setText(f"Candidato A: {resultados['A']} votos")
        self.label_conteo_b.setText(f"Candidato B: {resultados['B']} votos")
        self.label_estado.setText("Estado: ✅ Conteo finalizado. Resultados actualizados.")
        self.boton_iniciar.setEnabled(True)

    def mostrar_conteo_iniciado(self):
        print("Admin: Conteo iniciado (señal recibida).")
        self.label_estado.setText("Estado: ⏳ Contando votos... La GUI NO está bloqueada.")
        self.boton_iniciar.setEnabled(False)
    
    def mostrar_conteo_finalizado(self):
        print("Admin: Conteo finalizado (señal recibida).")
        # Puede dejarse vacío, ya que actualizar_conteo actualiza el estado final.
        pass