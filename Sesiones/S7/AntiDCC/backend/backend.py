import threading
import time
from PyQt5.QtCore import QObject, pyqtSignal

# Simulación de la función pesada de conteo que se ejecuta en el thread secundario.
def tarea_pesada_conteo(votos, senal_retorno):
    """
    Se ejecuta en un thread secundario. Simula un conteo largo.
    """
    print("Backend: Hilo Conteo: Iniciando tarea pesada de conteo (5s)...")
    # TODO ESTUDIANTE 3 - 1: Simular el trabajo pesado
    time.sleep(5)
    candidato_A = votos.get('A', 0)
    candidato_B = votos.get('B', 0)
    print(f"Backend: Hilo Conteo: Conteo finalizado. A={candidato_A}, B={candidato_B}")
    # TODO ESTUDIANTE 3 - 2: Emitir la señal de resultado al thread principal
    resultado = {'A': candidato_A, 'B': candidato_B}
    senal_retorno.emit(resultado)

class LogicaBackend(QObject):
    senal_resultado_conteo = pyqtSignal(dict)
    senal_conteo_iniciado = pyqtSignal()
    senal_conteo_finalizado = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.votos = {'A': 0, 'B': 0}
        self.conteo_activo = False
        print("Backend: Lógica inicializada.")

    def recibir_voto(self, candidato):
        # TODO ESTUDIANTE 3 - 5: Backend recibe voto del cliente
        print(f"Backend: Recibiendo voto para {candidato}")
        if candidato in self.votos:
            self.votos[candidato] += 1
            print(f"Backend: Voto registrado! Totales: {self.votos}")
        else:
            print(f"Backend: Error, candidato '{candidato}' no válido.")

    def iniciar_conteo(self):
        # TODO ESTUDIANTE 3 - 3: Instanciar el hilo de trabajo
        if self.conteo_activo:
            print("Backend: Conteo ya activo. Esperando...")
            return
        print("Backend: Iniciando conteo en thread secundario.")
        self.conteo_activo = True
        self.senal_conteo_iniciado.emit()
        self.thread_conteo = threading.Thread(
            target=tarea_pesada_conteo, 
            args=(self.votos, self.senal_resultado_conteo)
        )
        # TODO ESTUDIANTE 3 - 4: Comenzar el hilo de trabajo
        print("Backend: Lanzando hilo de conteo.")
        self.thread_conteo.start()
        # Permitir múltiples conteos sucesivos
        self.conteo_activo = False
        self.senal_conteo_finalizado.emit()
        print("Backend: Conteo marcado como finalizado.")