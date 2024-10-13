import requests
#импорт из модуля read_json функции read_json
from .read_json import read_json
#импорт модуля json
import json
#чтение файла config_api.json
data_api = read_json(name_file= 'config_api.json')
#апи ключ для подключения к серверу и получения каких то данных из него
API_KEY = data_api['api_key']
#название города для получения данных о погоде
CITY_NAME = data_api['city_name']
#ссылка на сайт в которую вставляются имя города и апи ключ. По этой ссылке будут получены данные
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#предоставляет доступ к URL с помощью модуля requests
response = requests.get(URL)
#условие которое гласит: если код ответа на наш запрос серверу будет 200, полученные данные будут конвертированы в пайтон словарь
if response.status_code == 200:
    #конвертация данных в пайтон словарь
    data_dict = json.loads(response.content)
    #выводит в терминал данные в формате строки json
    print(json.dumps(data_dict, indent= 4))