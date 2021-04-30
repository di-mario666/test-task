"""
ВЫПОЛНЕНА НА PYTHON

Разработать программу, которая выводит курс японских иен к российскому рублю, на основании данных, запрошенных с сайта
http://www.cbr.ru/scripts/XML_daily.asp
"""

import requests
# Импортируем модуль etree из библиотеки lxml для парсинга xml (так как сайт у нас в формате xml)
from lxml import etree

# делаем GET-запрос на сайт и декодируем в windows-1251(так как ответ мы получаем в формате xml и переводим в байты)
xml_res = etree.fromstring(requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.encode("1251"))

# c помощью метода find находим нужную строку
curs = xml_res.find("Valute[@ID='R01820']/Value").text

print(f"Курс валют:\nОдин японских иен равен {curs} российских рублей")
