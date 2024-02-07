def function(x):    # original function
    return x * x * x + 2 * x + 4


def derivate(x):     # derivative of function
    return 3*x*x+2


def newton(f, d, x1, err=0.0001):   # newton's method
    iter = 0

    while True:
        x2 = -f(x1) / d(x1) + x1

        if abs(x2 - x1) < err:
            print('num if iteration', iter)
            print('function root', x2)
            return x2

        x1 = x2

        iter += 1


for i in range(0, 100, 10):
    print(i)
    newton(function, derivate, i)
    print()


