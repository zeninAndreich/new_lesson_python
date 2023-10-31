"""
Задание №1

Написать программу, которая в текущем каталоге создает текстовый файл stichi.txt
Записывает в него следующий стих (используя print или write).

We walk through the years like steps.
No need to whine that our ascent is hard.
If we suddenly don't find a new step —
The way back is always a moment.
"""
fl = open('stichi.txt', 'wt', encoding='utf-8') # Открываем файл
print("""We walk through the years like steps. 
No need to whine that our ascent is hard.
If we suddenly don't find a new step —
The way back is always a moment.""" , file= fl) # первый вариант,с помощью функции print,переменная в качестве файла -функция
#ls = """We walk through the years like steps.
#No need to whine that our ascent is hard.
#If we suddenly don't find a new step —
#The way back is always a moment."""
#fl.write(ls) # записываем в файл # второй вариант с помощью функции write.
fl.close() # закрываем файл


"""
Задание №2

Написать программу, которая считает количество строк в прикрепленном файле.
Файл должен находиться в том же каталоге, что и программа.

P.S. в подсчет не включать строки, которые обозначают пропуски между частями стихотворения.
zadanie2.txt
0.66 Кб
"""
#th = open('zadanie2.txt','wt',encoding='utf-8')
#print(""" Rock, substituting his chest under the waves,
#It's worth it, it's open to all winds.
#Is there anything in the world,
#What would be stronger than granite?

#The answer to this was given by science
#More from a hundred years away:
#— Stronger than granite — titanium metal
#And solid steel grades.

#And harder? Do not squint your eyes inquisitively,
#The answer is also known:
#— Stronger than steel and titanium — diamond. —
#Let it be so. Well, we have on earth
#Is there anything harder than diamond?

#Yes, there is one substance on earth,
#And it has nothing to do with science:
#Everyone is stronger and it was and it should be
#The firm word of a friend!""",file = th)

ej = open('zadanie2.txt','r',encoding='utf-8') # открываем файл в режиме чтения
count = 0 #задаем счетчик
for i in ej: # перебираем все строки
    if i == '\n': # если встречаем отступ на новую строку,пропускаем итерацию
        continue
    else: # в противном случае,прибавляем к счетчику +1
        count+=1
ej.close() # закрываем файл
print(count) # выводим колличество

"""
Задание №3

Представленный файл, разбить на 4 файла, каждый из которых содержит по одному абзацу стиха.

zadanie3.txt
0.66 Кб
"""
ru = open('zadanie3.txt','r',encoding='utf-8') # открываем файл
poem = '' # временная переменная для хранения абзаца
w = 0 # переменная счетчика для файлов
for i in ru:
    if i: # если строка не пустая
        if i != '\n': # если строка не равна переходу на новую строку
            poem+=i # прибавляем строку к нашей переменной
        else:
            data_file = open(f'fail{w}.txt','wt',encoding='utf-8') #открываем файл,в который записываем авзац
            data_file.write(poem) # записываем,то,что у нас хранится во временной переменной
            data_file.close() # закрываем файл
            poem = '' # обнуляем временную переменную
            w += 1 # увеличиваем счетчик абзаца
else: # по окончанию работы цикла записываем последний абзац в последний файл
    data_file = open(f'fail{w}.txt','wt',encoding='utf-8') #  открываем файл,в который записываем абзац
    data_file.write(poem) # записываем,то что хранится во временной переменной
    data_file.close() # закрываем файл
ru.close() # закрываем файл

"""
Задание №4

Написать функцию, которая принимает на вход два параметра: имя файла и режим открытия (имя файла вводится пользователем,
режим указывается при вызове функции в виде литерала).
Функция должна считать количество слов в переданном в нее файле и возвращать это количество.
Для тестирования можно использовать текстовый файл из 2 задания.
"""

def my_funk(name,mode): # определяем функцию
    with open(name,mode,encoding='utf-8') as fl: # открываем файл
        ttt = fl.read() # читаем все из файла и помещаем в переменную
        ttt = ttt.replace('\n',' ') # заменяем отступы на пробелы
        ttt = ttt.replace('  ',' ') # заменяем двойные пробелы на одинарные
        sp = [] # создаем пустой список
        sp = ttt.split() # создаем список из текста
        for i in range(len(sp)-1, -1, -1): # перебираем список
            if len(sp[i]) == 1: #  проверяем элементы длиной в 1 символ
                if not sp[i].isalpha():  # проверяем,если это не символ,удаляем его
                    del sp[i]
        return print(f'Колличество слов в файле : {len(sp)}')  # выводим длинну списка
my_funk(input('Введите имя файла: '), 'r') # вызываем функцию

"""
Задание №5

Напишите функцию, которая на вход принимает имя файла.
Функция должна возвращать следующую информацию о файле:

    Количество строк (предложений)
    Количество слов
    Количество целых чисел
    Количество знаков препинания (точки, запятые, вопросительные знаки и др.)


Использовать один из прикрепленных текстовых файлов для теста.
zadanie5-us.txt.txt
0.91 Кб
zadanie5.txt
1.57 Кб
"""

def my_fanc(name): # определяем функцию
    with open(name, 'r', encoding='utf-8') as r: # открываем файл
        eee = r.read() # помещаем содержимое файла в переменную
        eee1 = eee.replace('\n',' ') # меняем все отступы на пробелы
        eee1 = eee.replace('  ',' ') # меняем двойные пробелы на одинарные
        sp = []  # создаем пустой список
        sp = eee1.split() # помещаем в список строки разделенные пробелом
        for i in range(len(sp)-1, -1, -1): # перебираем элементы и считаем слова
            if len(sp[i]) == 1:
                if not sp[i].isalpha():
                    del sp[i]
        print(sp)
        str = eee.count('. ') + eee.count('.\n') # считаем колличество предложений
        print(f'Колличество строк: {str}')  # выводим колличество предложений
        print(f'Колличество слов в файле: {len(sp)}') # выводим колличество слов
        new_eee = '' # создаем временную переменную строковую
        for j in eee: # перебираем символы всего текста
            if j.isdigit() or j.isalpha() or j == ' ': # если это буква,цифра или пробел.
                new_eee += j # приклеиваем его к новой переменной
        new_sp = new_eee.split()     # создаем список из элементов текста разделенных пробелом
        cisla = [] #создаем список ,в который будут записываться числа из текста
        for i in range(len(new_sp)): # перебираем элементы временного списка и проверяем является ли элемент числом
            if new_sp[i].isdigit():
                cisla.append((new_sp[i])) # если число, то добавляем в список
        print(f'Колличество целых чисел: {len(cisla)}') #  длина списка в который помещали числа
        print(f'{len(eee)} - {len(new_eee)}') # считаем знаки, как мы помним удаляли все кроме цифр и букв

my_fanc('zadasnie5.txt')