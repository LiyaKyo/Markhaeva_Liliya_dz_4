import requests
import xmltodict
import json
from decimal import *


def currency_rates(valute_code):
    resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    dict_data = xmltodict.parse(resp.content)
    output_dict = json.loads(json.dumps(dict_data))
    valute_value, value_str = 0.0, ''
    valute_code = valute_code.lower()
    for i in range(len(output_dict['ValCurs']['Valute'])):
        if valute_code == output_dict['ValCurs']['Valute'][i]['CharCode'].lower():
            value_str = output_dict['ValCurs']['Valute'][i]['Value']
            value_str = value_str.replace(',', '.')
            valute_value = Decimal(value_str)
    if valute_value > 0.0:
        return print(valute_value)
    else:
        return print("None")


currency_rates(input('Input valute charcode:'))


""" 
1. Можно ли, используя только методы класса str, решить поставленную задачу?
    Можно, но не очень красиво и есть риск ошибки

2. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
    да:
    valute_code = valute_code.lower()
    ....
    if valute_code == output_dict['ValCurs']['Valute'][i]['CharCode'].lower():
    ....
    
3. Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
    Числа типа float имеют фиксированную точность, в то время как числа типа Decimal настраиваемую
    Поэтому использование лишь чисел типа float очень затрудняет разработку финансовых приложений.
    Сначала импортируем модуль decimal:
    from decimal import *
    ...
    valute_value = Decimal(value_str)
"""