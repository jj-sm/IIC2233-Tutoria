## Enunciado: Tutoría Interactiva de Pong Multijugador

**Objetivo:** Implementar las piezas clave de una aplicación cliente-servidor en tiempo real, conectando la lógica de red (back-end) con una interfaz gráfica (front-end).

**Duración:** 60 minutos.

**Conceptos Clave:**
1.  **Arquitectura Cliente-Servidor:** Entender por qué el servidor debe ser la "autoridad" del juego.
2.  **Sockets (Networking):** Implementar la creación, conexión y comunicación de sockets TCP/IP.
3.  **Threading (`Thread` y `QThread`):** Usar hilos para manejar tareas concurrentes (el "game loop" y la escucha de red) sin congelar la aplicación.
4.  **Protocolo de Comunicación:** Serializar datos (JSON), manejar bytes y aplicar encriptación (XOR).
5.  **PyQt5 y Señales:** Definir y conectar señales (`pyqtSignal`) para comunicar el hilo de red (back-end) con la ventana (front-end) de forma desacoplada.

### Estructura de la Tutoría

* **Arquitectura y Setup:**
    * Explicar el modelo: 1 Servidor, 2 Clientes (jugadores).
    * Revisar la estructura de archivos (`cliente/`, `servidor/`) y `parametros.py`.
    * Analizar el protocolo: `[4 bytes largo] + [data encriptada]`.

* **Foco en el Servidor (Completar `servidor/main.py`):**
    * **Tarea 1:** Implementar la función `main()`, creando, enlazando (`bind`) y poniendo a escuchar (`listen`) el socket principal.
    * **Tarea 2:** Completar el bucle `while` en `main()` para que acepte (`accept`) nuevas conexiones.
    * **Tarea 3:** Completar `handle_client` para recibir (`recv`), desencriptar y decodificar los mensajes del cliente.

* **Foco en el Cliente (Completar `cliente/cliente.py`):**
    * **Tarea 4:** Definir las `pyqtSignal` necesarias en `ClientSocketThread` para informar a la GUI.
    * **Tarea 5:** Completar el método `run()` para conectarse (`connect`) al servidor.
    * **Tarea 6:** Implementar el bucle de recepción en `run()`, manejando el protocolo (leer 4 bytes de largo, leer el resto), desencriptando y *emitiendo* la señal con los datos.

* **Foco en la Encriptación y Conexión (Completar `cliente/` y `servidor/`):**
    * **Tarea 7:** Implementar la función `encrypt` (la lógica es inversa a `decrypt`).
    * **Tarea 8:** Completar `send_message` (cliente) y `broadcast` (servidor) para usar la función `encrypt` y enviar datos.
    * **Tarea 9:** En `cliente/ventana_juego.py`, *conectar* las señales definidas en la Tarea 4 a los "slots" (métodos) de la ventana.

* **Resumen y Pruebas:**
    * Recalcar cómo `QThread` y `pyqtSignal` son la "bisagra" que une la red con la GUI.
    * Probar el juego.

---

## Código Base

Aquí está el código con las secciones a completar.

```
Tutorial_Pong/
├── cliente/
│   ├── __init__.py
│   ├── main.py
│   ├── cliente.py
│   └── ventana_juego.py
├── servidor/
│   ├── __init__.py
│   └── main.py
└── parametros.py
```

### 1. `parametros.py` (Completo)

Este archivo se entrega completo.

```python
# parametros.py
# Este archivo define constantes que usan tanto el cliente como el servidor.

# --- Conexión ---
HOST = "127.0.0.1"
PORT = 3490

# --- Encriptación ---
XOR_KEY = b"mi_llave_secreta_123"

# --- Juego ---
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 10
BALL_SPEED_X = 4
BALL_SPEED_Y = 4
```

### 2. `servidor/main.py` (Para completar)

### 3. `cliente/cliente.py` (Para completar)

Combina `QThread`, señales y sockets.

### 4. `cliente/ventana_juego.py` (Para completar)

### 5. `cliente/main.py` (Completo)

Este archivo se entrega completo.

```python
# cliente/main.py
import sys
from PyQt5.QtWidgets import QApplication
from ventana_juego import PongWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PongWindow()
    sys.exit(app.exec_())
```

### Cómo ejecutar la tutoría:

1.  **Ejecuta el servidor:** Abre una terminal y corre `python servidor/main.py`.
2.  **Ejecuta el Cliente 1:** Abre *otra* terminal y corre `python cliente/main.py`.
3.  **Ejecuta el Cliente 2:** Abre una *tercera* terminal y corre `python cliente/main.py`.

El juego comenzará automáticamente cuando ambos clientes se conecten (una vez que el código esté completo).