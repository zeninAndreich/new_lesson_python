from Urok_12_oop_osnovnoy_klass import Base

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


class Mag(Base):
    def __init__(self, nik, rasa, pol, colorvolos, typevnesh, bazovy_uron, zdorovie):
        super().__init__(bazovy_uron, zdorovie)
        self.nik = nik
        self.rasa = rasa
        self.pol = pol
        self.colorvolos = colorvolos
        self.typevnesh = typevnesh

    def ognenny_shar(self):
        print(f'Нвнесен урон - {5+self.bazovy_uron} огненным шаром, перезарядка составит 5 секунд')

    def zamorozka(self):
        print(f'Применена заморозка - {1+self.bazovy_uron} урон')

    def hills(self):
        super().healing()

    def info(self):
        print(f'Класс МАГ')
        print(f'Ник: {self.nik}')
        print(f'Раса: {self.rasa}')
        print(f'Пол: {self.pol}')
        print(f'Цвет волос: {self.colorvolos}')
        print(f'Тип внешности: {self.typevnesh}')
        print(f'Доступно: \nognenny_shar - огненный шар\nzamorozka - заморозка \nhills - исцеление')
        self.ognenny_shar()
        self.zamorozka()


class Voin(Base):
    def __init__(self, nik, rasa, pol, colorvolos, typevnesh, bazovy_uron, zdorovie):
        super().__init__(bazovy_uron, zdorovie)
        self.nik = nik
        self.rasa = rasa
        self.pol = pol
        self.colorvolos = colorvolos
        self.typevnesh = typevnesh

    def udar_mechom(self):
        print(f'Нанесено {2+self.bazovy_uron} урона мечом')

    def udar_shitom(self):
        print(f'Нанесено {1+self.bazovy_uron} урон щитом')

    def hills(self):
        super().healing()

    def info(self):
        print(f'\nКласс ВОИН')
        print(f'Ник: {self.nik}')
        print(f'Раса: {self.rasa}')
        print(f'Пол: {self.pol}')
        print(f'Цвет волос: {self.colorvolos}')
        print(f'Тип внешности: {self.typevnesh}')
        print(f'Доступно:\nudar_mechom - удар мечом\nudar_shitom - удар щитом\nhills - исцеление')
        self.udar_mechom()
        self.udar_shitom()


pers = (input('Какого класса вы хотите создать персонажа? \n 1 - Маг\n 2 - Воин\n'))
if pers:
    nik = input('Введите никнэйм персонажа : ')
    rasa = input('Введите расу персонажа (Человек\nЭльфы\nФеи\nДворфы\nПолурослики\nОрки\nГоблины\nОгры\nТролли\nОборотни\nДемоны): ')
    pol = input('Введите пол персонажа (Мужской\nЖенский) :')
    colorvolos = input('Введите цвет волос персонажа: ')
    typevnesh = input('Введите тип внешности персонажа (Драмматик\nГамин\nРомантик\nКлассик\nДругое): ')
    bazovy_uron = int(input('Введите базовый урон: '))
    zdorovie = int(input('Введите здоровье: '))

    if pers == '1':
        personage = Mag(nik, rasa, pol, colorvolos, typevnesh, bazovy_uron, zdorovie)

    elif pers == '2':
        personage = Voin(nik, rasa, pol, colorvolos, typevnesh, bazovy_uron, zdorovie)


personage.info()
