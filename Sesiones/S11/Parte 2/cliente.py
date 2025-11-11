# cliente.py
import socket
import json

HOST = "127.0.0.1"
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        texto = input("Ingresa un mensaje: ")
        dic = {"mensaje": texto}

        s.sendall(json.dumps(dic).encode())
        resp = s.recv(1024)
        print("Respuesta del servidor:", resp.decode())
