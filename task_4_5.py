# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

import requests
import xmltodict
import json
from decimal import *
from datetime import date


def currency_rates(argv):
    """
    :param valute_code: 3-хсимвольный код валюты
    :return: дополнительно возвращает дату, которая передается в ответе сервера
    Дату, и все остальные данные извлечены в виде json-объекта, обращение по ключу
    """
    programs, valute_code = argv
    resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    dict_data = xmltodict.parse(resp.content)
    output_dict = json.loads(json.dumps(dict_data))
    day, month, year = map(int, output_dict['ValCurs']['@Date'].split('.'))
    dd = date(year, month, day)
    print(f'Date {dd}')
    valute_value, value_str = 0.0, ''
    valute_code = valute_code.lower()
    for i in range(len(output_dict['ValCurs']['Valute'])):
        if valute_code == output_dict['ValCurs']['Valute'][i]['CharCode'].lower():
            value_str = output_dict['ValCurs']['Valute'][i]['Value']
            value_str = value_str.replace(',', '.')
            valute_value = Decimal(value_str)
    if valute_value > 0.0:
        return print(f"Value {valute_value}")
    else:
        return print("None")


if __name__ == '__main__':
    import sys

    exit(currency_rates(sys.argv))


