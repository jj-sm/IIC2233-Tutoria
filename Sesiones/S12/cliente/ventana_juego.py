# cliente/ventana_juego.py
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QBrush
from cliente import ClientSocketThread
import parametros as p

class PongWindow(QWidget):
    """Ventana principal del juego (Front-End)[cite: 20]."""
    
    def __init__(self):
        super().__init__()
        # Estado local del juego (se actualiza por el hilo de red)
        self.player_id = -1
        self.game_state = {
            'ball': [p.WINDOW_WIDTH // 2, p.WINDOW_HEIGHT // 2],
            'paddles': [p.WINDOW_HEIGHT // 2 - p.PADDLE_HEIGHT // 2] * 2,
            'score': [0, 0]
        }
        
        self.init_ui()
        self.setup_backend()

    def init_ui(self):
        self.setGeometry(100, 100, p.WINDOW_WIDTH, p.WINDOW_HEIGHT)
        self.setWindowTitle('Tutoría Pong - Cliente')
        self.setStyleSheet("background-color: black;")
        # Habilitar la recepción de eventos de teclado
        self.setFocusPolicy(Qt.StrongFocus)
        self.show()

    def setup_backend(self):
        """Inicia y conecta el hilo de red (Back-End)."""
        self.network_thread = ClientSocketThread()
        
        # Conectar las señales del hilo a los "slots" (métodos) de esta ventana
        self.network_thread.player_id_received.connect(self.set_player_id)
        self.network_thread.game_state_received.connect(self.update_game_state)
        self.network_thread.connection_lost.connect(self.close) # Cerrar si se pierde conexión
        
        self.network_thread.start()

    # --- Slots (Métodos que reciben señales) ---

    def set_player_id(self, player_id):
        self.player_id = player_id
        self.setWindowTitle(f'Tutoría Pong - Jugador {player_id + 1}')

    def update_game_state(self, new_state):
        """Este método es llamado por el hilo de red."""
        self.game_state = new_state
        # Forzar un redibujado de la ventana
        self.update()

    # --- Eventos de la GUI ---

    def keyPressEvent(self, event):
        """Maneja el input del teclado."""
        if self.player_id == -1:
            return # Aún no estamos listos

        key = event.key()
        current_y = self.game_state['paddles'][self.player_id]
        
        if key == Qt.Key_W:
            current_y -= 20 # Movemos la paleta 20px
        elif key == Qt.Key_S:
            current_y += 20
        
        # Limitar el movimiento a la ventana
        current_y = max(0, min(current_y, p.WINDOW_HEIGHT - p.PADDLE_HEIGHT))
        
        # Actualizar estado local (para respuesta inmediata)
        self.game_state['paddles'][self.player_id] = current_y
        
        # Enviar el movimiento al servidor
        self.network_thread.send_message({
            'type': 'move',
            'y': current_y
        })
        self.update() # Redibujar localmente

    def paintEvent(self, event):
        """Dibuja todos los elementos en la pantalla."""
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor("white")))
        painter.setPen(Qt.NoPen)

        # Dibujar paleta 1 (Jugador 1)
        p1_y = self.game_state['paddles'][0]
        painter.drawRect(0, p1_y, p.PADDLE_WIDTH, p.PADDLE_HEIGHT)

        # Dibujar paleta 2 (Jugador 2)
        p2_y = self.game_state['paddles'][1]
        painter.drawRect(p.WINDOW_WIDTH - p.PADDLE_WIDTH, p2_y, p.PADDLE_WIDTH, p.PADDLE_HEIGHT)

        # Dibujar pelota
        ball_x, ball_y = self.game_state['ball']
        painter.drawEllipse(ball_x, ball_y, p.BALL_SIZE, p.BALL_SIZE)

        # Dibujar puntaje (Opcional, pero útil)
        painter.setPen(Qt.white)
        painter.setFont(QApplication.font())
        painter.drawText(p.WINDOW_WIDTH // 4, 50, f"{self.game_state['score'][0]}")
        painter.drawText(p.WINDOW_WIDTH * 3 // 4, 50, f"{self.game_state['score'][1]}")

    def closeEvent(self, event):
        """Asegurarse de detener el hilo al cerrar la ventana."""
        self.network_thread.stop()
        event.accept()