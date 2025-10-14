from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from .utils import get_external_votes


class ExternalVotesWorker(QObject):
    """
    Worker que vive en un QThread. Usa un QTimer interno para
    pedir votos externos periódicamente y emite la señal votes_ready
    con un dict plano de votos.
    """
    votes_ready = pyqtSignal(dict)

    def __init__(self, interval_ms=5000):
        super().__init__()
        # TODO: Crea un QTimer e implementalo con start(), conecta su timeout a fetch()
        self.interval_ms = interval_ms


    def start(self):
        # TODO: Crea un QTimer e implementalo con start(), conecta su timeout a fetch()
        ...

    def fetch(self):
        # TODO: emite un dict de los votos externos usando get_external_votes()
        # NOTA: recuerda emitir solo el dict plano, no {"votes": {...}} (my mistake)
        votes = {} # FIXME


        print("[ExternalVotesWorker] fetched:", votes)
        self.votes_ready.emit(votes)