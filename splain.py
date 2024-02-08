import numpy as np
import matplotlib.pyplot as plt


def function(x):  # desired function
    return np.sin(x) + np.cos(x)


table = [1.4, 1.1, 0.5, -0.2, -0.8, -1.3, -1.4, -1.2, -0.7, 0.0]  # list of points on Y axis
X = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]  # list of points on X axis

'''
f(x) = a_i + b_i * (x - x_i-1_) + c_i * (x - x_i-1_)^2 + d_i * (x - x_i-1_)^3
'''


# Find the coefficients c_i
# Make a matrix equation to do it L * C = F


def line(n):  # returns n-th coefficients string if c_i is there
    if n == 1:
        return [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if n == 10:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    else:
        return (n - 2) * [0] + [0.5, 2, 0.5] + (10 - (n - 2) - 3) * [0]


# Make a matrix of coefficients for c_i
L = np.array([line(1), line(2), line(3), line(4), line(5), line(6), line(7), line(8), line(9), line(10)])

# find the inverse matrix L
inv_L = np.linalg.inv(L)


def free_member(n):  # returns n-th free member
    if n == 1:
        return 0
    if n == 10:
        return 0
    else:
        return 6 * (table[n] - 2 * table[n - 1] + table[n - 2])


# Make a matrix using free members
F = np.array([free_member(1), free_member(2), free_member(3), free_member(4), free_member(5), free_member(6),
              free_member(7), free_member(8), free_member(9), free_member(10)])

# Solve a matrix equation
C = np.linalg.inv(L).dot(F)

# Make a list from the matrix
C = C.tolist()

# list of a_i
A = table[0:-1]

# list of d_i
D = []
for i in range(8):
    D.append((C[i + 1] - C[i]) / (3 * 0.5))
D.append(-C[8] / (3 * 0.5))

# list of b_i
B = []
for i in range(8):
    B.append((table[i + 1] - table[i]) / 0.5 - 0.5 / 3 * (C[i + 1] + 2 * C[i]))
B.append((table[9] - table[8]) / 0.5 - 2 / 3 * 0.5 * C[8])


def splain_interp(x):   # returns a value of the interpolation function at the point x
    i = int((x - x % 0.5) / 0.5 - 2)

    return A[i] + B[i] * (x - X[i]) + C[i] * (x - X[i]) ** 2 + D[i] * (x - X[i]) ** 3


# Draw a plot
x = np.linspace(1.0, 5, 800)
y = np.vectorize(splain_interp, otypes=[float])

plt.plot(x, y(x), x, np.sin(x) + np.cos(x))
plt.legend(['spline interpolation', 'desired plot'], loc=2)
plt.title('spline interpolation', fontweight="bold")
plt.show()
