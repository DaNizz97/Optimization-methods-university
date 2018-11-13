from math import cos, pi
from decimal import Decimal

#Функция, возвращающая новые границы а и b
def find_a_b(a, b, x1, x2, y_x1, y_x2):
    return (a, x2) if y_x1 > y_x2 else (x1, b)

#Функция, рассчитывающая значение в точке х
def f(x):
    #return x*x-30*x+230
    return cos(x)

def calculate_function_2(x1, x2):
    return (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def print_information(context):
    template = "%s\t" + "%.16f\t" * 9

    print(template % (context))


a, b = Decimal(0), Decimal(pi)
epsilon = Decimal(0.001)
