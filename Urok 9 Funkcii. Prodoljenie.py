"""

Задание №1

Переписать код программы ниже так, чтобы был не только вывод звездочек,
но и подсчет всех звездочек, которые напечатаются при вызове функции с аргументом 140. (F(140))

def F( n ):
print('*')
if n >= 1:
print('*')
F(n-1)
F(n//2)

P.S. Если задание выполняется очень долго, то вызов функции сделайте не от 140 а от 40.
"""
y = 0 # определяем переменную счетчика
def t(n): # определяем функцию с параметром n
    global y # определяем,что используем глобальную переменную
    print('*')
    y += 1 # увеличиваем счетчик
    if n >= 1:
        print('*')
        y += 1  # увеличиваем счетчик
        t(n-1) # вызываем снова функцию,делаем рекурсию с параметром n-1
        t(n//2) # вызываем функцию с параметрами n//2

t(140) # вызываем функцию с параметром 140
print(f'колличество звездочек = {y}') # выводим колличество зведочек

"""
Задание №2

Используя рекурсию, написать функцию, которая выводит числа Фибоначчи.
Функция принимает в качестве аргумента количество элементов последовательности, начиная с 0.
Числа Фибоначчи - это последовательность, в которой последующее число равно сумме двух предыдущих чисел.
ввод:
6
вывод:
0
1
1
2
3
5
"""

def fibonachi(n): #определяем функцию для вывода чисел фибоначи с параметром n
    if (n <= 1): # условие остановки рекурсии
        return n # если условие выполнено ,то возвращаем n
    else:
        return (fibonachi(n-1) + fibonachi(n-2)) # при невыполнении условий вызываем снова функцию с аргументами n-1 и n-2
r = int(input('Введите число: ')) #запрашиваем колличество элементов
print("Последовательность:")
for i in range(r+1): #открываем цикл и перебираем числа от 0 до введенного
    print(fibonachi(i)) # и для каждого числа вызываем функцию

"""
Задание №3

Используя лямбда выражение и функцию filter, создать программу,
которая из введенной строки создает список, содержащий только цифровые символы.
"""
w = input('Введите строку: ') # заправшиваем строку
result = list(filter(lambda x:x.isdigit(), w)) # в переменную result записываем список, который получается при работе
# функции filter лямда позводяет проверить,является ли наш элемент цифровым значением ,если да, то передаем его в список
print(result)

"""
Задание №4

Список на 10 элементов, заполненный случайными числами от 1 до 20.
Необходимо на основе данного списка создать новый список, в котором четные элементы первого списка умножены на 2,
а нечетные на 3.
Использовать функции map() и лямбда.
Вывести первоначальный список и получившийся список.
Пример:
первый список: [1, 2, 3, 4]
получившийся список: [3, 4, 9, 8]
"""
import random
ls = [random.randint(1,20) for i in range(10)] # создаем и заполняем список
resls = list(map(lambda x: (x*2)  if x%2==0 else (x*3),ls )) # создаем новый список на основании старого, преобразуем
# в список результат работы функции map,внутри которой лямда, проверяющая условие, и возвращающая соответсвующее преобразование
# элемента списка, который указан в качестве аргумента
print(ls)
print(resls)

"""
Задание №5

Используя декоратор, вывести время выполнения функции подсчета факториала (задание 3 прошлого урока).
"""
import time

def my_decorator(funk): # создаем функцию,которая будет служить декоратором
    def my_vlog(numb): # создаем вложенную функцию
        start_time = time.time() # записываем время перед началом работы функции
        funk(numb) # выполняем переданную функцию
        end_time = time.time() # записываем время после работы функции
        long_time = end_time - start_time # высчитываем разницу
        print(f'Время выполнения фунции {long_time}')
    return my_vlog # возвращаем нашу функцию

@my_decorator
def my_funk(num):  # определяем функцию с параметром
    i = 1  # переменная для перебора
    faktorial = 1  # переменная для факториала
    while i <= num:  # цикл для перебора чисел
        faktorial *= i  # считаем факториал
        i += 1  # увеличиваем счетчик
    return print(f'Факториал числа {num} равен {faktorial}')


g = int(input('Введите число,для расчета факториала: '))
my_funk(g)