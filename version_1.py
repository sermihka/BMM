from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.animation import ArtistAnimation


# окно для отображения 3d графика
fig_3d = plt.figure(figsize=(10, 7))
frames_3d = []  # для анимации
# окно для отображения 2d графика
fig_2d = plt.figure(figsize=(7, 7))
frames_2d = []  # для анимации

ax_3d = fig_3d.add_subplot(projection='3d')
ax_3d.xaxis.set_major_locator(MultipleLocator(base=1))
ax_3d.yaxis.set_major_locator(MultipleLocator(base=1))
ax_3d.zaxis.set_major_locator(MultipleLocator(base=1))

ax_2d = fig_2d.add_subplot()
ax_2d.xaxis.set_major_locator(MultipleLocator(base=1))
ax_2d.yaxis.set_major_locator(MultipleLocator(base=1))

# создание трёхмерного массива
capacity = np.array([[[0 for i in range(20)] for j in range(20)] for m in range(20)])
sh = capacity.shape  # размер массива

# создание трёхмерного
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




def liquid_start(capacity_2d, capacity):
    St_volume = 0
    # начальный объём a*b*h
    St_square = 0
    # стартовая площадь a*b
    os = 19
    # номер оси z в которой мы будем заливать воду

    for i in range(7, 12):
        capacity_2d[i][os] = 2
    # print(capacity_2d)
    for ax0 in range(7, 12):
        for ax1 in range(7, 12):
            capacity[ax0][ax1][os] = 2

    return capacity, capacity_2d


# массивы для анимации
x_li_2d = np.array([], dtype="int8")
y_li_2d = np.array([], dtype="int8")

x_li_3d = np.array([], dtype="int16")
y_li_3d = np.array([], dtype="int16")
z_li_3d = np.array([], dtype="int16")


def spread_3d(cap3, cap_3d, x, y, z, V=3.5 * 10 ** (-12), v_crit=3.5 * 10 ** (-13)):
    # функция правил растекания для 3d
    sh = cap3.shape

    if z - 1 > 0:
        if cap_3d[x][y][z - 1] == 0:
            cap3[x][y][z - 1] = 2
    if x - 1 > 0:
        if cap_3d[x - 1][y][z] == 0:
            cap3[x - 1][y][z] = 2
    if x + 1 < sh[0]:
        if cap_3d[x + 1][y][z] == 0:
            cap3[x + 1][y][z] = 2

    if y + 1 < sh[1]:
        if cap_3d[x][y + 1][z] == 0:
            cap3[x][y + 1][z] = 2
    if y - 1 > 0:
        if cap_3d[x][y - 1][z] == 0:
            cap3[x][y - 1][z] = 2

    return cap3


def spread_2d(cap, cap_2d, x, y):
    # функция правил растекания для 2d
    sh = cap.shape

    if y - 1 > 0:
        if cap_2d[x][y - 1] == 0:
            cap[x][y - 1] = 2
    if x + 1 < sh[0]:
        if cap_2d[x + 1][y] == 0:
            cap[x + 1][y] = 2
    if x - 1 > 0:
        if cap_2d[x - 1][y] == 0:
            cap[x - 1][y] = 2

    return cap


def func():
    print(capacity_2d)
    cap_3d, cap_2d = liquid_start(capacity_2d, capacity)
    # print(cap_2d)
    cap = deepcopy(cap_2d)
    cap3 = deepcopy(cap_3d)
    global x_li_2d
    global y_li_2d

    global x_li_3d
    global y_li_3d
    global z_li_3d
    mas_V = {}

    sh_2d = cap_2d.shape
    sh_3d = cap_3d.shape

    count = 0
    while count < 5:
        for ax0 in range(sh_2d[0]):
            for ax1 in range(sh_2d[1]):
                if cap_2d[ax0][ax1] == 2:
                    x_li_2d = np.append(x_li_2d, ax0)
                    y_li_2d = np.append(y_li_2d, ax1)
                    cap = spread_2d(cap, cap_2d, ax0, ax1)

        for ax_0 in range(sh_3d[0]):
            for ax_1 in range(sh_3d[1]):
                for ax_2 in range(sh_3d[2]):
                    if cap_3d[ax_0][ax_1][ax_2] == 2:
                        x_li_3d = np.append(x_li_3d, ax_0)
                        y_li_3d = np.append(y_li_3d, ax_1)
                        z_li_3d = np.append(z_li_3d, ax_2)
                        cap3 = spread_3d(cap3, cap_3d, ax_0, ax_1, ax_2)

        cap_3d = deepcopy(cap3)

        cap_2d = deepcopy(cap)

        # заполнение фреймов
        line1 = ax_3d.scatter(x_li_3d, y_li_3d, z_li_3d, color="blue")
        frames_3d.append([line1])

        line = ax_2d.scatter(x_li_2d, y_li_2d, color="blue")
        frames_2d.append([line])

        count += 1


func()

# ОТРИСОВКА
animation_2d = ArtistAnimation(
    fig_2d,  # фигура, где отображается анимация
    frames_2d,  # кадры
    interval=100,  # задержка между кадрами в мс
    blit=True,  # использовать ли двойную буферизацию
    repeat=True)

animation_3d = ArtistAnimation(
    fig_3d,  # фигура, где отображается анимация
    frames_3d,  # кадры
    interval=100,  # задержка между кадрами в мс
    blit=True,  # использовать ли двойную буферизацию
    repeat=True)


gr_2d = ax_2d.scatter(x_2d, y_2d, color="black")
gr_3d = ax_3d.scatter(xgrid, ygrid, zgrid, color='black')

plt.show()

print('finish')
