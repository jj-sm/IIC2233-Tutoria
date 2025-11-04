import threading
import time
from datetime import datetime

def reloj() -> None:
    while True:
        hora_actual = datetime.now()
        time.sleep(1)
        print(hora_actual.strftime('%H:%M:%S'))

thread_main = threading.Thread(target=reloj)
thread_main.start()