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

        self.setLayout(vbox)
        self.setMinimumSize(400, 200)
        self.setWindowTitle("Menú Principal")

        # TODO: implementen una funcion para centrar la ventana
        # self.center()

    def center(self):
        ...

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