import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import time
# from numba import
# для проверки на затраты времени на выполнение проги
start_time1 = time.time()


# окно для отображения 3d графика
fig_3d = plt.figure(figsize=(10, 7))

# окно для отображения 2d графика
fig_2d = plt.figure(figsize=(7, 7))


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

# массивы для отрисовки 3d
xgrid = np.array([], dtype="int8")
ygrid = np.array([], dtype="int8")
zgrid = np.array([], dtype="int8")
# для отрисовки 2d
x_2d = np.array([], dtype="int8")
y_2d = np.array([], dtype="int8")
start_time = time.time()
# Заполнение основного массива, а также массивов для отрисовки песчинок
for ax0 in range(0, sh[0], 2):
    for ax2 in range(0, sh[2], 2):
        x_2d = np.append(xgrid, ax0)
        y_2d = np.append(ygrid, ax2)
        for ax1 in range(0, sh[1], 2):

            capacity[ax0][ax1][ax2] = 1

            xgrid = np.append(xgrid, ax0)
            ygrid = np.append(ygrid, ax1)
            zgrid = np.append(zgrid, ax2)

print('Finished cycle in %s seconds' % (time.time() - start_time))








# ОТРИСОВКА
gr_2d = ax_2d.scatter(x_2d, y_2d, color="black")
gr_3d = ax_3d.scatter(xgrid, ygrid, zgrid, color='black')


print('Finished in %s seconds' % (time.time() - start_time1))
plt.show()