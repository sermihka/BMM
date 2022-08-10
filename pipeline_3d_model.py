import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import time
from tqdm import tqdm

# размеры массива
ax0_max = 40
ax1_max = 40
ax2_max = 40

# двумерный массив, для имитации склона
tr = np.tri(ax0_max, ax1_max, -1)

# массивы трубочек
vertical = np.array([[[0. for i in range(ax0_max + 1)] for j in range(ax1_max + 1)] for n in range(ax2_max + 1)])
# вдоль оси ax1
horizontal_ax1 = deepcopy(vertical)
# вдоль оси ax2
horizontal_ax2 = deepcopy(vertical)


# vertical[ax0][ax1][ax2] ax0 - вертикаль

def cycle(z, count=0, list=np.array([[0, 0.1, 0.4, 0.3, 0.3, 0.01, 0.3, 0.3, 0.3]]),
          # массив слоёв(хранит высоту их начала и коэффиценты)
          vertic=vertical,
          horizon_ax1=horizontal_ax1,
          horizon_ax2=horizontal_ax2
          ):
    global tr
    DOWN_MIN = 0.1  # минимально количество жидкости в трубочке по вертикали после которого вода течёт
    DOWN_PERS = 0.4  # доля от объёма воды, которая утекает
    DOWN_PERS_ax1 = 0.3  # доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax1
    DOWN_PERS_ax2 = 0.3  # доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax2
    LR_MIN = 0.05  # минимальноеколичество по горизонтали для вытекания
    LR_PERS = 0.3  # Сколько вытекает в общем
    LR_PERS_L = 0.3  # то, сколько перетекает в бок
    LR_PERS_R = 0.3
    # для проверки того, как долго работает цикл
    start_time = time.time()

    TUBE_MAX = 1.0  # максимально возможное значение в трубочке

    # значения
    n_v_1 = 3
    n_h_1 = 3
    sh_list = np.shape(list)
    print(sh_list)
    for n in tqdm(range(z)):

        # типо жидкость капает
        vertic[0][ax1_max // 2][ax2_max // 2] = 1

        # копируем массивы
        ver = deepcopy(vertic)
        hor_ax1 = deepcopy(horizon_ax1)
        hor_ax2 = deepcopy(horizon_ax2)

        # проверка на то, что мы не выходим за рамки массива
        if n_v_1 < ax0_max:
            n_v = n_v_1
        else:
            print("усё")
            break
        if n_h_1 < ax1_max:
            n_h = n_h_1
        else:
            print("усё")
            break
        # Прохождения по массивам и "распространение жидкости"
        for ax0 in range(n_v):
            if count == 0:
                for y in range(sh_list[0]):

                    """
                    Проверка того, на каком слое мы находимся
                    и установка соответсвующих коэффицентов
                    """
                    if list[y][0] <= ax0:
                        DOWN_MIN = list[y][
                            1]  # минимально количество жидкости в трубочке по вертикали после которого вода течёт
                        DOWN_PERS = list[y][2]  # доля от объёма воды, которая утекает
                        DOWN_PERS_ax1 = list[y][
                            3]  # доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax1
                        DOWN_PERS_ax2 = list[y][
                            4]  # доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax2
                        LR_MIN = list[y][5]  # минимальноеколичество по горизонтали для вытекания
                        LR_PERS = list[y][6]  # Сколько вытекает в общем
                        LR_PERS_L = list[y][7]  # то, сколько перетекает в бок
                        LR_PERS_R = list[y][8]

            # процент(от DOWN_PERS) который переходит в вертикаль ячейки, которая ниже
            DOWN_PERS_DOWN = 1.0 - DOWN_PERS_ax1 - DOWN_PERS_ax2

            # то, сколько перетекает в вертикаль
            LR_PERS_DOWN = 1.0 - (LR_PERS_L + LR_PERS_R)
            for ax1 in range((ax1_max // 2) - n_h, (ax1_max // 2) + n_h):
                if count == 1:
                    if tr[ax0][ax1] > 0:
                        DOWN_MIN = list[1][1]
                        DOWN_PERS = list[1][2]
                        DOWN_PERS_ax1 = list[1][3]
                        DOWN_PERS_ax2 = list[1][4]
                        LR_MIN = list[1][5]
                        LR_PERS = list[1][6]
                        LR_PERS_L = list[1][7]
                        LR_PERS_R = list[1][8]
                    else:
                        DOWN_MIN = list[0][1]
                        DOWN_PERS = list[0][2]
                        DOWN_PERS_ax1 = list[0][3]
                        DOWN_PERS_ax2 = list[0][4]
                        LR_MIN = list[0][5]
                        LR_PERS = list[0][6]
                        LR_PERS_L = list[0][7]
                        LR_PERS_R = list[0][8]
                for ax2 in range((ax2_max // 2) - n_h, (ax2_max // 2) + n_h):
                    # проход по вертикальным трубочкам
                    if vertic[ax0][ax1][ax2] > DOWN_MIN:
                        if ax0 + 1 == n_v:
                            n_v_1 += 1
                        # то, сколько вытекает
                        down = vertic[ax0][ax1][ax2] * DOWN_PERS
                        # то, сколько перетекает в ось ax1
                        down_ax1 = down * DOWN_PERS_ax1
                        # то, сколько перетекает в ось ax2
                        down_ax2 = down * DOWN_PERS_ax2
                        # то, сколько перетекает в вертикаль нижней ячейки
                        down_down = down * DOWN_PERS_DOWN

                        # то, сколько может втечь в нужную трубочку
                        tube_max_down = (TUBE_MAX - ver[ax0 + 1][ax1][ax2])
                        tube_max_ax1 = (TUBE_MAX - hor_ax1[ax0][ax1][ax2])
                        tube_max_ax2 = (TUBE_MAX - hor_ax2[ax0][ax1][ax2])

                        # проверка на излишки
                        if (down_ax1 > tube_max_ax1):
                            down_ax1 = tube_max_ax1
                        if (down_ax2 > tube_max_ax2):
                            down_ax2 = tube_max_ax2
                        if (down_down > tube_max_down):
                            down_down = tube_max_down

                        down_stay = down - (down_down + down_ax1 + down_ax2)

                        ver[ax0][ax1][ax2] = ver[ax0][ax1][ax2] - down + down_stay
                        hor_ax1[ax0][ax1][ax2] = hor_ax1[ax0][ax1][ax2] + down_ax1
                        hor_ax2[ax0][ax1][ax2] = hor_ax2[ax0][ax1][ax2] + down_ax2
                        ver[ax0 + 1][ax1][ax2] = ver[ax0 + 1][ax1][ax2] + down_down

                    # проход по горизонтальным вдоль оси ax1
                    if horizon_ax1[ax0][ax1][ax2] > LR_MIN:
                        if ax1 + 1 == (ax1_max // 2) + n_h or ax1 - 1 == (ax1_max // 2) - n_h:
                            n_h_1 += 1
                        spread = horizon_ax1[ax0][ax1][ax2] * LR_PERS
                        # перетикает вправо вдоль оси ax1
                        spread_r = spread * LR_PERS_R
                        # перетикает влево вдоль оси ax1
                        spread_l = spread * LR_PERS_L
                        # перетекает в вертикаль
                        spread_d = spread * LR_PERS_DOWN

                        # дальше, по сути, всё аналогично вретикальному растеканию

                        tube_max_sp_r = TUBE_MAX - hor_ax1[ax0][ax1 + 1][ax2]
                        tube_max_sp_l = TUBE_MAX - hor_ax1[ax0][ax1 - 1][ax2]
                        tube_max_sp_d = TUBE_MAX - ver[ax0][ax1][ax2]

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

                        ax2tube_max_sp_r = TUBE_MAX - hor_ax2[ax0][ax1][ax2 + 1]
                        ax2tube_max_sp_l = TUBE_MAX - hor_ax2[ax0][ax1][ax2 - 1]
                        ax2tube_max_sp_d = TUBE_MAX - ver[ax0][ax1][ax2]

                        if ax2spread_d > ax2tube_max_sp_d:
                            ax2spread_d = ax2tube_max_sp_d
                        if ax2spread_l > ax2tube_max_sp_l:
                            ax2spread_l = ax2tube_max_sp_l
                        if ax2spread_r > ax2tube_max_sp_r:
                            ax2spread_r = ax2tube_max_sp_r

                        ax2spread_stay = ax2spread - (ax2spread_d + ax2spread_r + ax2spread_l)

                        hor_ax2[ax0][ax1][ax2] = hor_ax2[ax0][ax1][ax2] - ax2spread + ax2spread_stay
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


def graph(result, ax2_incision=ax2_max // 2):
    # окно для отрисовки графика
    fig_2d = plt.figure(figsize=(7, 7))
    ax_2d = fig_2d.add_subplot()
    ax_2d.set_title("разрез по оси ax2" + '\n' + "по координате " + str(ax2_incision))
    # отображение градиента
    ax_2d.imshow(result)
    plt.show()


def incision(v, h1, h2, ax2_incision=ax2_max // 2):
    """
    здесь формируется итоговый массив, который отображется в итоге на графике
    с помощью градиента
    """

    result = np.array([[0. for f in range(ax0_max)] for g in range(ax1_max)])
    for ax0 in range(ax0_max):
        for ax1 in range(ax1_max):
            result[ax0][ax1] = v[ax0][ax1][ax2_incision] + h1[ax0][ax1][ax2_incision] + h2[ax0][ax1][ax2_incision]
    return result

# v, h1, h2 = cycle(500)
# вызов разреза
# RES = incision(v, h1, h2)
# вызов графика
# graph(RES)
