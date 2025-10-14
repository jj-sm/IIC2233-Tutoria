import requests

URL = "https://tutor-iic2233.jjsm.science/iic/votes"
CANDIDATES = ["Flip Flop", "Los 3 Mishqueteros", "IIC2233.pop()", "y Perry?"]
BASE_PAYLOAD = {
    "candidate_ids": CANDIDATES,
    "interval": 3
}


def get_external_votes() -> dict:
    """
    Llama a la API y retorna dict del tipo:
    {"votes": {"Flip Flop": 3, ...}}
    En caso de error, retorna {"votes": {}}.
    """
    try:
        resp = requests.post(URL, json=BASE_PAYLOAD, timeout=5)
        data = resp.json()
        print("[utils.get_external_votes] API:", data)
        if not isinstance(data, dict):
            return {"votes": {}}
        return data
    except Exception as e:
        print("[utils.get_external_votes] Error:", e)
        return {"votes": {}}