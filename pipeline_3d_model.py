import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import time
# окно для отрисовки графика

fig_2d = plt.figure(figsize=(7, 7))

ax_2d = fig_2d.add_subplot()
ax_2d.set_title("baze")

ax0_max = 40
ax1_max = 40
ax2_max = 40

vertical = np.array([[[0. for i in range(ax0_max + 1)] for j in range(ax1_max + 1)] for n in range(ax2_max + 1)])
# вдоль оси ax1
horizontal_ax1 = deepcopy(vertical)
# вдоль оси ax2
horizontal_ax2 = deepcopy(vertical)
# vertical[y][x] y - вертикаль, х - горизонталь

# максимально возможное значение в трубочке
TUBE_MAX = 1.0
# минимально количество жидкости в трубочке
# по вертикали после которого вода течёт
DOWN_MIN = 0.1
# процент от объёма воды, который утекает
DOWN_PERS = 0.3
# процент(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax1
DOWN_PERS_ax1 = 0.3
# процент(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax2
DOWN_PERS_ax2 = 0.3
# процент(от DOWN_PERS) который переходит в вертикаль ячейки, которая ниже
DOWN_PERS_DOWN = 1.0 - DOWN_PERS_ax1 - DOWN_PERS_ax2

# минимальноеколичество по горизонтали для вытекания
LR_MIN = 0.01
# Сколько вытекает в общем
LR_PERS = 0.3
# то, сколько перетекает в бок
LR_PERS_L = 0.3
LR_PERS_R = 0.3
# то, сколько перетекает в вертикаль
LR_PERS_DOWN = 1.0 - (LR_PERS_L + LR_PERS_R)

# для проверки того, как долго работает прога
start_time = time.time()

for n in range(300):
    vertical[0][ax1_max//2][ax2_max//2] = 1

    ver = deepcopy(vertical)
    hor_ax1 = deepcopy(horizontal_ax1)
    hor_ax2 = deepcopy(horizontal_ax2)


    for ax0 in range(ax0_max):
        for ax1 in range(ax1_max):
            for ax2 in range(ax2_max):

                if vertical[ax0][ax1][ax2] > DOWN_MIN:
                    # то, сколько вытекает
                    down = vertical[ax0][ax1][ax2] * DOWN_PERS
                    # то, сколько перетекает в ось ax1
                    down_ax1 = down*DOWN_PERS_ax1
                    # то, сколько перетекает в ось ax2
                    down_ax2 = down * DOWN_PERS_ax2
                    # то, сколько перетекает в вертикаль нижней ячейки
                    down_down = down * DOWN_PERS_DOWN

                    # то, сколько может втечь в нужную трубочку
                    tube_max_down = (TUBE_MAX - vertical[ax0 + 1][ax1][ax2])
                    tube_max_ax1 = (TUBE_MAX - horizontal_ax1[ax0][ax1][ax2])
                    tube_max_ax2 = (TUBE_MAX - horizontal_ax2[ax0][ax1][ax2])

                    if  (down_ax1 > tube_max_ax1):
                        down_ax1 = tube_max_ax1
                    if  (down_ax2 > tube_max_ax2):
                        down_ax2 = tube_max_ax2
                    if  (down_down > tube_max_down):
                        down_down = tube_max_down

                    down_stay = down - (down_down + down_ax1 + down_ax2)

                    ver[ax0][ax1][ax2] = vertical[ax0][ax1][ax2] - down + down_stay
                    hor_ax1[ax0][ax1][ax2] = hor_ax1[ax0][ax1][ax2] + down_ax1
                    hor_ax2[ax0][ax1][ax2] = hor_ax2[ax0][ax1][ax2] + down_ax2
                    ver[ax0 + 1][ax1][ax2] = ver[ax0 + 1][ax1][ax2] + down_down

                if horizontal_ax1[ax0][ax1][ax2] > LR_MIN:

                    spread = horizontal_ax1[ax0][ax1][ax2] * LR_PERS
                    # перетикает вправо вдоль оси ax1
                    spread_r = spread * LR_PERS_R
                    # перетикает влево вдоль оси ax1
                    spread_l = spread * LR_PERS_L
                    # перетекает в вертикаль
                    spread_d = spread * LR_PERS_DOWN

                    tube_max_sp_r = TUBE_MAX - horizontal_ax1[ax0][ax1 + 1][ax2]
                    tube_max_sp_l = TUBE_MAX - horizontal_ax1[ax0][ax1 - 1][ax2]
                    tube_max_sp_d = TUBE_MAX - vertical[ax0][ax1][ax2]

                    if spread_d > tube_max_sp_d:
                        spread_d = tube_max_sp_d
                    if spread_l > tube_max_sp_l:
                        spread_l = tube_max_sp_l
                    if spread_r > tube_max_sp_r:
                        spread_r = tube_max_sp_r

                    spread_stay = spread - (spread_d + spread_r + spread_l)

                    hor_ax1[ax0][ax1][ax2] = hor_ax1[ax0][ax1][ax2] - spread + spread_stay
                    hor_ax1[ax0][ax1 + 1][ax2] = hor_ax1[ax0][ax1 + 1][ax2] + spread_r
                    hor_ax1[ax0][ax1 - 1][ax2] = hor_ax1[ax0][ax1 - 1][ax2] + spread_l
                    ver[ax0][ax1][ax2] = ver[ax0][ax1][ax2] + spread_d

                # то же самое, по оси ax2
                if horizontal_ax2[ax0][ax1][ax2] > LR_MIN:
                    ax2spread = horizontal_ax2[ax0][ax1][ax2] * LR_PERS
                    # перетикает вправо вдоль оси ax1
                    ax2spread_r = ax2spread * LR_PERS_R
                    # перетикает влево вдоль оси ax1
                    ax2spread_l = ax2spread * LR_PERS_L
                    # перетекает в вертикаль
                    ax2spread_d = ax2spread * LR_PERS_DOWN

                    ax2tube_max_sp_r = TUBE_MAX - horizontal_ax2[ax0][ax1][ax2 + 1]
                    ax2tube_max_sp_l = TUBE_MAX - horizontal_ax2[ax0][ax1][ax2 - 1]
                    ax2tube_max_sp_d = TUBE_MAX - vertical[ax0][ax1][ax2]

                    if ax2spread_d > ax2tube_max_sp_d:
                        ax2spread_d = ax2tube_max_sp_d
                    if ax2spread_l > ax2tube_max_sp_l:
                        ax2spread_l = ax2tube_max_sp_l
                    if ax2spread_r > ax2tube_max_sp_r:
                        ax2spread_r = ax2tube_max_sp_r

                    ax2spread_stay = ax2spread - (ax2spread_d + ax2spread_r + ax2spread_l)

                    hor_ax2[ax0][ax1][ax2] = horizontal_ax2[ax0][ax1][ax2] - ax2spread + ax2spread_stay
                    hor_ax2[ax0][ax1][ax2 + 1] = hor_ax2[ax0][ax1][ax2 + 1] + ax2spread_r
                    hor_ax2[ax0][ax1][ax2 - 1] = hor_ax2[ax0][ax1][ax2 - 1] + ax2spread_l
                    ver[ax0][ax1][ax2] = ver[ax0][ax1][ax2] + ax2spread_d
    vertical = deepcopy(ver)
    horizontal_ax1 = deepcopy(hor_ax1)
    horizontal_ax2 = deepcopy(hor_ax2)
print('Finished cycle in %s seconds' % (time.time() - start_time))
result = np.array([[0. for i in range(ax0_max)] for j in range(ax1_max)])
for ax0 in range(ax0_max):
    for ax1 in range(ax1_max):
        result[ax0][ax1] = vertical[ax0][ax1][ax2_max//2]


ax_2d.imshow(result)

plt.show()
