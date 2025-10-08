import sys
from PyQt5.QtWidgets import QApplication
from frontend.frontend_client import VentanaCliente
from frontend.frontend_admin import VentanaAdmin
from backend.backend import LogicaBackend

if __name__ == '__main__':
    # Configuración de hook para capturar excepciones de PyQt5 (útil para debugging)
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication(sys.argv)

    # 1. Crear el Backend (Lógica)
    logica = LogicaBackend()

    # 2. Crear los Frontends (Interfaces)
    cliente = VentanaCliente()
    admin = VentanaAdmin()

    # 3. Conexiones Cliente (Front-end) <-> Backend
    # Cliente (emite voto) -> Backend (recibe voto)
    cliente.senal_votar.connect(logica.recibir_voto)
    
    # 4. Conexiones Admin (Front-end) <-> Backend
    # Admin (pide conteo) -> Backend (inicia hilo)
    admin.senal_iniciar_conteo.connect(logica.iniciar_conteo)

    # 5. Conexiones Backend (Lógica) <-> Admin (Front-end)
    # 5a. Conexión de la señal asíncrona (desde el thread) al slot de la GUI
    # Backend (emite resultados) -> Admin (actualiza GUI)
    logica.senal_resultado_conteo.connect(admin.actualizar_conteo) 
    
    # 5b. Conexión de señales de estado del hilo
    logica.senal_conteo_iniciado.connect(admin.mostrar_conteo_iniciado)
    logica.senal_conteo_finalizado.connect(admin.mostrar_conteo_finalizado)
    
    cliente.show()
    admin.show()

    sys.exit(app.exec_())