import sys
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
)
from PyQt5.QtCore import Qt, pyqtSignal

class VentanaAdmin(QWidget):
    # Señal para pedir al Backend que inicie la tarea pesada de conteo.
    senal_iniciar_conteo = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana de Administración y Conteo")
        self.inicializar_gui()

    def inicializar_gui(self):
        # ----------------------------------------------------
        # 🛑 SOLUCIÓN ESTUDIANTE 4: Inicializar Widgets para Conteo y Layout
        # ----------------------------------------------------

        vbox_principal = QVBoxLayout(self)

        # 1. Crear el botón para iniciar el conteo y conectarlo a la señal
        self.boton_iniciar = QPushButton("Iniciar Conteo Asíncrono")
        # El botón debe emitir la señal directamente al ser presionado.
        self.boton_iniciar.clicked.connect(self.senal_iniciar_conteo.emit)
        
        # 2. Crear los QLabel para mostrar el resultado del Candidato A y B
        self.label_conteo_a = QLabel("Candidato A: 0 votos")
        self.label_conteo_b = QLabel("Candidato B: 0 votos")
        
        # 3. Crear un QLabel para mostrar el estado del conteo (si está activo)
        self.label_estado = QLabel("Estado: Listo para contar")
        
        # 4. Agregar los widgets al layout
        vbox_principal.addWidget(self.boton_iniciar)
        vbox_principal.addWidget(QLabel("--- Resultados ---"))
        vbox_principal.addWidget(self.label_conteo_a)
        vbox_principal.addWidget(self.label_conteo_b)
        vbox_principal.addWidget(QLabel("--- Estado del Hilo ---"))
        vbox_principal.addWidget(self.label_estado)

        self.setLayout(vbox_principal)


    # ----------------------------------------------------
    # 🛑 SOLUCIÓN ESTUDIANTE 4: Slots para actualizar la GUI
    # ----------------------------------------------------
    def actualizar_conteo(self, resultados):
        """Slot que recibe el resultado del thread de conteo."""
        # 5. Actualizar los labels con los valores del diccionario 'resultados'
        self.label_conteo_a.setText(f"Candidato A: {resultados['A']} votos")
        self.label_conteo_b.setText(f"Candidato B: {resultados['B']} votos")
        self.label_estado.setText("Estado: ✅ Conteo finalizado. Resultados actualizados.")
        self.boton_iniciar.setEnabled(True)

    def mostrar_conteo_iniciado(self):
        """Slot que se activa cuando el Backend notifica que el conteo ha iniciado."""
        self.label_estado.setText("Estado: ⏳ Contando votos... La GUI NO está bloqueada.")
        self.boton_iniciar.setEnabled(False)
    
    def mostrar_conteo_finalizado(self):
        """Slot que se activa cuando el Backend notifica que el conteo ha finalizado."""
        pass # Se deja vacío ya que 'actualizar_conteo' es el que actualiza el estado final.