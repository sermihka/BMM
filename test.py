import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt

# окно для отрисовки графика
fig_2d = plt.figure(figsize=(7, 7))
frames_2d = []

ax_2d = fig_2d.add_subplot()

# размеры массива
x = 70
y = 70
# массив трубочек по горизонтали
h_capacity_1 = np.array([[0. for n in range(y+1)] for m in range(x+1)])
# массив трубочек по вертикали
v_capacity_1 = np.array([[0. for i in range(y+1)] for j in range(x+1)])

v_capacity_1[x//2][0] = 1

# максимально возможное значение в трубочке
TUBE_MAX = 1.0
# минимально количество жидкости в трубочке
# по вертикали после которого вода течёт
DOWN_MIN = 0.1
# процент от объёма воды, который утекает
DOWN_PERS = 0.3
# процент который остаётся в этой ячейке, но переходит в горизонталь
DOWN_PERS_LEFT = 0.3
# процент который переходит в горизонталь ячейки, которая ниже нынешней
DOWN_PERS_RIGHT = 0.3
# процент который переходит в вертикаль ячейки, которая ниже
DOWN_PERS_DOWN = 1.0 - DOWN_PERS_LEFT - DOWN_PERS_RIGHT

LR_MIN = 0.01
LR_PERS = 0.3
LR_PERS_LR = 0.4
LR_PERS_DOWN = 1.0 - LR_PERS_LR

for n in range(500):
    v_capacity_1[x//2][0] = 1
    #глубокое копирование массивов
    h_capacity_2 = deepcopy(h_capacity_1)
    v_capacity_2 = deepcopy(v_capacity_1)

    for i in range(x):
        for j in range(y):
            # правила стекания по вертикали
            if v_capacity_1[i][j] > DOWN_MIN:

                # то, сколько вытекает
                down = v_capacity_1[i][j] * DOWN_PERS
                # то, сколько переходит в горизонталь
                down_mmleft = down * DOWN_PERS_LEFT
                # то сколько переходит в горизонталь
                down_mmright = down * DOWN_PERS_RIGHT
                # то, сколько переходит в вертикаль ячейки ниже
                down_mmdown = down * DOWN_PERS_DOWN

                # то, сколько может втечь в нужную трубочку
                tube_max_left = (TUBE_MAX - h_capacity_2[j][i]) / 2.0
                tube_max_right = (TUBE_MAX - h_capacity_2[j][i + 1]) / 2.0
                tube_max_down = (TUBE_MAX - v_capacity_2[i][j + 1]) / 2.0

                # проверка на то, что то что туда собирается втечь,
                # сможет это сделать
                if (down_mmleft > tube_max_left):
                    down_mmleft = tube_max_left
                if (down_mmright > tube_max_right):
                    down_mmright = tube_max_right
                if (down_mmdown > tube_max_down):
                    down_mmdown = tube_max_down

                # то что в итоге останетсяв ячейки
                down_stay = down - (down_mmleft + down_mmright + down_mmdown)

                # присваивание итоговых результатов в массивы
                v_capacity_2[i][j] = v_capacity_2[i][j] - down + down_stay
                h_capacity_2[j][i] = h_capacity_2[j][i] + down_mmleft
                h_capacity_2[j][i + 1] = h_capacity_2[j][i + 1] + down_mmright
                v_capacity_2[i][j + 1] = v_capacity_2[i][j + 1] + down_mmdown

            if (h_capacity_1[j][i] > LR_MIN):
                # print("Перетекание вправо: ", i, ":", j, " = ", horiz[j][i])

                right = h_capacity_1[j][i] * LR_PERS
                right_mmright = right * LR_PERS_LR
                right_mmdown = right * LR_PERS_DOWN

                tube_max_right = (TUBE_MAX - h_capacity_2[j][i + 1]) / 2.0
                tube_max_down = (TUBE_MAX - v_capacity_2[i][j + 1]) / 2.0

                if (right_mmright > tube_max_right):
                    right_mmright = tube_max_right
                if (right_mmdown > tube_max_down):
                    right_mmdown = tube_max_down

                right_stay = right - (right_mmright + right_mmdown)

                h_capacity_2[j][i] = h_capacity_2[j][i] - right + right_stay
                h_capacity_2[j][i + 1] = h_capacity_2[j][i + 1] + right_mmright
                v_capacity_2[i][j] = v_capacity_2[i][j] + right_mmdown

            if (h_capacity_1[j][i + 1] > LR_MIN):
                # print("Перетекание влево: ", i, ":", j, " = ", horiz[j][i + 1])

                left = h_capacity_1[j][i + 1] * LR_PERS
                left_mmleft = left * LR_PERS_LR
                left_mmdown = left * LR_PERS_DOWN

                tube_max_left = (TUBE_MAX - h_capacity_2[j][i]) / 2.0
                tube_max_down = (TUBE_MAX - v_capacity_2[i][j]) / 2.0

                if (left_mmleft > tube_max_left):
                    left_mmleft = tube_max_left
                if (left_mmdown > tube_max_down):
                    left_mmdown = tube_max_down

                left_stay = left - (left_mmleft + left_mmdown)

                h_capacity_2[j][i + 1] = h_capacity_2[j][i + 1] - left + left_stay
                h_capacity_2[j][i] = h_capacity_2[j][i] + left_mmleft
                v_capacity_2[i][j] = v_capacity_2[i][j] + left_mmdown


    h_capacity_1 = deepcopy(h_capacity_2)
    v_capacity_1 = deepcopy(v_capacity_2)

PROB = [[0] * (x) for j in range(y)]
for i in range(x):
    for j in range(y):
        PROB[j][i] = (v_capacity_1[i][j] + v_capacity_1[i][j + 1] + h_capacity_1[j][i] + h_capacity_1[j][i + 1]) / 4.0
for k in range(len(PROB)):
    print(PROB[k])

ax_2d.imshow(PROB)
plt.show()


