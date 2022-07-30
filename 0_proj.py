from copy import deepcopy
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.animation import ArtistAnimation

fig_2d = plt.figure(figsize=(7, 7))
frames_2d = []

ax_2d = fig_2d.add_subplot()

# коэфицент распространения по горизонтали
coef_horiz = 0.18
# коэфицент распространения по вертикали вниз
coef_vertical_down = 0.24
# коэфицент распространения по вертикали вверх
coef_vertical_up = 0.04
# по сути можно просто написать так:
coef_vertical = 0.2



capacity_2d = np.array([[0 for n in range(100)] for h in range(100)])
# словарь узлов и привязанных к ним значений
#map_node_0 = {}

#sh = capacity_2d.shape
#x_start = int(sh[0]/2)
#Start = str(x_start) + " " + str(sh[1] - 1)

# [a, b, c, d]
# a - отвечает за левую трубочку
# b - за верхнюю
# с - за правую
# d - за нижнюю
# 3.5*10**(-13)
#map_node_0[Start] = [0, 3.5, 0, 0]
#print(map_node_0)

#map_node_1 = deepcopy(map_node_0)

"""def spread(map_node_0, map_node_1, num_elem, val):
    global capacity_2d
    # коэфицент распространения по горизонтали
    coef_horiz = 0.18
    # коэфицент распространения по вертикали вниз
    coef_vertical_down = 0.24
    # коэфицент распространения по вертикали вверх
    coef_vertical_up = 0.04
    # по сути можно просто написать так:
    coef_vertical = 0.2


    for num_elem in map_node_0:
        val = map_node_0.get(num_elem)
        baze = val[1]
        val[0] = coef_horiz * baze
        val[2] = coef_horiz * baze
        val[3] = coef_vertical * baze
        spl = num_elem.split()
        capacity_2d[int(spl[0])][int(spl[1])] = 0
"""


# проходим 100 итераций
"""for n in range(1):

    for num_elem in map_node_0:
        val = map_node_0.get(num_elem)
        print(val)
        print(num_elem.split())
"""