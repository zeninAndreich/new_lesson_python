# Рассчет площади квадрата
''' Функция возвращает площадь квадрата,где (а - длинна стороны)'''

def ploshad_kvadrat(a):
    return (a * a)

#Рассчет периметра квадрата
''' Функция возвращает периметр квадрата,где (а - длинна стороны)'''

def perimetr_kvadrat(a):
    return (4 * a)

#Рассчет площади прямоугольника
''' Функция возвращает площадь прямоугольника,где (а,b - длинны сторон)'''

def ploshad_prymoug(a, b):
    return (a * b)

#Рассчет площади параллелограмма
''' Функция возвращает площадь параллелограмма,где (а-длинна стороны, h - высота  )'''

def ploshad_paralleogram(a,h):
    return (a * h)

#Рассчет площади треугольника
''' Функция возвращает площадь треугольника,где (а-длинна стороны, h - высота  )'''

def ploshad_treugol(a,h):
    return (0.5 * a * h)

#Рассчет площади трапеции
''' Функция возвращает площадь трапеции,где (а,b-длинны сторон, h - высота  )'''
def ploshad_trapec(a,b,h):
    return (((a+b)/2) * h)