from decimal import Decimal

from funcion import (
    a,
    b,
    epsilon,
    calculate_function,
    find_a_b,
    print_information
)

#Функция, которая рассчитывает и возвращает новые х1 и х2
def calculate_x(a, b, epsilon):
    return ((a+b)+epsilon)/Decimal(2), ((a+b)-epsilon)/Decimal(2)

#Счетчик количества итераций
itecCounter = 0
while b - a > epsilon+epsilon/100000:
    #Получение новых значений х1 и х2
    x1, x2 = calculate_x(a, b, epsilon)
    itecCounter += 1

    #Получение значений функций в точках х1 и х2
    y_x1 = calculate_function(x1)
    y_x2 = calculate_function(x2)

    #Сохранение старых границ отрезка и получение новых
    b_previous, a_previous = b, a
    a, b = find_a_b(a, b, x1, x2, y_x1, y_x2)

    #Вывод информации на экран
    context = (
        str(itecCounter).ljust(4, ' '),
        a_previous, b_previous,
        a, b,
        (b_previous-a_previous)/(b - a),
        x1, y_x1,
        x2, y_x2
    )

    print_information(context)


print("%.5f %.5f %s" % (a, b, itecCounter))