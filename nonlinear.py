from sympy import *
import functools
import time

x, y = symbols('x y')

func1 = sin(y - 1) + x - 1.3
func2 = y - sin(x + 1) - 0.8


def time_measuring(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_t = time.perf_counter()
        output = func(*args, **kwargs)
        print(time.perf_counter() - start_t)
        return output

    return wrapper


@time_measuring
def nonlinear_solving(f1, f2, x_start=(1000, 20), eps=0.0001):
    def jakobian(first_f, second_f, x_value=x_start[0], y_value=x_start[1]):
        """Define jakobian according the theory"""
        df1dx = lambdify(x, diff(first_f, x))
        df1dy = lambdify(y, diff(first_f, y))
        df2dx = lambdify(x, diff(second_f, x))
        df2dy = lambdify(y, diff(second_f, y))

        matrix = [[df1dx(x_value), df1dy(y_value)], [df2dx(x_value), df2dy(y_value)]]
        return matrix

    def kramer(m, m0):
        """System of equations like a_11 * x + a_12 * y = a, a_21 * x + a_22 * y = b"""
        delta = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        delta_x = m0[0] * m[1][1] - m[0][1] * m0[1]
        delta_y = m[0][0] * m0[1] - m0[0] * m[1][0]
        return delta_x / delta, delta_y / delta

    def step(w, x_inp=x_start[0], y_inp=x_start[1], fn1=lambdify([x, y], func1), fn2=lambdify([x, y], func2)):
        return kramer(w, [-fn1(x_inp, y_inp), -fn2(x_inp, y_inp)])

    res_st = step(jakobian(f1, f2))
    dx = (simplify(res_st[0]), simplify(res_st[1]))
    xi = [x_start[0] + dx[0], x_start[1] + dx[1]]

    while abs(dx[0]) >= eps and abs(dx[1]) >= eps:
        xi = [xi[0] + dx[0], xi[1] + dx[1]]
        res = step(jakobian(f1, f2, x_value=xi[0], y_value=xi[1]), x_inp=xi[0], y_inp=xi[1])
        dx = (simplify(res[0]), simplify(res[1]))
    else:
        return xi


print(nonlinear_solving(func1, func2))
