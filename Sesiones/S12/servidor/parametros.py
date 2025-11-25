# parametros.py
# Este archivo define constantes que usan tanto el cliente como el servidor.

# --- Conexión ---
# Usamos localhost (127.0.0.1) para pruebas locales.
HOST = "0.0.0.0"
PORT = 3490

# --- Encriptación ---
# Esta es nuestra clave secreta para la encriptación XOR.
# Debe ser de tipo bytes.
XOR_KEY = b"mi_llave_secreta_123"

# --- Juego ---
# Dimensiones de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Dimensiones de las paletas y la pelota
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 10

# Velocidad de la pelota
BALL_SPEED_X = 4
BALL_SPEED_Y = 4