from Urok_11_modul1 import obem_kuba
from Urok_11_Modul2 import ploshad_trapec

f = int(input('Для рассчета объема куба введите длинну его стороны: '))
print(f'Объем куба равен {obem_kuba(f)}')

a = int(input('Для рассчета площади трапеции введите первую длинну стороны: '))
b = int(input('Введите вторую длинну стороны: '))
h = int(input('Введите длинну высоты: '))
print(f'По вышим параметрам площадь трапеции равна {ploshad_trapec(a,b,h)}')