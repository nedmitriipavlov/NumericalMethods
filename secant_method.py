def function(x):    # original function
    return x * x * x + 2 * x + 4


def secant(f, x1, x2, err=0.0001):  # метод секущих
    iter = 0

    while True:
        x3 = x1 - (x2 - x1) * f(x1) / (f(x2) - f(x1))

        if abs(x3 - x2) < err:
            print('num of iteration', iter)
            print('function root', x3)
            return x3

        x1 = x2
        x2 = x3

        iter += 1


for i in range(10, 111, 10):
    print(i)
    secant(function, 0, i)
    print()
