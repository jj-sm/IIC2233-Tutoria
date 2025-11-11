import sys
import random
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class Ruleta(QWidget):
    def __init__(self, players, png_path="Sesiones/S11/Parte 4/resources/named_wheel.png"):
        super().__init__()

        self.players = players
        self.slice_angle = 360 / len(players)

        # Rotación
        self.angle = 0
        self.speed = 0
        self.deceleration = 0.05

        # Imagen
        self.original_pixmap = QPixmap(png_path)
        self.label = QLabel()
        self.label.setPixmap(self.original_pixmap)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMinimumSize(200, 200)
        self.label.setScaledContents(True)

        # Ganador
        self.result_label = QLabel("Ganador: —")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Botón girar
        self.spin_button = QPushButton("Girar")
        self.spin_button.clicked.connect(self.start_spin)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.rotate)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.spin_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        self.setWindowTitle("Ruleta")
        self.resize(600, 700)

    def start_spin(self):
        self.speed = random.uniform(20, 30)
        self.timer.start(16)
        self.spin_button.setEnabled(False)
        self.result_label.setText("Girando...")

    def rotate(self):
        self.angle += self.speed
        self.speed -= self.deceleration

        transform = QTransform().rotate(self.angle)
        pix_rotated = self.original_pixmap.transformed(transform, Qt.SmoothTransformation)
        self.label.setPixmap(pix_rotated)

        if self.speed <= 0:
            self.timer.stop()
            self.spin_button.setEnabled(True)
            self.determine_winner()

    def determine_winner(self):
        pass
        # normalized = (360 - (self.angle % 360)) % 360
        # index = int(normalized // self.slice_angle)
        # winner = self.players[index]
        # self.result_label.setText(f"Ganador: {winner}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    players = ["Juan", "Cristian", "Wendy", "Sebastián"]*3

    window = Ruleta(players)
    window.show()

    sys.exit(app.exec_())
