import threading
import time
from PyQt5.QtCore import QObject, pyqtSignal

# Simulación de la función pesada de conteo que se ejecuta en el thread secundario.
def tarea_pesada_conteo(votos, senal_retorno):
    """
    Se ejecuta en un thread secundario. Simula un conteo largo.
    """
    print("Hilo Conteo: Iniciando tarea pesada de conteo (5s)...")
    
    # 🛑 SOLUCIÓN ESTUDIANTE 3 - 1: Simular el trabajo pesado
    time.sleep(5)

    # Lógica del conteo final
    candidato_A = votos.get('A', 0)
    candidato_B = votos.get('B', 0)

    print(f"Hilo Conteo: Conteo finalizado. A={candidato_A}, B={candidato_B}")

    # 🛑 SOLUCIÓN ESTUDIANTE 3 - 2: Emitir la señal de resultado al thread principal
    # El payload es un diccionario con los resultados
    resultado = {'A': candidato_A, 'B': candidato_B}
    senal_retorno.emit(resultado)

class LogicaBackend(QObject):
    # Señal para enviar el resultado del conteo (desde el thread secundario) al Main Thread/GUI
    senal_resultado_conteo = pyqtSignal(dict)

    # Señal para notificar a la GUI que el conteo ha iniciado/finalizado
    senal_conteo_iniciado = pyqtSignal()
    senal_conteo_finalizado = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.votos = {'A': 0, 'B': 0}
        self.conteo_activo = False

    def recibir_voto(self, candidato):
        """Slot que recibe votos de la Ventana Cliente."""
        if candidato in self.votos:
            self.votos[candidato] += 1
            print(f"Backend: Voto recibido para {candidato}. Totales: {self.votos}")
        else:
            print(f"Backend: Error, candidato '{candidato}' no válido.")

    def iniciar_conteo(self):
        """Slot que se activa desde la Ventana Admin para iniciar el conteo asíncrono."""
        if self.conteo_activo:
            print("Backend: Conteo ya activo. Esperando...")
            return

        print("Backend: Iniciando conteo en thread secundario.")
        self.conteo_activo = True
        self.senal_conteo_iniciado.emit() # Notifica a la GUI Admin

        # 🛑 SOLUCIÓN ESTUDIANTE 3 - 3: Instanciar el hilo de trabajo
        self.thread_conteo = threading.Thread(
            target=tarea_pesada_conteo, 
            args=(self.votos, self.senal_resultado_conteo)
        )

        # 🛑 SOLUCIÓN ESTUDIANTE 3 - 4: Comenzar el hilo de trabajo
        self.thread_conteo.start()

        # Nota: La actualización de 'conteo_activo' se hace aquí para permitir 
        # múltiples conteos sucesivos, aunque el thread aún esté en ejecución.
        # En una solución más robusta, se usaría .join() o .is_alive() para reestablecer.
        self.conteo_activo = False
        self.senal_conteo_finalizado.emit()