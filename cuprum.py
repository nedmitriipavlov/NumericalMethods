
import matplotlib.pyplot as plt
import numpy as np

rgb = lambda: np.random.randint(0, 255)

l = 10  # cm
t = 10  # seconds

T_room = 21+273  # room temperature
T_melt = 1083+273  # melting temperature
coef = 373/(8.2*386)  # heat transfer coefficient


def nodes(c, Tox = T_room, T00 =  T_melt/2, delta_t=0.1, delta_l=0.25):
    k = c * delta_t / (delta_l ** 2)
    t_num = int(t / delta_t)
    l_num = int(l / delta_l)
    matrix = [[T00]+[Tox for j in range(l_num-1)] for i in range(t_num)]
    for i in range(1, t_num):
        for j in range(1, l_num-1):
            matrix[i][j] = matrix[i-1][j] + k*(matrix[i-1][j-1] + matrix[i-1][j+1] - 2*matrix[i-1][j])
    start = 9
    values = [matrix[i] for i in range(start, int(t/delta_t), int(2/delta_t))]
    for i in range(len(values)):
        clr = '#%02X%02X%02X' % (rgb(), rgb(),rgb())
        plt.plot(np.arange(0, l, delta_l), values[i], color=clr, label='T={} s'.format(start+delta_t*i))
    plt.xlabel('x, cm')
    plt.ylabel('T, K')
    plt.legend()
    plt.show()




data = nodes(coef)
print(data)



