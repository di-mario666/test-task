"""
ВЫПОЛНЕНА НА PYTHON

Разработать программу, которая будет отправлять запрос к сервису прогноза погоды https://openweathermap.org/  с использованием бесплатного плана (Free, требует регистрации на сайте) и на основании полученных данных выводить следующую информацию:
1. Максимальное давление за предстоящие 5 дней (включая текущий);
"""
# https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly,alerts&appid={API_KEY}&units=metric

import requests
import json

API_KEY = "c1d0f0da7d1ca0fb7674eae1f7c2168b"

# Координаты моего родного г.Ликино-Дулево
longitude = 38.9600075  # долгота
latitude = 55.7038114  # широта



# делаем GET-запрос на сайт через API, выводя в виде текстовых строк
api_response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly,alerts&appid={API_KEY}&units=metric").text
# читаем полученный файл с помощью модуля JSON
json_response = json.loads(api_response)
# Создаем пустой список, динамически заполняем его циклом range данными день-давление
pressure_arr = []
for i in range(5):
    pressure_arr.append(json_response["daily"][i]["pressure"])
# Выводим максимальное значение списка pressure_arr
print(f"Максимальное давление в г.Ликино-Дулево за предстоящие 5 дней составляет: {max(pressure_arr)} мм рт.ст.")

