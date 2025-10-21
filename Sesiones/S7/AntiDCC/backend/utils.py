import requests
import json

CANDIDATOS = ["Flip Flop", "Los 3 Mishqueteros", "IIC2233.pop()", "y Perry?"]

def get_external_votes() -> dict:
    """
    Llama a la API y retorna dict del tipo:
    {"votes": {"Flip Flop": 3, ...}}
    En caso de error, retorna {"votes": {}}.
    """

    # TODO: Completar
    try:
        diccionario = {
            "candidate_ids": CANDIDATOS,
            "interval": 5
        }

        url = 'https://tutor-iic2233.jjsm.science/iic/votes/'
        response: requests.Response = requests.post(url, json=diccionario)
        data_1 = response.text
        data = json.loads(data_1)

        print("[utils.get_external_votes] API:", data)
        if not isinstance(data, dict):
            return {"votes": {}}
        return data
    except Exception as e:
        print("[utils.get_external_votes] Error:", e)
        return {"votes": {}}
