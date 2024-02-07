from fractions import Fraction
import time
import functools

m = [[2, 2, 1, 1, 1],
     [2, 3, 2, 1, 1],
     [4, 5, 4, 3, 1],
     [6, 5, 1, 1, 5]]


def time_measuring(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_t = time.perf_counter()
        output = func(*args, **kwargs)
        print(time.perf_counter() - start_t)
        return output

    return wrapper


@time_measuring
def gauss_method(matrix):
    def action_over_line(mat, num):
        return [Fraction(elem, mat[num][num]) for elem in mat[num]]

    def distract_lines(line1, line2):
        return [line1[n] - line2[n] for n in range(len(line1))]

    # First, triangulate the matrix

    for i in range(len(matrix)):
        for j in range(i):
            matrix[i] = distract_lines(matrix[i], [elem * matrix[i][j] for elem in matrix[j]])
        matrix[i] = action_over_line(m, i)

    # Find each x

    for l in range(-2, -(len(matrix) + 1), -1):
        for k in range(-1, l, -1):
            matrix[l] = distract_lines(matrix[l], [elem * matrix[l][k - 1] for elem in matrix[k]])
    return '\t'.join([f'x_{i}={matrix[i][-1]};' for i in range(len(matrix))])


print(gauss_method(m))
