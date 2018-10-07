from numpy import array


from funcion import (
    calculate_function_2,
    epsilon
)


def calc_f(x1, x2):
    return -4*x1*x2+4*x1**3-2


def calc_g(x1, x2):
    return 2*x2-2*x1**2+1


lamb = 1


x_prev = array([2,2])
y_prev = calculate_function_2(*x_prev)

while True:
    x_new = x_prev - array([calc_f(*x_prev), calc_g(*x_prev)])*lamb
    y_new = calculate_function_2(*x_new)

    if lamb <= epsilon:
        break
    elif y_prev < y_new:
        lamb = lamb/2
    else:
        x_prev = x_new
        y_prev = y_new

    print(x_prev, x_new, y_prev, y_new, lamb)


    print("%s %s" % (x_prev, x_new))