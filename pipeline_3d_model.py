import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import time

# размеры массива
ax0_max = 40
ax1_max = 40
ax2_max = 40

vertical = np.array([[[0. for i in range(ax0_max + 1)] for j in range(ax1_max + 1)] for n in range(ax2_max + 1)])
# вдоль оси ax1
horizontal_ax1 = deepcopy(vertical)
# вдоль оси ax2
horizontal_ax2 = deepcopy(vertical)


# vertical[ax0][ax1][ax2] ax0 - вертикаль

def cycle(z, vertic=vertical, horizon_ax1=horizontal_ax1, horizon_ax2=horizontal_ax2):
    # для проверки того, как долго работает цикл
    start_time = time.time()

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

    for n in range(z):
        # типо жидкость капает
        vertic[0][ax1_max // 2][ax2_max // 2] = 1

        # копируем массивы
        ver = deepcopy(vertic)
        hor_ax1 = deepcopy(horizon_ax1)
        hor_ax2 = deepcopy(horizon_ax2)
        # условие на прохождение по оси ax0
        if (4 + n // 50) < ax0_max:
            n0 = (4 + n // 50)
        else:
            n0 = ax0_max
        # условия на прохождение по оси ax1
        if (4 + n // 50 + ax1_max // 2) < ax1_max and (ax1_max // 2 - (4 + n // 50)) < ax1_max:
            n1_min = (ax1_max // 2 - (4 + n // 50))
            n1_max = (4 + n // 50 + ax1_max // 2)
        else:
            n1_min = 0
            n1_max = ax1_max

        # условия на прохождение по оси ax2
        if (4 + n // 50 + ax2_max // 2) < ax2_max and (ax2_max // 2 - (4 + n // 50)) < ax2_max:
            n2_min = (ax2_max // 2 - (4 + n // 50))
            n2_max = (4 + n // 50 + ax2_max // 2)
        else:
            n2_min = 0
            n2_max = ax2_max

        for ax0 in range(n0):
            for ax1 in range(n1_min, n1_max):
                for ax2 in range(n2_min, n2_max):
                    # проход по вертикальным трубочкам
                    if vertic[ax0][ax1][ax2] > DOWN_MIN:
                        # то, сколько вытекает
                        down = vertic[ax0][ax1][ax2] * DOWN_PERS
                        # то, сколько перетекает в ось ax1
                        down_ax1 = down * DOWN_PERS_ax1
                        # то, сколько перетекает в ось ax2
                        down_ax2 = down * DOWN_PERS_ax2
                        # то, сколько перетекает в вертикаль нижней ячейки
                        down_down = down * DOWN_PERS_DOWN

                        # то, сколько может втечь в нужную трубочку
                        tube_max_down = (TUBE_MAX - vertic[ax0 + 1][ax1][ax2])
                        tube_max_ax1 = (TUBE_MAX - horizon_ax1[ax0][ax1][ax2])
                        tube_max_ax2 = (TUBE_MAX - horizon_ax2[ax0][ax1][ax2])

                        if (down_ax1 > tube_max_ax1):
                            down_ax1 = tube_max_ax1
                        if (down_ax2 > tube_max_ax2):
                            down_ax2 = tube_max_ax2
                        if (down_down > tube_max_down):
                            down_down = tube_max_down

                        down_stay = down - (down_down + down_ax1 + down_ax2)

                        ver[ax0][ax1][ax2] = vertic[ax0][ax1][ax2] - down + down_stay
                        hor_ax1[ax0][ax1][ax2] = hor_ax1[ax0][ax1][ax2] + down_ax1
                        hor_ax2[ax0][ax1][ax2] = hor_ax2[ax0][ax1][ax2] + down_ax2
                        ver[ax0 + 1][ax1][ax2] = ver[ax0 + 1][ax1][ax2] + down_down

                    # проход по горизонтальным вдоль оси ax1
                    if horizon_ax1[ax0][ax1][ax2] > LR_MIN:

                        spread = horizon_ax1[ax0][ax1][ax2] * LR_PERS
                        # перетикает вправо вдоль оси ax1
                        spread_r = spread * LR_PERS_R
                        # перетикает влево вдоль оси ax1
                        spread_l = spread * LR_PERS_L
                        # перетекает в вертикаль
                        spread_d = spread * LR_PERS_DOWN

                        # дальше, по сути, всё аналогично вретикальному растеканию

                        tube_max_sp_r = TUBE_MAX - horizon_ax1[ax0][ax1 + 1][ax2]
                        tube_max_sp_l = TUBE_MAX - horizon_ax1[ax0][ax1 - 1][ax2]
                        tube_max_sp_d = TUBE_MAX - vertic[ax0][ax1][ax2]

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

                    # проход по горизонтальным вдоль оси ax2
                    if horizon_ax2[ax0][ax1][ax2] > LR_MIN:
                        ax2spread = horizon_ax2[ax0][ax1][ax2] * LR_PERS
                        # перетикает вправо вдоль оси ax1
                        ax2spread_r = ax2spread * LR_PERS_R
                        # перетикает влево вдоль оси ax1
                        ax2spread_l = ax2spread * LR_PERS_L
                        # перетекает в вертикаль
                        ax2spread_d = ax2spread * LR_PERS_DOWN

                        ax2tube_max_sp_r = TUBE_MAX - horizon_ax2[ax0][ax1][ax2 + 1]
                        ax2tube_max_sp_l = TUBE_MAX - horizon_ax2[ax0][ax1][ax2 - 1]
                        ax2tube_max_sp_d = TUBE_MAX - vertic[ax0][ax1][ax2]

                        if ax2spread_d > ax2tube_max_sp_d:
                            ax2spread_d = ax2tube_max_sp_d
                        if ax2spread_l > ax2tube_max_sp_l:
                            ax2spread_l = ax2tube_max_sp_l
                        if ax2spread_r > ax2tube_max_sp_r:
                            ax2spread_r = ax2tube_max_sp_r

                        ax2spread_stay = ax2spread - (ax2spread_d + ax2spread_r + ax2spread_l)

                        hor_ax2[ax0][ax1][ax2] = horizon_ax2[ax0][ax1][ax2] - ax2spread + ax2spread_stay
                        hor_ax2[ax0][ax1][ax2 + 1] = hor_ax2[ax0][ax1][ax2 + 1] + ax2spread_r
                        hor_ax2[ax0][ax1][ax2 - 1] = hor_ax2[ax0][ax1][ax2 - 1] + ax2spread_l
                        ver[ax0][ax1][ax2] = ver[ax0][ax1][ax2] + ax2spread_d

        # опять перезаписываем массивы
        vertic = deepcopy(ver)
        horizon_ax1 = deepcopy(hor_ax1)
        horizon_ax2 = deepcopy(hor_ax2)

    # выводит время работы цикла
    print('Finished cycle in %s seconds' % (time.time() - start_time))
    return vertic, horizon_ax1, horizon_ax2


def graph(result):
    # окно для отрисовки графика
    fig_2d = plt.figure(figsize=(7, 7))
    ax_2d = fig_2d.add_subplot()
    ax_2d.set_title("baze")
    # отображение градиента
    ax_2d.imshow(result)
    plt.show()


def incision(v, h1, h2, ax2_incision=ax2_max // 2):
    # ну а тут у нас по сути разрез берётся
    result = np.array([[0. for f in range(ax0_max)] for g in range(ax1_max)])
    for ax0 in range(ax0_max):
        for ax1 in range(ax1_max):
            result[ax0][ax1] = v[ax0][ax1][ax2_incision] + h1[ax0][ax1][ax2_incision] + h2[ax0][ax1][ax2_incision]
    return result

# v, h1, h2 = cycle(400)
# вызов разреза
# RES = incision(v, h1, h2)
# вызов графика
# graph(RES)
