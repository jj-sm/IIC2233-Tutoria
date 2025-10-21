import json

class JugadorEncoder(json.JSONEncoder):
    def default(self, o):
        o = o.__dict__
        return {o['nombre']: {'puntaje': o['puntaje'], 'vida': o['vida'], 'nivel': o['nivel']}}


class Jugador:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
        self.vida = 100
        self.vida2()

    def vida2(self):
        self.nivel = 2


mario = Jugador("Mario", 1500)

json_jugador = json.dumps(mario.__dict__, cls=JugadorEncoder)
print(json_jugador)