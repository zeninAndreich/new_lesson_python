"""
Задание №1

Дана строка, введенная пользователем, состоящая из двух слов, разделенных пробелом.
Переставить эти слова местами, записать в строку и вывести её на экран.

"""
#запрашиваем ввод данных
a = input('Введите два слова,разделив их пробелом: ')
#сплитоп разделяем полученную строку на элементы
a = a.split()
#склеиваем элементы в обратном порядке
a = a[1] + " " + a[0]
#выводим
print(a)

"""
Задание №2

Пользователь вводит строку, необходимо посчитать сколько в этой строке встречается букв "a" и "o" .
Предварительно необходимо перевести строку в нижний регистр. Ввод и проверки осуществляются на английском языке.
Вывод должен иметь вид:

Буква 'a' встречается XXXX раз
Буква 'o' встречается XXXX раз
Если нет таких букв то:
В введенном предложении нет букв 'o' и 'a'
"""
r = input('Введите строку: ')
st1 = r.count('a')
st2 = r.count('o')
if st1 == 0 and st2 == 0:
    print("В введенной строке нет букв 'o' и 'a'")
else:
    print(f'В введенной строке {st1} букв(ы) "a" ')
    print(f'В введенной строке {st2} букв(ы) "o" ')

"""
Задание №3

Написать программу, которая подсчитывает, сколько содержится цифр в введенной пользователем строке.

пример вывода:
В введенной строке : ХХ цифр
"""

e = input('Введите любое значение: ')
kollchisel = 0
for i in e:
    if i.isdigit()
        kollchisel+=1
print(f'В введенной строке {kollchisel} цыфр(ы)')