import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread

from backend.vote_manager import VoteManager
from backend.external_worker import ExternalVotesWorker
from frontend.welcome import WelcomeWindow
from frontend.client import VotesWindow
from frontend.results import ResultsWindow


def main():
    def hook(t, v, tb):
        print("Excepción capturada:", t, v)
    sys.excepthook = hook
    app = QApplication(sys.argv)

    # Backend ------------------------------------------------------------------------
    vote_manager = VoteManager()

    # Ventanas -----------------------------------------------------------------------
    results_window = ResultsWindow()
    vote_manager.votes_updated.connect(results_window.update_votes_table)

    welcome_window = WelcomeWindow()

    # Funciones para navegación
    def open_votes_window():
        votes_window = VotesWindow(parent=welcome_window)
        votes_window.sig_votos.connect(vote_manager.add_vote)
        votes_window.show()
        welcome_window.close()

    def open_results_window():
        results_window.parent = welcome_window
        results_window.show()
        welcome_window.close()

    # Debug Conexiones
    welcome_window.open_votes_window = open_votes_window
    welcome_window.open_results_window = open_results_window

    # Worker en QThread para votos externos
    thread = QThread()
    worker = ExternalVotesWorker(interval_ms=2000)
    worker.moveToThread(thread)

    # TODO: Inicia el QTimer de worker
    worker.votes_ready.connect(vote_manager.set_external_votes)

    thread.start()

    welcome_window.show()
    exit_code = app.exec_()

    thread.quit()
    thread.wait()

    sys.exit(exit_code)

if __name__ == "__main__":
    main()