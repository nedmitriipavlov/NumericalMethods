import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative


def function(x):  # desired function
    return np.sin(x) + np.cos(x)


table = [[1, 1.4], [1.5, 1.1], [2, 0.5], [2.5, -0.2], [3, -0.8],
         [3.5, -1.3], [4, -1.4], [4.5, -1.2], [5, -0.7], [5.5, 0.0]]  # a list of (x, y) points

divdif_2 = []  #  devided difference of second order
for i in range(9):
    divdif_2.append((table[i + 1][1] - table[i][1]) / 0.5)


def divdif(n):  # returns devided difference of certain order
    divdif_n = []
    if n == 2:
        divdif_n = divdif_2
        return divdif_n
    else:
        for k in range(11 - n):
            divdif_n.append((divdif(n - 1)[k + 1] - divdif(n - 1)[k]) / (0.5 * (n - 1)))
    return divdif_n


def composition(x, n):
    if n == 1:
        return x - table[0][0]
    else:
        return composition(x, n - 1) * (x - table[n - 1][0])





def newton_interp(x):
    sum = 0
    for i in range(1, len(table)):
        sum += composition(x, i) * divdif(i + 1)[0]

    return function(1) + sum



# differentiation if interpolation polynom
def dif_interp_pol():
    for i in range(1, 9):
        print('Производная в точке', table[i][0], '=', derivative(newton_interp, table[i][0], dx=1e-6))


# devided difference
def razd_razn():
    for i in range(1, 9):
        print('Производная в точке', table[i][0], '=', (table[i + 1][1] - table[i][1]) / 0.5)


# adjusted devided difference
def utoch_razd_razn():
    for i in range(1, 9):
        print('Производная в точке', table[i][0], '=',
              divdif(2)[i - 1] + (2 * table[i][0] - table[i - 1][0] - table[i][0]) * divdif(3)[i - 1])


# exact value of derivative
def tochn_znach():
    for i in range(1, 9):
        print('Производная в точке', table[i][0], '=', derivative(function, table[i][0], dx=1e-6))


