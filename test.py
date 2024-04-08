"""
Задание №2

Представлен код, в котором происходит GET запрос к сайту с фактами о числах:

import requests

head = {'Content-Type': 'application/json'}
response = requests.get('http://numbersapi.com/9/2/date', headers=head)

r = response.content
print(type(r))
print(r)

Необходимо дополнить код так, чтобы месяц и день, о которых необходимо получить информацию, вводились пользователем.
Количество таких запросов должно быть 10, все ответы, которые мы получаем от сервиса, нужно записать в файл в формате json.

"""

import requests
import json
sp = {}
head = {'Content-Type': 'application/json'}
for i in range(10):
    m = int(input('Введите месяц: '))
    d = int(input('Введите число: '))
    response = requests.get(f'http://numbersapi.com/{m}/{d}/date', headers=head)
    sp[i] = response.json()

with open('fail02.json', 'w', encoding='utf-8') as fl:
    json.dump(sp, fl, indent=4, ensure_ascii=False)


