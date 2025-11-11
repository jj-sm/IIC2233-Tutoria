# servidor/main.py
import socket
import threading
import time
import json
import parametros as p

# --- Funciones de Encriptación ---
# Estas funciones replican el concepto de encriptación XOR 
# pero de forma más simple que el protocolo de la Tarea 4.

def encrypt(data_bytes, key):
    """Encripta bytes usando una clave XOR repetida."""
    encrypted = bytearray()
    for i in range(len(data_bytes)):
        encrypted.append(data_bytes[i] ^ key[i % len(key)])
    return bytes(encrypted)

def decrypt(encrypted_bytes, key):
    """Desencripta bytes usando una clave XOR repetida."""
    decrypted = bytearray()
    for i in range(len(encrypted_bytes)):
        decrypted.append(encrypted_bytes[i] ^ key[i % len(key)])
    return bytes(decrypted)

# --- Lógica del Servidor ---

# Almacenamos las conexiones de los clientes
clients = []
game_state = {
    'ball': [p.WINDOW_WIDTH // 2, p.WINDOW_HEIGHT // 2],
    'ball_vel': [p.BALL_SPEED_X, p.BALL_SPEED_Y],
    'paddles': [p.WINDOW_HEIGHT // 2 - p.PADDLE_HEIGHT // 2, 
                p.WINDOW_HEIGHT // 2 - p.PADDLE_HEIGHT // 2],
    'score': [0, 0]
}

def update_game_state():
    """Actualiza la física de la pelota y revisa colisiones."""
    global game_state

    # Mover la pelota
    game_state['ball'][0] += game_state['ball_vel'][0]
    game_state['ball'][1] += game_state['ball_vel'][1]

    ball_x, ball_y = game_state['ball']
    vel_x, vel_y = game_state['ball_vel']

    # Colisión con paredes (arriba/abajo)
    if ball_y <= 0 or ball_y >= p.WINDOW_HEIGHT - p.BALL_SIZE:
        game_state['ball_vel'][1] *= -1

    # Colisión con paleta 1 (izquierda)
    p1_y = game_state['paddles'][0]
    if (ball_x <= p.PADDLE_WIDTH and 
        p1_y <= ball_y <= p1_y + p.PADDLE_HEIGHT):
        game_state['ball_vel'][0] *= -1

    # Colisión con paleta 2 (derecha)
    p2_y = game_state['paddles'][1]
    if (ball_x >= p.WINDOW_WIDTH - p.PADDLE_WIDTH - p.BALL_SIZE and 
        p2_y <= ball_y <= p2_y + p.PADDLE_HEIGHT):
        game_state['ball_vel'][0] *= -1

    # Anotación (Punto)
    if ball_x < 0:
        game_state['score'][1] += 1
        reset_ball()
    elif ball_x > p.WINDOW_WIDTH:
        game_state['score'][0] += 1
        reset_ball()

def reset_ball():
    game_state['ball'] = [p.WINDOW_WIDTH // 2, p.WINDOW_HEIGHT // 2]
    game_state['ball_vel'] = [p.BALL_SPEED_X, p.BALL_SPEED_Y] # Reiniciar dirección

def game_loop():
    """Bucle principal del juego que actualiza y transmite el estado."""
    while True:
        update_game_state()
        broadcast(game_state)
        time.sleep(1/10)

def broadcast(message):
    """Envía un mensaje a todos los clientes conectados."""
    message_json = json.dumps(message)
    message_bytes = message_json.encode('utf-8')
    encrypted_message = encrypt(message_bytes, p.XOR_KEY)
    
    # Preparamos el mensaje con su largo (similar al protocolo T4 [cite: 421])
    # Usamos 4 bytes, 'little' endian
    message_len = len(encrypted_message).to_bytes(4, 'little')
    
    for client_socket in clients:
        try:
            print(message)
            print(message_len + encrypted_message)
            client_socket.sendall(message_len + encrypted_message)
        except socket.error:
            # Si hay error, el cliente se desconectó
            clients.remove(client_socket)

def handle_client(conn, player_id):
    """Maneja la conexión de un cliente específico."""
    print(f"Jugador {player_id + 1} conectado.")
    
    # Informar al cliente su ID
    id_message = json.dumps({'type': 'assign_id', 'player_id': player_id})
    conn.sendall(encrypt(id_message.encode('utf-8'), p.XOR_KEY))

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            
            decrypted_data = decrypt(data, p.XOR_KEY)
            message = json.loads(decrypted_data.decode('utf-8'))
            
            if message['type'] == 'move':
                game_state['paddles'][player_id] = message['y']
                
        except (socket.error, json.JSONDecodeError, UnicodeDecodeError):
            break
            
    print(f"Jugador {player_id + 1} desconectado.")
    if conn in clients:
        clients.remove(conn)
    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((p.HOST, p.PORT))
    server.listen()
    print(f"Servidor Pong escuchando en {p.HOST}:{p.PORT}")

    # Iniciar el bucle del juego en un hilo separado
    game_thread = threading.Thread(target=game_loop, daemon=True)
    game_thread.start()

    player_count = 0
    while player_count <= 2:
        conn, addr = server.accept()
        clients.append(conn)
        
        client_thread = threading.Thread(target=handle_client, args=(conn, player_count), daemon=True)
        client_thread.start()
        
        player_count += 1
        
    print("Juego iniciado. (El servidor seguirá aceptando más conexiones si se modifica)")
    # El servidor principal solo acepta, los hilos manejan el resto.

if __name__ == "__main__":
    main()