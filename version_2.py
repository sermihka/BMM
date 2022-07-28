from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.animation import ArtistAnimation

# окно для отображения 3d графика
fig_3d = plt.figure(figsize=(10, 7))
frames_3d = [] # для анимации

# окно для отображения 2d графика
fig_2d = plt.figure(figsize=(7, 7))
frames_2d = [] # для анимации

ax_3d = fig_3d.add_subplot(projection='3d')
ax_3d.xaxis.set_major_locator(MultipleLocator(base=1))
ax_3d.yaxis.set_major_locator(MultipleLocator(base=1))
ax_3d.zaxis.set_major_locator(MultipleLocator(base=1))


ax_2d = fig_2d.add_subplot()
ax_2d.xaxis.set_major_locator(MultipleLocator(base=1))
ax_2d.yaxis.set_major_locator(MultipleLocator(base=1))

# создание трёхмерного массива
capacity = np.array([[[0 for i in range(20)] for j in range(20)] for m in range(20)])
sh = capacity.shape # размер массива

# создание двухмерного
capacity_2d = np.array([[0 for n in range(20)] for h in range(20)])

# массивы для отрисовки 3d
xgrid = np.array([], dtype="int8")
ygrid = np.array([], dtype="int8")
zgrid = np.array([], dtype="int8")

# для отрисовки 2d
x_2d = np.array([], dtype="int8")
y_2d = np.array([], dtype="int8")

# Заполнение основного массива, а также массивов для отрисовки песчинок
for ax0 in range(0, sh[0], 2):
    for ax2 in range(0, sh[2], 2):
        x_2d = np.append(xgrid, ax0)
        y_2d = np.append(ygrid, ax2)

        capacity_2d[ax0][ax2] = 1

        for ax1 in range(0, sh[1], 2):

            capacity[ax0][ax1][ax2] = 1

            xgrid = np.append(xgrid, ax0)
            ygrid = np.append(ygrid, ax1)
            zgrid = np.append(zgrid, ax2)


def liquid_start(V, mas_V, mas_S, capacity_2d, capacity):
    a = 7
    # начальный объём a*b*h
    b = 12
    l = b - a # 5
    # получается у нас в начальной ситуации всего 16 отверстий в которые течёт вода
    V_0 = V/16
    # стартовая площадь a*b
    os = 19
    # номер оси z в которой мы будем заливать воду

    for i in range(a, b):
        capacity_2d[i][os] = 2
        st = str(i)  + " " + str(os)
        mas_S[st] = V_0
    capacity_2d[a-1][os] = 3
    capacity_2d[b][os] = 3


    for ax0 in range(a, b):
        capacity[a - 1][ax0][os] = 3
        capacity[ax0][a - 1][os] = 3
        capacity[b][ax0][os] = 3
        capacity[ax0][b][os] = 3
        for ax1 in range(a, b):
            capacity[ax0][ax1][os] = 2
            st3 = str(ax0) + " " + str(ax1) + " " + str(os)
            mas_V[st3] = V_0

    #print(capacity)
    return capacity, capacity_2d, mas_V, mas_S


def spread_3d(mas_V, cap3, cap_3d, x, y, z, v_crit = 3.5 * 10**(-13)):

    # функция правил растекания для 3d
    sh = cap3.shape

    """count = 0
    sh = cap3.shape
    st = str(x) + " " + str(y)
    v = mas_V.get(st)"""

    if x - 1 > 0:
        if cap_3d[x - 1][y][z] == 0:
            cap3[x - 1][y][z] = 2
    if x + 1 < sh[0]:
        if cap_3d[x + 1][y][z] == 0:
            cap3[x + 1][y][z] = 2


    if z - 1 > 0:
        if cap_3d[x][y][z - 1] == 0:
            cap3[x][y][z - 1] = 2



    if y + 1 < sh[1]:
        if cap_3d[x][y + 1][z] == 0:
            cap3[x][y + 1][z] = 2
    if y - 1 > 0:
        if cap_3d[x][y - 1][z] == 0:
            cap3[x][y - 1][z] = 2

    return cap3, mas_V

def spread_2d(cap, cap_2d, x, y, mas_S, v_crit = 3.5 * 10**(-13)):
    # функция правил растекания для 2d
    count = 0
    sh = cap.shape
    st = str(x) + " " + str(y)
    v = mas_S.get(st)
    if v > v_crit:

        if x + 1 < sh[0]:
            if cap_2d[x + 1][y] == 0:
                if cap_2d[x + 2][y] == 0:
                    s = str(x + 1) + " " + str(y)
                    mas_S[s] = (v - v_crit) * 0.1875
                    cap[x + 1][y] = 2
                elif cap_2d[x + 1][y] == 2:
                    s = str(x + 1) + " " + str(y)
                    v = v - (0.5 * v_crit)
                    mas_S[s] = v_crit
                    cap[x + 1][y] = 2

        if y - 1 > 0:
            if cap_2d[x][y - 1] == 0:
                s = str(x) + " " + str(y - 1)
                mas_S[s] = (v - v_crit)*0.25
                cap[x][y - 1] = 2

        if x - 1 > 0:
            if cap_2d[x - 1][y] == 0:
                if cap_2d[x - 2][y] == 2:
                    s = str(x - 1) + " " + str(y)
                    v = v - (0.5 * v_crit)
                    mas_S[s] = v_crit
                    cap[x - 1][y] = 2
                elif cap_2d[x - 2][y] == 0:
                    s = str(x - 1) + " " + str(y)
                    mas_S[s] = (v - v_crit) * 0.1875
                    cap[x - 1][y] = 2

    else:
        count = 1


    return cap , count

def func():
    mas_V = {}
    mas_S = {}
    V = 300 * 3.5 * 10**(-10)
    cap_3d, cap_2d, mas_V, mas_S = liquid_start(V, mas_V, mas_S, capacity_2d, capacity)

    cap = deepcopy(cap_2d)
    cap3 = deepcopy(cap_3d)

    # массивы для анимации
    x_li_2d = np.array([], dtype="int8")
    y_li_2d = np.array([], dtype="int8")

    x_li_3d = np.array([], dtype="int16")
    y_li_3d = np.array([], dtype="int16")
    z_li_3d = np.array([], dtype="int16")


    sh_2d = cap_2d.shape
    sh_3d = cap_3d.shape

    count = 0
    while count == 0:
        for ax0 in range(sh_2d[0]):
            for ax1 in range(sh_2d[1]):
                if cap_2d[ax0][ax1] == 2:
                    x_li_2d = np.append(x_li_2d, ax0)
                    y_li_2d = np.append(y_li_2d, ax1)
                    cap, count = spread_2d(cap, cap_2d, ax0, ax1, mas_S)

        for ax_0 in range(sh_3d[0]):
            for ax_1 in range(sh_3d[1]):
                for ax_2 in range(sh_3d[2]):
                    if cap_3d[ax_0][ax_1][ax_2] == 2:
                        x_li_3d = np.append(x_li_3d, ax_0)
                        y_li_3d = np.append(y_li_3d, ax_1)
                        z_li_3d = np.append(z_li_3d, ax_2)
                        cap3, mas_V = spread_3d(mas_V, cap3, cap_3d, ax_0, ax_1, ax_2)

        cap_3d = deepcopy(cap3)
        cap_2d = deepcopy(cap)
        # заполнение фреймов
        line1 = ax_3d.scatter(x_li_3d, y_li_3d, z_li_3d, color="blue")
        frames_3d.append([line1])

        line = ax_2d.scatter(x_li_2d, y_li_2d, color="blue")
        frames_2d.append([line])






func()

# ОТРИСОВКА
animation_2d = ArtistAnimation(
    fig_2d,                # фигура, где отображается анимация
    frames_2d,              # кадры
    interval=100,        # задержка между кадрами в мс
    blit=True,          # использовать ли двойную буферизацию
    repeat=True)

animation_3d = ArtistAnimation(
    fig_3d,                # фигура, где отображается анимация
    frames_3d,              # кадры
    interval=100,        # задержка между кадрами в мс
    blit=True,          # использовать ли двойную буферизацию
    repeat=True)


gr_2d = ax_2d.scatter(x_2d, y_2d, color="black")
gr_3d = ax_3d.scatter(xgrid, ygrid, zgrid, color='black')

plt.show()