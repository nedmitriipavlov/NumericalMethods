def function(x):    # original function
    return x * x * x + 2 * x + 4


def new_function(x):    # compression mapping g(x) = -4 / (x * x + 2) = x
    return -4 / (x * x + 2)


def iteration(g, x1, err=0.0001):   # fixed point iteration
    iter = 0

    while True:
        x2 = g(x1)

        if abs(x2 - x1) < err:
            print('num if iteration', iter)
            print('function root', x1)
            return x2

        x1 = x2

        iter += 1


for i in range(0, 101, 10):
    print(i)
    iteration(new_function, i)
    print()
