"""
Окно три столбца, первый столбец выбрать жидкость , пока что только вода, второй столбец выбор почвы ,
пока что только песок , последний столбец кнопка старт (начало)
"""
import tkinter as tk
import pipeline_3d_model
#import numpy as np
#from copy import deepcopy
#import time
choice_soil = 'soil'
choice_liquid = 'liquid'
ax_incision = pipeline_3d_model.ax0_max // 2
D_M = 0.1
D_P = 0.4
D_P_ax1 = 0.3
D_P_ax2 = 0.3

LR_M = 0.01
LR_P = 0.3
LR_P_L = 0.3
LR_P_R = 0.3


def rem_value():
    global choice_liquid
    global choice_soil

    global D_M
    global D_P
    global D_P_ax1
    global D_P_ax2

    global LR_P
    global LR_M
    global LR_P_R
    global LR_P_L


    D = entry_down_min.get()
    if D == '':
        return
    if float(D) < 0 or float(D) > 1:
        return
    else:
        D_M = float(D)

    Dp = entry_down_pers.get()
    if Dp == '':
        return
    if float(Dp) < 0 or float(Dp) > 1:
        return
    else:
        D_P = float(Dp)

    Dpax1 = entry_down_pers_ax1.get()
    if Dpax1 == '':
        return
    if float(Dpax1) < 0 or float(Dpax1) > 1:
        return
    else:
        D_P_ax1 = float(Dpax1)

    Dpax2 = entry_down_pers_ax2.get()
    if Dpax2 == '':
        return
    if float(Dpax2) < 0 or float(Dpax2) > 1:
        return
    else:
        D_P_ax2 = float(Dpax2)

    LR = entry_lr_min.get()
    if LR == '':
        return
    if float(LR) < 0 or float(LR) > 1:
        return
    else:
        LR_M = float(LR)

    LRp = entry_lr_pers.get()
    if LRp == '':
        return
    if float(LRp) < 0 or float(LRp) > 1:
        return
    else:
        LR_P = float(LRp)

    LRpl = entry_lr_pers_l.get()
    if LRpl == '':
        return
    if float(LRpl) < 0 or float(LRpl) > 1:
        return
    else:
        LR_P_L = float(LRpl)

    LRpr = entry_lr_pers_r.get()
    if LRpr == '':
        return
    if float(LRpr) < 0 or float(LRpr) > 1:
        return
    else:
        LR_P_R = float(LRpr)
    choice_liquid = 'liquid'
    choice_soil = 'soil'


def incision():
    global ax_incision
    n = int(entry_incision.get())
    if (-pipeline_3d_model.ax0_max // 2) < n < (pipeline_3d_model.ax0_max // 2):
        ax_incision = (pipeline_3d_model.ax0_max // 2) + n


def separation():
    pass





def start():
    global choice_liquid
    global choice_soil


    if choice_soil == 'soil' and choice_liquid == 'liquid':
        v, h1, h2 = pipeline_3d_model.cycle(400, D_M, D_P, D_P_ax1, D_P_ax2, LR_M, LR_P, LR_P_L, LR_P_R)
        RES = pipeline_3d_model.incision(v, h1, h2, ax2_incision=ax_incision)
        pipeline_3d_model.graph(RES, ax2_incision=ax_incision)



win = tk.Tk()

# интерфейс окна
win.title('Математическое моделирование процесса просачивания жидкости в пористые среды')

# размеры
win.geometry("1000x500")
"""win.minsize(300, 400)
win.maxsize(700, 800)"""

# запрет на именения размера окна
win.resizable(False, False)


# стартовый фрейм
frame1 = tk.Frame(win, bg='gray')
frame1.place(relx=0, rely=0, relwidth=0.25, relheight=1)
frame1.grid_columnconfigure(0, minsize=250)
# виджеты стартового фрейма

# кнопка, для введения своих значений
tk.Button(frame1, text='Нажмите, чтобы ввести' + '\n' + 'свои коэффиценты [0;1]', command=rem_value, font=('Arial', 10)).grid(row=1, column=0, stick='we')


# минимально количество жидкости в трубочке по вертикали после которого вода течёт
tk.Label(frame1, text='DOWN_MIN', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry_down_min = tk.Entry(frame1, fg="green", bg="white")
entry_down_min.grid(stick='we')

# доля от объёма воды, который утекает
tk.Label(frame1, text='DOWN_PERC', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry_down_pers = tk.Entry(frame1, fg="green", bg="white")
entry_down_pers.grid(stick='we')

# доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax1
tk.Label(frame1, text='DOWN_PERC_ax1', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry_down_pers_ax1 = tk.Entry(frame1, fg="green", bg="white")
entry_down_pers_ax1 .grid(stick='we')

# доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax2
tk.Label(frame1, text='DOWN_PERC_ax2', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry_down_pers_ax2 = tk.Entry(frame1, fg="green", bg="white")
entry_down_pers_ax2.grid(stick='we')

# минимальноеколичество по горизонтали для вытекания
tk.Label(frame1, text='LR_MIN', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry_lr_min = tk.Entry(frame1, fg="green", bg="white")
entry_lr_min.grid(stick='we')

# Сколько вытекает в общем по горизонтали
tk.Label(frame1, text='LR_PERC', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry_lr_pers = tk.Entry(frame1, fg="green", bg="white")
entry_lr_pers.grid(stick='we')

# то, сколько перетекает влево
tk.Label(frame1, text='LR_PERC_L', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry_lr_pers_l = tk.Entry(frame1, fg="green", bg="white")
entry_lr_pers_l.grid(stick='we')

# то, сколько перетекает вправо
tk.Label(frame1, text='LR_PERC_R', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry_lr_pers_r = tk.Entry(frame1, fg="green", bg="white")
entry_lr_pers_r.grid(stick='we')

tk.Label(frame1, text='Нажмите старт для вывода', font=('Arial', 10, 'bold'), height=2, relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
# кнопка старта
tk.Button(frame1, text='Старт', command=start, font=('Arial', 10), width=10, height=3).grid()


# фрейм с изменяемыми значениями
frame2 = tk.Frame(win, bg='black')
frame2.place(relx=0.25, rely=0, relwidth=0.25, relheight=1)
frame2.grid_columnconfigure(0, minsize=250)
# виджеты

# разрез
tk.Label(frame2, text=('Укажите номер' + '\n' + 'разреза'), font=('Arial', 10, 'bold'), height=3, relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry_incision = tk.Entry(frame2, fg="green", bg="white")
# размещение надо прописывать отдельно, иначе не будет работать
entry_incision.grid(stick='we')
tk.Button(frame2, text='сохранить номер', command=incision, font=('Arial', 10)).grid(stick='we')


# разделение на два грунта
tk.Label(frame2, text='Укажите уровень' + '\n' + 'разделения', font=('Arial', 10, 'bold'), height=3, relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry_separation = tk.Entry(frame2, fg="green", bg="white")
entry_separation.grid(stick='we')
tk.Button(frame2, text='сохранить уровень', font=('Arial', 10), command=separation()).grid(stick='we')

"""
!!!!!!!!! третий фрейм, коэффиценты для второго слоя !!!!!
"""
frame3 = tk.Frame(win, bg='gray')
frame3.place(relx=0.50, rely=0, relwidth=0.25, relheight=1)
frame3.grid_columnconfigure(0, minsize=250)
# виджеты

# кнопка, для введения значений 2 слоя
tk.Button(frame3, text='Нажмите, чтобы ввести' + '\n' + 'коэффиценты 2 слоя', command=rem_value, font=('Arial', 10)).grid(row=1, column=0, stick='we')


# минимально количество жидкости в трубочке по вертикали после которого вода течёт
tk.Label(frame3, text='DOWN_MIN', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry1_down_min = tk.Entry(frame3, fg="green", bg="white")
entry1_down_min.grid(stick='we')

# доля от объёма воды, который утекает
tk.Label(frame3, text='DOWN_PERC', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry1_down_pers = tk.Entry(frame3, fg="green", bg="white")
entry1_down_pers.grid(stick='we')

# доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax1
tk.Label(frame3, text='DOWN_PERC_ax1', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry1_down_pers_ax1 = tk.Entry(frame3, fg="green", bg="white")
entry1_down_pers_ax1 .grid(stick='we')

# доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax2
tk.Label(frame3, text='DOWN_PERC_ax2', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry1_down_pers_ax2 = tk.Entry(frame3, fg="green", bg="white")
entry1_down_pers_ax2.grid(stick='we')

# минимальноеколичество по горизонтали для вытекания
tk.Label(frame3, text='LR_MIN', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry1_lr_min = tk.Entry(frame3, fg="green", bg="white")
entry1_lr_min.grid(stick='we')

# Сколько вытекает в общем по горизонтали
tk.Label(frame3, text='LR_PERC', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry1_lr_pers = tk.Entry(frame3, fg="green", bg="white")
entry1_lr_pers.grid(stick='we')

# то, сколько перетекает влево
tk.Label(frame3, text='LR_PERC_L', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry1_lr_pers_l = tk.Entry(frame3, fg="green", bg="white")
entry1_lr_pers_l.grid(stick='we')

# то, сколько перетекает вправо
tk.Label(frame3, text='LR_PERC_R', relief=tk.GROOVE, bg='#2F4F4F').grid(stick='we')
entry1_lr_pers_r = tk.Entry(frame3, fg="green", bg="white")
entry1_lr_pers_r.grid(stick='we')




win.mainloop()
