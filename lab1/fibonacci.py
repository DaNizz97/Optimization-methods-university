from decimal import Decimal
from math import (
    sqrt,
)

from funcion import (
    a,
    b,
    epsilon,
    f,
    print_information,
    find_a_b
)


def calculate_fibonacci(n):
    return Decimal((((1 + sqrt(5)) / 2) ** n) / sqrt(5))


def calculate_x(a, b, n):
    fib_n = calculate_fibonacci(n)
    fib_1n = calculate_fibonacci(n + 1)
    fib_2n = calculate_fibonacci(n + 2)

    return a + fib_n / fib_2n * (b - a), a + fib_1n / fib_2n * (b - a)


# n = 0
# print(b-a)
# while b - a > epsilon + Decimal(0.0000000001):
#     x1, x2 = calculate_x(a, b, n)
#     n += 1
#
#     y_x1 = f(x1)
#     y_x2 = f(x2)
#
#     b_previous, a_previous = b, a
#
#     a, b = find_a_b(a, b, x1, x2, y_x1, y_x2)
#
#     context = (
#         str(n).ljust(4, ' '),
#         a_previous, b_previous,
#         a, b,
#         (b_previous - a_previous) / (b - a),
#         x1, y_x1,
#         x2, y_x2
#     )
#
#     print_information(context)
iterCounter = 0
F = [0 for i in range(100)]
n = 60
F[0] = 1
F[1] = 1
for i in range(2, n):
    F[i] = F[i - 1] + F[i - 2]

a1 = a + (b - a) * F[n - 3] / F[n - 1]
b1 = a + (b - a) * F[n - 2] / F[n - 1]
ya = f(a1)
yb = f(b1)

while b - a > epsilon and n != 2:
    iterCounter += 1
    n -= 1
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
