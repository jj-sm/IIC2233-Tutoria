from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QDesktopWidget
)

class WelcomeWindow(QWidget):
    """
    Ventana de bienvenida. main.py
        - open_votes_window (callable)
        - open_results_window (callable)
        - results_window (referencia)
    """

    def __init__(self):
        super().__init__()
        self.open_votes_window = None
        self.open_results_window = None
        self.results_window = None
        self.init_gui()

    def init_gui(self):
        vbox = QVBoxLayout()

        title = QLabel("Bienvenido a Votaciones Pangüin't")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        vbox.addWidget(title)

        # TODO: Agrega el texto genérico de manera centrada
        
        # TODO: Agrega los botones para votar y ver resultados.
        # Conecta sus señales a los métodos _go_vote y _go_results
        caja_horizontal = QHBoxLayout()
        boton1 = QPushButton("Votar")
        boton2 = QPushButton("Resultados")
        caja_horizontal.addWidget(boton1)
        caja_horizontal.addWidget(boton2)
           
        # ------ Cuadro de Mensaje Genérico -----
        cuadro_mensaje_H = QHBoxLayout()
        
        mensaje_generico = QLabel("Tu decides si eliminar al DCC 🧌")
        mensaje_generico.setAlignment(Qt.AlignCenter)
        cuadro_mensaje_H.addWidget(mensaje_generico)
        vbox.addLayout(cuadro_mensaje_H)
        # -------------------------------

        vbox.addWidget(mensaje_generico)
        vbox.addLayout(caja_horizontal)

        self.setLayout(vbox)
        self.setMinimumSize(400, 200)
        self.setWindowTitle("Menú Principal")

        # Conectar Botones
        boton1.clicked.connect(self._go_vote)
        boton2.clicked.connect(self._go_results)

        # TODO: implementen una funcion para centrar la ventana
        self.center()

    def center(self):
        width, height = QDesktopWidget().availableGeometry().width(), QDesktopWidget().availableGeometry().height()
        width_real = (width - 400) // 2
        height_real = (height - 200) // 2
        self.move(width_real, height_real)
        

    def _go_vote(self):
        if callable(self.open_votes_window):
            self.open_votes_window()

    def _go_results(self):
        if callable(self.open_results_window):
            self.open_results_window()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec_())