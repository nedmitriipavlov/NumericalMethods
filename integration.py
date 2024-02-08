from sympy import *
import functools
import time

x = symbols('x')  # Define a variable x

func_inp = 2 * x ** 2 + 1 - x ** (1 / 2)


def time_measuring(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_t = time.perf_counter()
        output = func(*args, **kwargs)
        print(time.perf_counter() - start_t)
        return output

    return wrapper


@time_measuring
def trapezoid_method(func, start, end, h=0.0001):
    """Function to calculate an integral using trapezoid method"""
    f = lambdify(x, func)
    ddf = lambdify(x, diff(diff(func_inp, x), x))
    steps = int(abs(end - start) / h)
    result = h * (sum([f(start + h * i) for i in range(1, steps - 1)]) + (f(start) + f(end)) / 2)
    error = - (h ** 3 * sum([ddf((start + h * (i - 1) + start + h * i) / 2) for i in range(1, steps + 1)])) / 12
    return result, abs(simplify(error))


print(trapezoid_method(func_inp, 0, 4))


@time_measuring
def simpson_method(func, start, end, h=0.0001):
    """Function to calculate an integral using Simpson method"""
    f = lambdify(x, func)
    steps = int(abs(end - start) / h)
    result = (h * (sum([f(start + h * i) * (2 * (2 - bool(not i % 2))) for i in range(1, steps - 1)]) + f(start) + f(end))) / 3
    error = 0  # We have to calculate fourth order derivative for function, but we have only square of x is variable with maximum order
    return result, error


print(simpson_method(func_inp, 0, 4))


@time_measuring
def rectangle_method(func, start, end, h=0.0001):
    """Function to calculate an integral using rectangle method"""
    f = lambdify(x, func)
    dff = lambdify(x, diff(diff(func_inp, x), x))
    steps = int(abs(end - start) / h)
    result = h * sum([f((start + i * h + start + (i - 1) * h) / 2) for i in range(1, steps + 1)])
    error = h ** 3 * sum([dff((start + i * h + start * (i - 1) * h) / 2) for i in range(1, steps + 1)])
    return result, simplify(error)


print(rectangle_method(func_inp, 0, 4))
