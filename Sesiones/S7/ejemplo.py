lista = ['1'    ,'2' ,'3' ,'4' ,'5' ]

filtro = filter(lambda x: int(x) % 2 == 0, lista)

def filtro(x):
    return int(x) % 2 == 0