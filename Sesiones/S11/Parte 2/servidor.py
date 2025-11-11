# servidor.py
import socket
import json

HOST = "127.0.0.1"
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")

    conn, addr = s.accept()
    print("Cliente conectado:", addr)

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            mensaje = json.loads(data.decode())
            print("Recibido:", mensaje)

            respuesta = "recibido".encode()
            conn.sendall(respuesta)
