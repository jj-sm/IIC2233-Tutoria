¡Claro! Recrear Pong es un proyecto excelente y clásico para una tutoría, ya que permite ilustrar de forma práctica varios conceptos complejos de "Programación Avanzada" en un tiempo acotado.

Basándome en los conceptos que mencionaste (PyQt5, Sockets, XOR) y la necesidad de que sea una tutoría de 1 hora, he preparado un "enunciado" y un conjunto de código base.

La clave para una tutoría de 1 hora es **no programar todo desde cero**, sino partir de un código funcional y explicar las "piezas" clave que lo hacen funcionar, especialmente las conexiones entre ellas.

Aquí tienes el material para la tutoría.

---

## 🎲 Enunciado: Tutoría de Pong Multijugador

**Objetivo:** Analizar y comprender la arquitectura de una aplicación cliente-servidor en tiempo real usando Python.

**Duración:** 60 minutos.

**Conceptos Clave:**
1.  **Arquitectura Cliente-Servidor:** Entender por qué el servidor debe ser la "autoridad" que centraliza la lógica del juego (posición de la pelota, puntajes), tal como un servidor de casino maneja el saldo y las reglas del juego.
2.  **Sockets (Networking):** Cómo los clientes y el servidor establecen una conexión TCP/IP para comunicarse.
3.  **Threading:** La necesidad de hilos para manejar tareas concurrentes:
    * **Servidor:** Aceptar múltiples clientes y ejecutar el "game loop" simultáneamente.
    * **Cliente:** Escuchar mensajes del servidor en un hilo (usando `QThread`) para no congelar la interfaz gráfica (GUI).
4.  **Protocolo de Comunicación:** Serializar datos (con JSON) y aplicar una encriptación simple (XOR) para practicar el manejo de bytes.
5.  **PyQt5 y Señales:** Cómo la GUI (front-end) se comunica con la lógica de red (back-end) del cliente usando señales (`pyqtSignal`) para mantener un bajo acoplamiento.

### Estructura de la Tutoría (60 min)

* **(0-10 min) Arquitectura y Setup:**
    * Explicar el modelo: 1 Servidor (árbitro), 2 Clientes (jugadores).
    * Revisar la estructura de archivos (`cliente/`, `servidor/`) y `parametros.py`.
    * Definir el protocolo de comunicación: usaremos JSON para la estructura y encriptación XOR para la capa de transporte.

* **(10-25 min) Foco en el Servidor:**
    * `main.py`: El "lobby". Acepta conexiones de sockets y asigna hilos.
    * Lógica de Hilos: Un hilo para el "game loop" (actualiza la física de la pelota) y un hilo por cliente (para escuchar sus movimientos).
    * Lógica del Juego: El servidor calcula *toda* la física. A esto se le llama "server-side authority".
    * Transmisión: El servidor "transmite" (broadcast) el estado del juego a todos los clientes varias veces por segundo.

* **(25-45 min) Foco en el Cliente (La parte más importante):**
    * `main.py`: Inicia la app PyQt5.
    * `ventana_juego.py` (Front-end): La clase `PongWindow` que hereda de `QWidget`.
        * `paintEvent`: Dibuja el juego (pelota, paletas) basándose en variables locales.
        * `keyPressEvent`: Captura W/S y actualiza la posición *local* de la paleta. Llama a una función para enviar el movimiento al servidor.
    * `cliente.py` (Back-end): La clase `ClientSocketThread` que hereda de `QThread`.
        * **La "Magia"**: El `run()` de este hilo se conecta al socket y entra en un bucle `while True`, esperando mensajes del servidor.
        * **Señal**: Define un `pyqtSignal` (ej: `estado_recibido = pyqtSignal(dict)`).
        * **Emisión**: Cuando recibe un mensaje del servidor, lo desencripta, lo decodifica y *emite* la señal con los datos del juego.
    * **Conexión**: En `PongWindow`, conectamos la señal del hilo (`self.hilo_socket.estado_recibido.connect(self.actualizar_juego)`).
    * `actualizar_juego(self, estado)`: Este "slot" recibe los datos del hilo y actualiza las variables locales (ej: `self.pelota_pos = estado['pelota']`). Finalmente, llama a `self.update()` para forzar un redibujado.

* **(45-55 min) Foco en la Encriptación (Manejo de Bytes):**
    * Mostrar las funciones `encrypt` y `decrypt`.
    * Explicar cómo se aplica el operador XOR byte a byte usando una clave repetida.
    * **Importante**: Mostrar que el `socket.send()` y `socket.recv()` trabajan con `bytes`, no con `str` ni `dict`. Por eso serializamos (JSON -> str -> bytes) y luego encriptamos (bytes -> bytes).

* **(55-60 min) Resumen y Preguntas:**
    * Recalcar la separación front-end/back-end en el cliente y cómo `QThread` y `pyqtSignal` son la "bisagra" que los une.

---

## 📁 Código Base para la Tutoría

Estructura de archivos:

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

### 1. `parametros.py` (Compartido)

```python
# parametros.py
# Este archivo define constantes que usan tanto el cliente como el servidor.

# --- Conexión ---
# Usamos localhost (127.0.0.1) para pruebas locales.
HOST = "127.0.0.1"
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
```

### 2. `servidor/main.py`

Maneja la lógica del juego y las conexiones.

### 3. `cliente/`

Esta es la aplicación PyQt5. La dividimos en 3 archivos para respetar la separación de responsabilidades (front-end/back-end).

#### `cliente/cliente.py` (Back-end)

Este archivo maneja la conexión de red en un hilo separado (`QThread`) para no bloquear la GUI.

#### `cliente/ventana_juego.py` (Front-end)

Esta es la ventana de PyQt5. Dibuja el juego y maneja la entrada del teclado.


#### `cliente/main.py` (Punto de entrada)

Este archivo solo inicia la aplicación PyQt5.


### Cómo ejecutar la tutoría:

1.  **Ejecuta el servidor:** Abre una terminal y corre `python servidor/main.py`.
2.  **Ejecuta el Cliente 1:** Abre *otra* terminal y corre `python cliente/main.py`.
3.  **Ejecuta el Cliente 2:** Abre una *tercera* terminal y corre `python cliente/main.py`.

El juego comenzará automáticamente cuando ambos clientes se conecten. El primer cliente controlará la paleta izquierda con W/S y el segundo la paleta derecha con W/S.