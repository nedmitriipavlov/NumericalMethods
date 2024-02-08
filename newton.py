import numpy as np
import matplotlib.pyplot as plt


def function(x):  # desired function
    return np.sin(x) + np.cos(x)


table = [[1, 1.4], [1.5, 1.1], [2, 0.5], [2.5, -0.2], [3, -0.8],
         [3.5, -1.3], [4, -1.4], [4.5, -1.2], [5, -0.7], [5.5, 0.0]]  # a list of (x, y) points

divdif_2 = []  # devided difference of second order
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

'''
def newton_interp(x):
    return function(1) + \
           composition(x, 1) * divdif(2)[0] + \
           composition(x, 2) * divdif(3)[0] + \
           composition(x, 3) * divdif(4)[0] + \
           composition(x, 4) * divdif(5)[0] + \
           composition(x, 5) * divdif(6)[0] + \
           composition(x, 6) * divdif(7)[0] + \
           composition(x, 7) * divdif(8)[0] + \
           composition(x, 8) * divdif(9)[0] + \
           composition(x, 9) * divdif(10)[0]
'''


def newton_interp(x):

    sum = 0
    for i in range(1, len(table)):
        sum += composition(x, i) * divdif(i + 1)[0]

    return function(1) + sum


# Plotting of desired function and interpolation polynom
fig = plt.subplots()
x = np.linspace(1.5, 5, 800)
y = lambda x: function(x)
plt.plot(x, newton_interp(x))
plt.plot(x, y(x))
plt.legend(["Newton's interpolation", 'desired plot'], loc=2)
plt.title("Newton's interpolation", fontweight="bold")
plt.show()
