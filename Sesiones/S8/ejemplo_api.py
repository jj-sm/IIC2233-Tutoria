import requests

url = "https://tutor-iic2233.jjsm.science/iic/"
respuesta = requests.get(url)

print(respuesta.status_code)
print(respuesta.json())