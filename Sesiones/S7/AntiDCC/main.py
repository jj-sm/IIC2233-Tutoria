import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from frontend.frontend_client import VentanaCliente
from frontend.frontend_admin import VentanaAdmin
from backend.backend import LogicaBackend

class MenuPrincipal(QWidget):
    def __init__(self, cliente, admin):
        super().__init__()
        self.setWindowTitle("Menú Principal - Sistema de Votaciones")
        layout = QVBoxLayout()
        self.boton_cliente = QPushButton("Abrir Ventana de Votación (Cliente)")
        self.boton_admin = QPushButton("Abrir Ventana de Administración")
        layout.addWidget(self.boton_cliente)
        layout.addWidget(self.boton_admin)
        self.setLayout(layout)

        # TODO ESTUDIANTE 1: Conectar botón cliente
        self.boton_cliente.clicked.connect(lambda: self.abrir_submenu(cliente))
        # TODO ESTUDIANTE 4: Conectar botón admin
        self.boton_admin.clicked.connect(lambda: self.abrir_submenu(admin))

    def abrir_submenu(self, ventana):
        print(f"Menú: Abriendo ventana {ventana.windowTitle()}")
        ventana.show()

if __name__ == '__main__':
    def hook(type, value, traceback):
        print("Excepción capturada:", type, value)
        print(traceback)
    sys.excepthook = hook

    app = QApplication(sys.argv)
    print("Main: Creando backend y ventanas.")

    logica = LogicaBackend()
    cliente = VentanaCliente()
    admin = VentanaAdmin()

    # Conexiones Cliente <-> Backend
    cliente.senal_votar.connect(logica.recibir_voto)

    # Conexiones Admin <-> Backend
    admin.senal_iniciar_conteo.connect(logica.iniciar_conteo)

    # Backend -> Admin (resultados)
    logica.senal_resultado_conteo.connect(admin.actualizar_conteo)
    logica.senal_conteo_iniciado.connect(admin.mostrar_conteo_iniciado)
    logica.senal_conteo_finalizado.connect(admin.mostrar_conteo_finalizado)

    menu = MenuPrincipal(cliente, admin)
    menu.show()

    print("Main: Lanzando aplicación.")
    sys.exit(app.exec_())