x = int(input('Введите число для расчета фактариала: '))

faktorial = 1
perebor_chisel = 1
while perebor_chisel <= x:
    faktorial *= perebor_chisel
    perebor_chisel += 1
print('факториал числа: ', x, 'равен: ', faktorial)
