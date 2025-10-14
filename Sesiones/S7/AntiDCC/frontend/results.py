import sys
from time import strftime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,
    QDesktopWidget, QTableWidget, QTableWidgetItem
)


class ResultsWindow(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__()
        self.parent = parent
        self.init_gui()

    def init_gui(self):
        self.main_layout()
        self.setMinimumSize(520, 260)
        self.setWindowTitle("Resultados Votaciones Pangüin't")
        self.center()

    def main_layout(self):
        vbox = QVBoxLayout()

        # TODO: Crea el layout segun el enunciado
        # TODO: Instancia una tabla de VotesTable y guardala en self.votes_table
        # TODO: Ubica correctamente self.last_update_label y self.votes_table
        # TODO: Crea e implementa el botón volver


        # Label Inicial
        self.last_update_label = QLabel("Última actualización: --:--:--")
        self.last_update_label.setAlignment(Qt.AlignCenter)



    def center(self):
        # TODO: usen la función usada en welcome.py
        ...

    def return_to_welcome(self):
        if self.parent:
            self.parent.show()
        self.close()

    def update_votes_table(self, votes: dict):
        """
        votes: dict plano ya combinado (local + externo).
        """
        # TODO: este es uno de los slots que es conectado. Implementalo actualizando self.votes_table
        # haciendo uso de su método update_votes que recibe un dict, además, cuando lo actualices,
        # actualiza también self.last_update_label con la hora actual. Usa: time: str = strftime('%H:%M:%S')

        print("[ResultsWindow] Recibí votos:", votes)
        # self.votes_table


class VotesTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Candidato", "Votos"])
        self.update_votes({})

    def update_votes(self, votes: dict):
        self.setRowCount(len(votes))
        self.clearContents()
        for i, (candidate, vote_n) in enumerate(votes.items()):
            self.setItem(i, 0, QTableWidgetItem(candidate))
            self.setItem(i, 1, QTableWidgetItem(str(vote_n)))


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    from ..backend.vote_manager import VoteManager
    app = QApplication([])
    vm = VoteManager()
    w = ResultsWindow()
    vm.votes_updated.connect(w.update_votes_table)
    w.show()
    # Prueba manual
    vm.add_vote("Flip Flop")
    vm.set_external_votes({"Flip Flop": 5, "Los 3 Mishqueteros": 2, "IIC2233.pop()": 3, "y Perry?": 1})
    sys.exit(app.exec_())