# cliente/cliente.py
import socket
import json
from PyQt5.QtCore import QThread, pyqtSignal
import parametros as p

# --- Funciones de Encriptación (Idénticas al servidor) ---

def encrypt(data_bytes, key):
    encrypted = bytearray()
    for i in range(len(data_bytes)):
        encrypted.append(data_bytes[i] ^ key[i % len(key)])
    return bytes(encrypted)

def decrypt(encrypted_bytes, key):
    decrypted = bytearray()
    for i in range(len(encrypted_bytes)):
        decrypted.append(encrypted_bytes[i] ^ key[i % len(key)])
    return bytes(decrypted)

# --- Hilo de Red ---

class ClientSocketThread(QThread):
    """
    Este hilo maneja la comunicación de red.
    Hereda de QThread para correr en paralelo a la GUI.
    """
    # Define señales para comunicarse con la ventana principal 
    game_state_received = pyqtSignal(dict)
    player_id_received = pyqtSignal(int)
    connection_lost = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_running = True

    def run(self):
        """El corazón del hilo. Se conecta y escucha mensajes."""
        try:
            self.client_socket.connect((p.HOST, p.PORT))
            print("Conectado al servidor.")
        except socket.error as e:
            print(f"No se pudo conectar: {e}")
            self.connection_lost.emit()
            return

        # Escuchar primero por el ID de jugador
        try:
            id_data = self.client_socket.recv(1024)
            decrypted_id_data = decrypt(id_data, p.XOR_KEY)
            id_message = json.loads(decrypted_id_data.decode('utf-8'))
            if id_message['type'] == 'assign_id':
                self.player_id_received.emit(id_message['player_id'])
        except Exception as e:
            print(f"Error recibiendo ID: {e}")
            self.connection_lost.emit()
            return

        # Bucle principal de escucha
        while self.is_running:
            try:
                # Recibir los 4 bytes del largo
                message_len_bytes = self.client_socket.recv(4)
                if not message_len_bytes:
                    break
                message_len = int.from_bytes(message_len_bytes, 'little')

                # Recibir el mensaje completo
                data_buffer = bytearray()
                while len(data_buffer) < message_len:
                    packet = self.client_socket.recv(message_len - len(data_buffer))
                    if not packet:
                        raise socket.error("Conexión perdida")
                    data_buffer.extend(packet)
                
                # Desencriptar y decodificar
                decrypted_data = decrypt(data_buffer, p.XOR_KEY)
                game_state = json.loads(decrypted_data.decode('utf-8'))
                
                # Emitir la señal a la GUI
                self.game_state_received.emit(game_state)

            except (socket.error, json.JSONDecodeError, UnicodeDecodeError):
                print("Conexión perdida con el servidor.")
                self.connection_lost.emit()
                break
        
        self.client_socket.close()

    def send_message(self, message_dict):
        """Envía un mensaje (diccionario) al servidor."""
        try:
            message_json = json.dumps(message_dict)
            encrypted_message = encrypt(message_json.encode('utf-8'), p.XOR_KEY)
            self.client_socket.sendall(encrypted_message)
        except socket.error:
            # La conexión ya podría estar cerrada
            pass
            
    def stop(self):
        self.is_running = False