from copy import copy, deepcopy
import matplotlib.pyplot as plt

fig_2d = plt.figure(figsize=(7, 7))
ax_2d = fig_2d.add_subplot()

IMAX = 75
JMAX = 70
STEPS_MAX = 500

horiz = [[0] * (IMAX + 1) for j in range(JMAX)]
horiz_new = horiz

#print(horiz)
vert = [[0] * (JMAX + 1) for i in range(IMAX)]
vert_new = deepcopy(vert)

vert[IMAX // 2][0] = 1

#print(vert, vert_new, id(vert), id(vert_new))

TUBE_MAX = 1.0
DOWN_MIN = 0.1
DOWN_PERS = 0.3
DOWN_PERS_LEFT = 0.3
DOWN_PERS_RIGHT = 0.3
DOWN_PERS_DOWN = 1.0 - DOWN_PERS_LEFT - DOWN_PERS_RIGHT

LR_MIN = 0.01
LR_PERS = 0.3
LR_PERS_LR = 0.4
LR_PERS_DOWN = 1.0 - LR_PERS_LR

# for i in range(IMAX):
#    for j in range(JMAX):

for step in range(STEPS_MAX):
    #print("Шаг: ", step)
    vert[IMAX // 2][0] = 1

    horiz_new = deepcopy(horiz)
    vert_new = deepcopy(vert)

    for i in range(IMAX):
        for j in range(JMAX):
            # print("Стекание из вертикальной: ", i, ":", j)
            if (vert[i][j] > DOWN_MIN):
                # print("Стекание из вертикальной: ", i, ":", j, " = ", vert[i][j])

                down = vert[i][j] * DOWN_PERS
                down_mmleft = down * DOWN_PERS_LEFT
                down_mmright = down * DOWN_PERS_RIGHT
                down_mmdown = down * DOWN_PERS_DOWN

                tube_max_left = (TUBE_MAX - horiz_new[j][i]) / 2.0
                tube_max_right = (TUBE_MAX - horiz_new[j][i + 1]) / 2.0
                tube_max_down = (TUBE_MAX - vert_new[i][j + 1]) / 2.0

                if (down_mmleft > tube_max_left):
                    down_mmleft = tube_max_left
                if (down_mmright > tube_max_right):
                    down_mmright = tube_max_right
                if (down_mmdown > tube_max_down):
                    down_mmdown = tube_max_down

                down_stay = down - (down_mmleft + down_mmright + down_mmdown)

                vert_new[i][j] = vert_new[i][j] - down + down_stay
                horiz_new[j][i] = horiz_new[j][i] + down_mmleft
                horiz_new[j][i + 1] = horiz_new[j][i + 1] + down_mmright
                vert_new[i][j + 1] = vert_new[i][j + 1] + down_mmdown

            if (horiz[j][i] > LR_MIN):
                # print("Перетекание вправо: ", i, ":", j, " = ", horiz[j][i])

                right = horiz[j][i] * LR_PERS
                right_mmright = right * LR_PERS_LR
                right_mmdown = right * LR_PERS_DOWN

                tube_max_right = (TUBE_MAX - horiz_new[j][i + 1]) / 2.0
                tube_max_down = (TUBE_MAX - vert_new[i][j + 1]) / 2.0

                if (right_mmright > tube_max_right):
                    right_mmright = tube_max_right
                if (right_mmdown > tube_max_down):
                    right_mmdown = tube_max_down

                right_stay = right - (right_mmright + right_mmdown)

                horiz_new[j][i] = horiz_new[j][i] - right + right_stay
                horiz_new[j][i + 1] = horiz_new[j][i + 1] + right_mmright
                vert_new[i][j] = vert_new[i][j] + right_mmdown

            if (horiz[j][i + 1] > LR_MIN):
                # print("Перетекание влево: ", i, ":", j, " = ", horiz[j][i + 1])

                left = horiz[j][i + 1] * LR_PERS
                left_mmleft = left * LR_PERS_LR
                left_mmdown = left * LR_PERS_DOWN

                tube_max_left = (TUBE_MAX - horiz_new[j][i]) / 2.0
                tube_max_down = (TUBE_MAX - vert_new[i][j]) / 2.0

                if (left_mmleft > tube_max_left):
                    left_mmleft = tube_max_left
                if (left_mmdown > tube_max_down):
                    left_mmdown = tube_max_down

                left_stay = left - (left_mmleft + left_mmdown)

                horiz_new[j][i + 1] = horiz_new[j][i + 1] - left + left_stay
                horiz_new[j][i] = horiz_new[j][i] + left_mmleft
                vert_new[i][j] = vert_new[i][j] + left_mmdown

            # print("Подъем из вертикальной: ", i, ":", j + 1)
            # print("Перетекание вправо: ", i, ":", j)
            # print("Перетекание влево: ", i + 1, ":", j)
    horiz = deepcopy(horiz_new)
    vert = deepcopy(vert_new)

#print(vert_new)

PROB = [[0] * (IMAX) for j in range(JMAX)]
for i in range(IMAX):
    for j in range(JMAX):
        PROB[j][i] = (vert[i][j] + vert[i][j + 1] + horiz[j][i] + horiz[j][i + 1]) / 4.0
for k in range(len(PROB)):
    print(PROB[k])

ax_2d.imshow(PROB)
plt.show()

