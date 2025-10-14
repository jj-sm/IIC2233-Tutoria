import threading
from PyQt5.QtCore import QObject, pyqtSignal

CANDIDATOS = ["Flip Flop", "Los 3 Mishqueteros", "IIC2233.pop()", "y Perry?"]


class VoteManager(QObject):
    """
    Centraliza votos locales y externos. Emite siempre un dict plano:
    {
        "Flip Flop": total,
        "Los 3 Mishqueteros": total,
        ...
    }
    """
    votes_updated = pyqtSignal(dict)

    def __init__(self):
        # TODO: Implementa el Lock para evitar race conditions
        super().__init__()
        self.local_votes = {c: 0 for c in CANDIDATOS}
        self.external_votes = {c: 0 for c in CANDIDATOS}


    def _combined(self) -> dict:
        # Suma local + externo para cada candidato
        return {
            c: self.local_votes.get(c, 0) + self.external_votes.get(c, 0)
            for c in set(self.local_votes) | set(self.external_votes)
        }

    def add_vote(self, candidate: str):
        with self.lock:
            if candidate not in self.local_votes:
                self.local_votes[candidate] = 0
            self.local_votes[candidate] += 1
            combined = self._combined()
            print("[VoteManager] Local+External tras voto:", combined)
            self.votes_updated.emit(combined)

    def set_external_votes(self, votes: dict):
        """
        Reemplaza votos externos (dict plano) y emite combinación.
        """
        with self.lock:
            # Mantener cualquier candidato nuevo que aparezca
            self.external_votes = votes.copy()
            combined = self._combined()
            print("[VoteManager] (API) Local+External:", combined)
            self.votes_updated.emit(combined)

    def get_votes(self) -> dict:
        with self.lock:
            return self._combined()


