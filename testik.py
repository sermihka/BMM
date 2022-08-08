import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import time

# размеры массива


vertical = np.array([[[0. for i in range(4)] for j in range(4)] for n in range(4)])
# вдоль оси ax1
horizontal_ax1 = deepcopy(vertical)
# вдоль оси ax2
horizontal_ax2 = deepcopy(vertical)


# vertical[ax0][ax1][ax2] ax0 - вертикаль

def cycle(z,
          DOWN_MIN=0.1,  # минимально количество жидкости в трубочке по вертикали после которого вода течёт
          DOWN_PERS=0.4,  # доля от объёма воды, которая утекает
          DOWN_PERS_ax1=0.3,  # доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax1
          DOWN_PERS_ax2=0.3,  # доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax2
          LR_MIN=0.05,  # минимальноеколичество по горизонтали для вытекания
          LR_PERS=0.3,  # Сколько вытекает в общем
          LR_PERS_L=0.3,  # то, сколько перетекает в бок
          LR_PERS_R=0.3,
          vertic=vertical,
          horizon_ax1=horizontal_ax1,
          horizon_ax2=horizontal_ax2
          ):
    # для проверки того, как долго работает цикл
    start_time = time.time()

    TUBE_MAX = 1.0  # максимально возможное значение в трубочке

    # процент(от DOWN_PERS) который переходит в вертикаль ячейки, которая ниже
    DOWN_PERS_DOWN = 1.0 - DOWN_PERS_ax1 - DOWN_PERS_ax2

    # то, сколько перетекает в вертикаль
    LR_PERS_DOWN = 1.0 - (LR_PERS_L + LR_PERS_R)

    for n in range(z):
        sh = np.shape(vertic)
        # типо жидкость капает
        vertic[0][sh[1] // 2][sh[2] // 2] = 1
        # print(vertic)
        # print(horizon_ax1)
        # копируем массивы
        ver = deepcopy(vertic)
        hor_ax1 = deepcopy(horizon_ax1)
        hor_ax2 = deepcopy(horizon_ax2)
        # условие на прохождение по оси ax0

        for ax0 in range(sh[0]):
            for ax1 in range(sh[1]):
                for ax2 in range(sh[2]):

                    # проход по вертикальным трубочкам
                    if vertic[ax0][ax1][ax2] > DOWN_MIN:
                        Sh = np.shape(ver)
                        if ax0 + 1 == Sh[0] - 1:
                            print("0")
                            app = np.array([[[0. for i in range(Sh[1])] for j in range(Sh[2])] for i in range(3)])
                            ver = np.append(ver, app, axis=0)
                            hor_ax1 = np.append(hor_ax1, app, axis=0)
                            hor_ax2 = np.append(hor_ax2, app, axis=0)
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
                        Sh_h1 = np.shape(ver)
                        if ax1 - 1 == 0 or ax1 + 1 == Sh_h1[1] - 1 or ax2 - 1 == 0 or ax2 + 1 == Sh_h1[2] - 1:
                            print('-1')
                            app1 = np.array([[[0. for i in range(Sh_h1[2])]] for j in range(Sh_h1[0])])
                            app2 = np.array([[[0. for i in range(Sh_h1[2])]] for j in range(Sh_h1[0])])
                            app = np.append(app1, app2, axis=1)
                            ver = np.append(app, ver, axis=1)
                            hor_ax1 = np.append(app, hor_ax1, axis=1)
                            hor_ax2 = np.append(app, hor_ax2, axis=1)

                            ver = np.append(ver, app, axis=1)
                            hor_ax1 = np.append(hor_ax1, app, axis=1)
                            hor_ax2 = np.append(hor_ax2, app, axis=1)
                            Sh_h2 = np.shape(ver)
                            app11 = np.array([[[0.] for i in range(Sh_h2[1])] for j in range(Sh_h2[0])])
                            app22 = np.array([[[0.] for i in range(Sh_h2[1])] for j in range(Sh_h2[0])])
                            app = np.append(app11, app22, axis=2)
                            ver = np.append(app, ver, axis=2)
                            hor_ax1 = np.append(app, hor_ax1, axis=2)
                            hor_ax2 = np.append(app, hor_ax2, axis=2)

                            ver = np.append(ver, app, axis=2)
                            hor_ax1 = np.append(hor_ax1, app, axis=2)
                            hor_ax2 = np.append(hor_ax2, app, axis=2)

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


def graph(result, ax2_incision):
    # окно для отрисовки графика
    fig_2d = plt.figure(figsize=(7, 7))
    ax_2d = fig_2d.add_subplot()
    ax_2d.set_title("разрез по оси ax2" + '\n' + "по координате " + str(ax2_incision))
    # отображение градиента
    ax_2d.imshow(result)
    plt.show()


def incision(v, h1, h2, ax0_max, ax1_max, ax2_incision):
    # ну а тут у нас по сути разрез берётся
    result = np.array([[0. for f in range(ax1_max)] for g in range(ax0_max)])
    for ax0 in range(ax0_max):
        for ax1 in range(ax1_max):
            result[ax0][ax1] = v[ax0][ax1][ax2_incision] + h1[ax0][ax1][ax2_incision] + h2[ax0][ax1][ax2_incision]
    return result


v, h1, h2= cycle(500)
sha = np.shape(v)
# вызов разреза
RES = incision(v, h1, h2, sha[0], sha[1], sha[2] // 2)
# вызов графика
graph(RES, sha[2] // 2)
