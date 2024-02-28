"""
Задание

Создать 2 класса (Маг и Воин), которые будет содержать характеристики персонажа в РПГ игре
(Ник, раса, пол, цвет волос, тип внешности)

Методы воин:
1) удар мечом - наносит 2 урона
2) удар щитом – наносит 1 урон
3) исцеление - восстанавливает 5 здоровья

Методы Маг:
1) огненный шар - наносит 5 урона и произносится 5 секунд
2) заморозка – наносит 1 урона
3) исцеление - восстанавливает 5 здоровья

Пользователь вводит все с клавиатуры и заполняет атрибуты будущего объекта
Пользователь выбирает класс и в зависимости от этого создается объект

"""


class Mag:
    def __init__(self, nik, rasa, pol, colorvolos, typevnesh):
        self.nik = nik
        self.rasa = rasa
        self.pol = pol
        self.colorvolos = colorvolos
        self.typevnesh = typevnesh

    def ognenny_shar(self):
        print('Нвнесен урон = 5 огненным шаром, перезарядка составит 5 секунд')

    def zamorozka(self):
        print('Применена заморозка - 1 урон')

    def iscelenie(self):
        print('Восстановлено 5 единиц здоровья')

    def info(self):
        print(f'Класс МАГ')
        print(f'Ник: {self.nik}')
        print(f'Раса: {self.rasa}')
        print(f'Пол: {self.pol}')
        print(f'Цвет волос: {self.colorvolos}')
        print(f'Тип внешности: {self.typevnesh}')
        print(f'Доступно: \nognenny_shar - огненный шар\nzamorozka - заморозка \niscelenie - исцеление')


class Voin:
    def __init__(self, nik, rasa, pol, colorvolos, typevnesh):
        self.nik = nik
        self.rasa = rasa
        self.pol = pol
        self.colorvolos = colorvolos
        self.typevnesh = typevnesh

    def udar_mechom(self):
        print('Нанесено 2 урона мечом')

    def udar_shitom(self):
        print('Нанесено 1 урон щитом')

    def zdorovie(self):
        print('Восстановлено 5 единиц здоровья')

    def info(self):
        print(f'Класс ВОИН')
        print(f'Ник: {self.nik}')
        print(f'Раса: {self.rasa}')
        print(f'Пол: {self.pol}')
        print(f'Цвет волос: {self.colorvolos}')
        print(f'Тип внешности: {self.typevnesh}')
        print(f'Доступно:\nudar_mechom - удар мечом\nudar_shitom - удар щитом\nzdorovie - исцеление')


pers = (input('Какого класса вы хотите создать персонажа? \n 1 - Маг\n 2 - Воин\n'))
if pers:
    nik = input('Введите никнэйм персонажа : ')
    rasa = input('Введите расу персонажа (Человек\nЭльфы\nФеи\nДворфы\nПолурослики\nОрки\nГоблины\nОгры\nТролли\nОборотни\nДемоны): ')
    pol = input('Введите пол персонажа (Мужской\nЖенский) :')
    colorvolos = input('Введите цвет волос персонажа: ')
    typevnesh = input('Введите тип внешности персонажа (Драмматик\nГамин\nРомантик\nКлассик\nДругое): ')

    if pers == '1':
        personage = Mag(nik, rasa, pol, colorvolos, typevnesh)

    elif pers == '2':
        personage = Voin(nik, rasa, pol, colorvolos, typevnesh)

personage.info()
