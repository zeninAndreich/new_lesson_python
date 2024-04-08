import requests

head = {'Content-Type': 'application/json'}
responce = requests.get('http://numbersapi.com/4/10/date', headers=head)

print(responce.status_code)
print(responce.json())

d = responce.content
print(d)

s = d.decode(encoding='utf-8')
print(s)

"""
Задание №1

За основу возьмем задание из урока Словари.
Создать словарь, в котором в качестве ключа содержится номер студенческого билета
(номер билета трехзначный т.е. от 0 до 999),
а в качестве значения содержится строка с именем и фамилией.
Заполняется словарь вводом с клавиатуры, номер билета генерируется случайно,
но проверяется чтобы он не использовался в словаре.
Заполнить словарь 10 элементами

Необходимо изменить код так, чтобы:
1.Цикл был не на 10 повторений, а бесконечный.
2.Ввод и работа программы прекращается, когда пользователь вводит "END" (в любом регистре).
3.Сгенерированный словарь необходимо записать в файл формата .json (файл создается из программы).
(не забываем indent для структурированной записи)

Для того чтобы записать РУССКИЕ символы в файл json необходимо:

    открыть файл в кодировке utf-8
    при использовании dump добавить еще один аргумент ensure_ascii=False

Пример:

with open('test.json', 'w', encoding='utf-8') as fl:
    json.dump(slovar, fl, indent=3, ensure_ascii=False)
"""
import random
import json
slovar = {} #Создаем пустой словарь

i = 0
while True: #цикл на бесконечного числа повторений
    j = random.randint(0,999)
    if j in slovar.keys(): #проверяем,есть ли такой ключ в словаре
        j = random.randint(0,999) #если есть,то генерируем снова
    else:
        try:
            r = input('Введите Имя и Фамилию студента: ')
            if r.lower() == 'end':
                raise TypeError
            slovar[j] = r #добавляем пару ключ/значение в словать
            i+=1 #увелициваем цикл
        except:
            print('Ну на этом завершимся')
            break

with open('fail.json', 'w' , encoding= 'utf-8',) as ff:
    json.dump(slovar,ff,indent=4, ensure_ascii=False)

print(slovar) #выводим наш словарь

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


