from decimal import Decimal

from funcion import (
    a,
    b,
    epsilon,
    f,
    print_information
)


# Функция, рассчитывающаяя и возвращающая новые значения точек x1 и х2
def calculate_x(a, b):
    # return a + golden_section_coefficient * (b - a), \
    #        b - golden_section_coefficient * (b - a)
    return b - (b - a) * golden_section_coefficient, \
           a + (b - a) * golden_section_coefficient


def find_a_b(y_x1, y_x2, a, b):
    return (a, b1) if y_x1 < y_x2 else (a1, b)


golden_section_coefficient = Decimal(0.6180339)

iterCounter = 0

a1, b1 = calculate_x(a, b)

ya = f(a1)
yb = f(b1)

print(a1, ya, "   ", b1, yb, "\n", a, b)
while b - a > epsilon:
    iterCounter += 1
    if ya > yb:
        a = a1
        a1 = b1
        b1 = a + b - a1
        ya = yb
        yb = f(b1)
    else:
        b = b1
        b1 = a1
        a1 = a + b - b1
        yb = ya
        ya = f(a1)

    context = (
        str(iterCounter).ljust(4, ' '),
        # a_previous, b_previous,
        -1, -1,
        a, b,
        #  (b_previous - a_previous) / (b - a),
        -1,
        a1, ya,
        b1, yb
    )

    print_information(context)

print("\n\n%.5f %.5f %s" % (a, b, iterCounter))
