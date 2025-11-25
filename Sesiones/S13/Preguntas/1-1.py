import threading


def thread_A(evento, lock):
    evento.wait()
    lock.acquire()
    print("A")


def thread_B(lock):
    lock.acquire()
    print("B")


def thread_C(evento, lock):
    evento.set()
    print("C")
    lock.release()

evento = threading.Event()
lock = threading.Lock()

thread_a = threading.Thread(target=thread_A, args=(evento, lock))
thread_b = threading.Thread(target=thread_B, args=(lock, ))
thread_c = threading.Thread(target=thread_C, args=(evento, lock))

thread_a.start()
thread_b.start()
thread_b.join()
thread_c.start()