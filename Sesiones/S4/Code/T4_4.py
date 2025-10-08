
def errores(n: int) -> None:
    if n == 0:
        raise ZeroDivisionError
    elif n == 1:
        raise IndexError(f"[ERROR]: Index fuera de rango {n}")
    elif n == 2:
        raise KeyError

try:
    errores(1)
except Exception as e:
    print(f'Ha ocurrido un error: {e}')