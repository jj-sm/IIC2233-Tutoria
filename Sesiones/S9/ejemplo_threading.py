import threading
import time

def tarea(nombre: str, duracion: int) -> None:
    print(f'Tarea {nombre} iniciada.')
    time.sleep(duracion)
    print(f'Tarea {nombre} finalizada.')
    new_thread = threading.Thread(target=tarea, args=('C', 1))
    new_thread.start()
    


thread_1 = threading.Thread(target=tarea, args=('A', 2))
thread_2 = threading.Thread(target=tarea, args=('B', 3))

