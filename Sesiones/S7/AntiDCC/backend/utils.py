import requests


def get_external_votes() -> dict:
    """
    Llama a la API y retorna dict del tipo:
    {"votes": {"Flip Flop": 3, ...}}
    En caso de error, retorna {"votes": {}}.
    """

    # TODO: Completar
    try:
        response = ...
        data = ...

        print("[utils.get_external_votes] API:", data)
        if not isinstance(data, dict):
            return {"votes": {}}
        return data
    except Exception as e:
        print("[utils.get_external_votes] Error:", e)
        return {"votes": {}}