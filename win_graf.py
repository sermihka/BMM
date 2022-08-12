import tkinter as tk
import numpy as np
from tkinter import messagebox as mbox
import pipeline_3d_model

ax_incision = pipeline_3d_model.ax0_max // 2

# Массив слоёв( их коэффицентов и высоты их начала)
list_layer = np.array([[0. for i in range(9)]])
# Переменная от которой зависит какие значения мы подадим при старте
count_l_or_tr = 0

# массив для стандартной ситуации(один слой)
list = np.array([[0, 0.1, 0.4, 0.3, 0.3, 0.01, 0.3, 0.3, 0.3]])

list_slope = np.array([[0, 0.1, 0.4, 0.2, 0.2, 0.05, 0.3, 0.3, 0.3],
                       [1, 0.1, 0.6, 0.4, 0.4, 0.03, 0.4, 0.3, 0.3]])


def rem_value():
    """
    сохранение коэффицентов для одного слоя
    тоесть тут "стандартная ситуация" и только один однородный слой
    """
    global list
    D = entry_down_min.get()
    if D == '':
        return
    if float(D) < 0 or float(D) > 1:
        return
    else:
        Dp = entry_down_pers.get()
        if Dp == '':
            return
        if float(Dp) < 0 or float(Dp) > 1:
            return
        else:
            Dpax1 = entry_down_pers_ax1.get()
            if Dpax1 == '':
                return
            if float(Dpax1) < 0 or float(Dpax1) > 1:
                return
            else:
                Dpax2 = entry_down_pers_ax2.get()
                if Dpax2 == '':
                    return
                if float(Dpax2) < 0 or float(Dpax2) > 1:
                    return
                else:
                    LR = entry_lr_min.get()
                    if LR == '':
                        return
                    if float(LR) < 0 or float(LR) > 1:
                        return
                    else:
                        LRp = entry_lr_pers.get()
                        if LRp == '':
                            return
                        if float(LRp) < 0 or float(LRp) > 1:
                            return
                        else:
                            LRpl = entry_lr_pers_l.get()
                            if LRpl == '':
                                return
                            if float(LRpl) < 0 or float(LRpl) > 1:
                                return
                            else:
                                LRpr = entry_lr_pers_r.get()
                                if LRpr == '':
                                    return
                                if float(LRpr) < 0 or float(LRpr) > 1:
                                    return
                                else:
                                    if (1 - (float(Dpax1) + float(Dpax2))) < 0:
                                        return
                                    else:
                                        if (1 - (float(LRpr) + float(LRpl))) < 0:
                                            return
                                        else:
                                            list[0][1] = float(D)
                                            list[0][2] = float(Dp)
                                            list[0][3] = float(Dpax1)
                                            list[0][4] = float(Dpax2)
                                            list[0][5] = float(LR)
                                            list[0][6] = float(LRp)
                                            list[0][7] = float(LRpl)
                                            list[0][8] = float(LRpr)
                                            tk.Label(frame2, text=('Сохранено'), font=('Arial', 10), bg='#90EE90', relief=tk.RAISED, bd=5).place(x=250, y=55, width=250,height=50)

def incision():
    global ax_incision
    n = int(entry_incision.get())
    if (-pipeline_3d_model.ax0_max // 2) < n < (pipeline_3d_model.ax0_max // 2):
        ax_incision = (pipeline_3d_model.ax0_max // 2) + n





def save_layer(n):
    """
    Тут происходит сохранение коэфецентов для слоёв
    """
    global list_layer
    H = entry1_height.get()
    if H == '':
        return
    if int(H) < 0 or int(H) > pipeline_3d_model.ax0_max:
        return
    else:
        D = entry_down_min.get()
        if D == '':
            return
        if float(D) < 0 or float(D) > 1:
            return
        else:
            Dp = entry_down_pers.get()
            if Dp == '':
                return
            if float(Dp) < 0 or float(Dp) > 1:
                return
            else:
                Dpax1 = entry_down_pers_ax1.get()
                if Dpax1 == '':
                    return
                if float(Dpax1) < 0 or float(Dpax1) > 1:
                    return
                else:
                    Dpax2 = entry_down_pers_ax2.get()
                    if Dpax2 == '':
                        return
                    if float(Dpax2) < 0 or float(Dpax2) > 1:
                        return
                    else:
                        LR = entry_lr_min.get()
                        if LR == '':
                            return
                        if float(LR) < 0 or float(LR) > 1:
                            return
                        else:
                            LRp = entry_lr_pers.get()
                            if LRp == '':
                                return
                            if float(LRp) < 0 or float(LRp) > 1:
                                return
                            else:
                                LRpl = entry_lr_pers_l.get()
                                if LRpl == '':
                                    return
                                if float(LRpl) < 0 or float(LRpl) > 1:
                                    return
                                else:
                                    LRpr = entry_lr_pers_r.get()
                                    if LRpr == '':
                                        return
                                    if float(LRpr) < 0 or float(LRpr) > 1:
                                        return
                                    else:
                                        if (1 - (float(Dpax1) + float(Dpax2))) < 0:
                                            return
                                        else:
                                            if (1 - (float(LRpr) + float(LRpl))) < 0:
                                                return
                                            else:
                                                list_layer[n][0] = int(H)
                                                list_layer[n][1] = float(D)
                                                list_layer[n][2] = float(Dp)
                                                list_layer[n][3] = float(Dpax1)
                                                list_layer[n][4] = float(Dpax2)
                                                list_layer[n][5] = float(LR)
                                                list_layer[n][6] = float(LRp)
                                                list_layer[n][7] = float(LRpl)
                                                list_layer[n][8] = float(LRpr)
                                                if n == 0:
                                                    tk.Label(frame2, text='Сохранено', font=('Arial', 10), bg='#90EE90', relief=tk.RAISED, bd=5).place(x=220, y=160, width=270, height=50)
                                                if n == 1:
                                                    tk.Label(frame2, text='Сохранено', font=('Arial', 10), bg='#90EE90', relief=tk.RAISED, bd=5).place(x=220, y=215, width=270, height=50)
                                                if n == 2:
                                                    tk.Label(frame2, text=('Сохранено'),font=('Arial', 10), bg='#90EE90',relief=tk.RAISED, bd=5).place(x=220, y=270, width=270, height=50)
                                                if n == 3:
                                                    tk.Label(frame2, text=('Сохранено'),font=('Arial', 10), bg='#90EE90',relief=tk.RAISED, bd=5).place(x=220, y=325, width=270, height=50)
                                                if n == 4:
                                                    tk.Label(frame2, text=('Сохранено'),font=('Arial', 10), bg='#90EE90',relief=tk.RAISED, bd=5).place(x=220, y=380, width=270, height=50)


def save_slope(n):
    global list_slope

    D = entry_down_min.get()
    if D == '':
        return
    if float(D) < 0 or float(D) > 1:
        return
    else:
        Dp = entry_down_pers.get()
        if Dp == '':
            return
        if float(Dp) < 0 or float(Dp) > 1:
            return
        else:
            Dpax1 = entry_down_pers_ax1.get()
            if Dpax1 == '':
                return
            if float(Dpax1) < 0 or float(Dpax1) > 1:
                return
            else:
                Dpax2 = entry_down_pers_ax2.get()
                if Dpax2 == '':
                    return
                if float(Dpax2) < 0 or float(Dpax2) > 1:
                    return
                else:
                    LR = entry_lr_min.get()
                    if LR == '':
                        return
                    if float(LR) < 0 or float(LR) > 1:
                        return
                    else:
                        LRp = entry_lr_pers.get()
                        if LRp == '':
                            return
                        if float(LRp) < 0 or float(LRp) > 1:
                            return
                        else:
                            LRpl = entry_lr_pers_l.get()
                            if LRpl == '':
                                return
                            if float(LRpl) < 0 or float(LRpl) > 1:
                                return
                            else:
                                LRpr = entry_lr_pers_r.get()
                                if LRpr == '':
                                    return
                                if float(LRpr) < 0 or float(LRpr) > 1:
                                    return
                                else:
                                    if (1 - (float(Dpax1) + float(Dpax2))) < 0:
                                        return
                                    else:
                                        if (1 - (float(LRpr) + float(LRpl))) < 0:
                                            return
                                        else:
                                            list_slope[n][1] = float(D)
                                            list_slope[n][2] = float(Dp)
                                            list_slope[n][3] = float(Dpax1)
                                            list_slope[n][4] = float(Dpax2)
                                            list_slope[n][5] = float(LR)
                                            list_slope[n][6] = float(LRp)
                                            list_slope[n][7] = float(LRpl)
                                            list_slope[n][8] = float(LRpr)
                                            if n == 0:
                                                tk.Label(frame2, text=('Соъранено'), font=('Arial', 10), bg='#90EE90',relief=tk.RAISED, bd=5).place(x=0, y=110, width=250, height=50)
                                            if n == 1:
                                                 tk.Label(frame2, text=('Сохранено'), font=('Arial', 10), bg='#90EE90',relief=tk.RAISED, bd=5).place(x=260, y=110, width=250, height=50)

# переменная для смены кол-ва итераций
iteration_count = 500
#Компилятор находть тут ошибку при взаимодействие с кнопкой
#line 262, in Iter_change
#    if int(entry_iteration_count.get()) >= 0:
#ValueError: invalid literal for int() with base 10: ''
def Iter_change():
    global iteration_count
    global entry_iteration_count
    if int(entry_iteration_count.get()) >= 0:
        iteration_count = int(entry_iteration_count.get())

def start():
    global iteration_count
    if count_l_or_tr == 0:
        v, h1, h2 = pipeline_3d_model.cycle(iteration_count, list=list)
        RES = pipeline_3d_model.incision(v, h1, h2, ax2_incision=ax_incision)
        pipeline_3d_model.graph(RES, ax2_incision=ax_incision)
    if count_l_or_tr == 1:
        v, h1, h2 = pipeline_3d_model.cycle(iteration_count, list=list_layer)
        RES = pipeline_3d_model.incision(v, h1, h2, ax2_incision=ax_incision)
        pipeline_3d_model.graph(RES, ax2_incision=ax_incision)
    if count_l_or_tr == 2:
        v, h1, h2 = pipeline_3d_model.cycle(iteration_count, count=1, list=list_slope)
        RES = pipeline_3d_model.incision(v, h1, h2, ax2_incision=ax_incision)
        pipeline_3d_model.graph(RES, ax2_incision=ax_incision)


def situation_baze():
    global frame2
    global list
    global count_l_or_tr
    count_l_or_tr = 0
    list = np.array([[0, 0.1, 0.4, 0.3, 0.3, 0.01, 0.3, 0.3, 0.3]])

    frame2.destroy()
    save_baze ='Не сохранено'
    frame2 = tk.Frame(win, bg='#696969')
    frame2.place(relx=0.25, rely=0, relwidth=0.50, relheight=1)
    frame2.grid_columnconfigure(0, minsize=250)

    tk.Label(frame2, text='Один однородный слой', font=('Arial', 15),relief=tk.RAISED,bd=5,
             bg='#EEE8AA').place(x=0, y=0,width=500, height=50)

    tk.Button(frame2, text='Сохранить коэффиценты', font=('Arial', 15), command=rem_value,relief=tk.RAISED,bd=5).place(x=0, y=55,width=247, height=52)
    tk.Label(frame2, text=(save_baze), font=('Arial', 10), bg='#FA8072',relief=tk.RAISED,bd=5).place(x=250, y=55,width=250, height=50)
    tk.Button(frame2, text="start", font=('Arial', 15), command=start,relief=tk.RAISED,bd=5).place(x=0, y=110,width=500, height=50)


def situation_layer():
    global frame2
    global count_l_or_tr
    global list_layer
    list_layer = np.array([[0, 0.1, 0.4, 0.2, 0.2, 0.05, 0.3, 0.3, 0.3],
                           [5, 0.1, 0.6, 0.4, 0.4, 0.03, 0.4, 0.3, 0.3]])
    def layer__():
        """
        Тут сохраняется кол-во слоёв
        ( и проверяется что их не больше 5)
        """
        global list_layer
        if entry_layer.get() == '':
            return
        else:
            n = int(entry_layer.get())
            if n > 1 and n < 5:
                list_layer = np.array([[0. for i in range(9)]])
                for i in range(1, n):
                    list_layer = np.append(list_layer, [[0 for i in range(9)]], axis=0)
            print(list_layer)


    count_l_or_tr = 1
    frame2.destroy()
    frame2 = tk.Frame(win, bg='#696969')
    frame2.place(relx=0.25, rely=0, relwidth=0.50, relheight=1)
    frame2.grid_columnconfigure([0, 1, 2, 3, 4, 5], minsize=30)
    layer_save_1 = tk.Label(frame2, text=('Не сохранено'), font=('Arial', 10), bg='#FA8072',relief=tk.RAISED,bd=5)
    layer_save_1.place(x=220, y=160,width=270, height=50)
    layer_save_2 = tk.Label(frame2, text=('Не сохранено'), font=('Arial', 10), bg='#FA8072',relief=tk.RAISED,bd=5)
    layer_save_2.place(x=220, y=215,width=270, height=50)
    layer_save_3 = tk.Label(frame2, text=('Не сохранено'), font=('Arial', 10), bg='#FA8072',relief=tk.RAISED,bd=5)
    layer_save_3.place(x=220, y=270,width=270, height=50)
    layer_save_4 = tk.Label(frame2, text=('Не сохранено'), font=('Arial', 10), bg='#FA8072',relief=tk.RAISED,bd=5)
    layer_save_4.place(x=220, y=325,width=270, height=50)
    tk.Label(frame2, text='Несколько однородных слоёв ', font=('Arial', 15),relief=tk.RAISED,bd=5,bg='#EEE8AA').place(x=0, y=0,width=500, height=50)
    # разделение на два грунта
    tk.Label(frame2, text='Укажите количество' + '\n' + 'слоёв [2,4]', font=('Arial', 10, 'bold'), height=3,bd=5,relief=tk.RAISED, bg='#EEE8AA').place(x=0, y=55,width=200, height=50)
    entry_layer = tk.Entry(frame2, fg="black", bg="white",relief=tk.RAISED,bd=1)
    entry_layer.place(x=205, y=55,width=304, height=29)
    tk.Button(frame2, text='Сохранить', font=('Arial', 10),command=layer__).place(x=205, y=80,width=300, height=25)

    def list1():
        global list_layer
        sh_layer = np.shape(list_layer)
        n = 0
        if n < sh_layer[0]:
            save_layer(n)

    tk.Label(frame2, text='Перед тем как нажмете кномпку Сохранить слой' + '\n' + 'убедитесь в правильности коэфицентов',font=('Arial', 10, 'bold'),relief=tk.RAISED,bd=5).place(x=0, y=110,width=500, height=50)
    tk.Button(frame2, text='Сохранить слой 1', font=('Arial', 10), command=list1,relief=tk.RAISED,bd=5).place(x=10, y=160,width=200, height=50)
    def list2():
        global list_layer
        sh_layer = np.shape(list_layer)
        n = 1
        if n < sh_layer[0]:
            save_layer(n)

    tk.Button(frame2, text='Сохранить слой 2', font=('Arial', 10), command=list2,relief=tk.RAISED,bd=5).place(x=10, y=215,width=200, height=50)
    def list3():
        global list_layer
        sh_layer = np.shape(list_layer)
        n = 2
        if n < sh_layer[0]:
            save_layer(n)

    tk.Button(frame2, text='Сохранить слой 3', font=('Arial', 10), command=list3,relief=tk.RAISED,bd=5).place(x=10, y=270,width=200, height=50)
    def list4():
        global list_layer
        sh_layer = np.shape(list_layer)
        n = 3
        if n < sh_layer[0]:
            save_layer(n)

    tk.Button(frame2, text='Сохранить слой 4', font=('Arial', 10), command=list4,relief=tk.RAISED,bd=5).place(x=10, y=325,width=200, height=50)
    tk.Button(frame2, text="start", font=('Arial', 15), command=start,relief=tk.RAISED,bd=10).place(x=25, y=405,width=450, height=75)


def situation_slope():
    global frame2
    global count_l_or_tr
    global list_slope
    count_l_or_tr = 2
    list_slope = np.array([[0, 0.1, 0.4, 0.2, 0.2, 0.05, 0.3, 0.3, 0.3],
                           [1, 0.1, 0.6, 0.4, 0.4, 0.03, 0.4, 0.3, 0.3]])
    frame2.destroy()
    save_slope_1 ='Не сохранено '
    save_slope_2 ='Не сохранено '
    frame2 = tk.Frame(win, bg='#696969')
    frame2.place(relx=0.25, rely=0, relwidth=0.50, relheight=1)
    frame2.place(x=0, y=0,width=10, height=10)

    tk.Label(frame2, text='  Склон (два однородных слоя)  ', font=('Arial', 15),relief=tk.RAISED,bd=5,
             bg='#EEE8AA').place(x=0, y=0,width=510, height=50)

    def slope1():
        global list_slope
        save_slope(0)

    tk.Button(frame2, text='Верхний слой', font=('Arial', 15),relief=tk.RAISED,bd=5, command=slope1).place(x=0, y=55,width=250, height=50)
    tk.Label(frame2, text=(save_slope_1), font=('Arial', 10), bg='#FA8072', relief=tk.RAISED, bd=5).place(x=0, y=110,width=250,height=50)
    def slope2():
        global list_slope
        save_slope(1)

    tk.Button(frame2, text='Нижний слой', font=('Arial', 15),relief=tk.RAISED,bd=5, command=slope2).place(x=260, y=55,width=250, height=50)
    tk.Label(frame2, text=(save_slope_2), font=('Arial', 10), bg='#FA8072', relief=tk.RAISED, bd=5).place(x=260, y=110,width=250,height=50)
    tk.Button(frame2, text="запуск", font=('Arial', 15),relief=tk.RAISED, bd=5, command=start).place(x=0, y=165,width=510, height=50)

class Example(tk.Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Математическое моделирование процесса просачивания жидкости в пористые среды")
        # Создание простого меню
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = tk.Menu(menubar)
        # кнопки смены режима
        fileMenu.add_command(label="Стандартный режим", underline=0, command=situation_baze)
        fileMenu.add_command(label="Несколько слоёв", underline=0, command=situation_layer)
        fileMenu.add_command(label="Склон", underline=0, command=situation_slope)

        # Кнопка закрытия окна(ну и программы)
        fileMenu.add_command(label="Выход", underline=0, command=self.onExit)

        menubar.add_cascade(label="Режим", underline=0, menu=fileMenu)

    def onExit(self):
        self.quit()


win = tk.Tk()
win.geometry("1000x500")
win.resizable(False, False)

# стартовый фрейм
frame1 = tk.Frame(win, bg='gray')
frame1.place(relx=0, rely=0, relwidth=0.25, relheight=1)
frame1.grid_columnconfigure(0, minsize=125)
frame1.grid_rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], minsize=40)

tk.Label(frame1, text='Коэффиценты', font=('Arial', 10, 'bold'), height=3, relief=tk.RAISED, bd=5, bg='#EEE8AA').place(x=0, y=0, width=250, height=50)
var = 2
tk.Label(frame1, text='height:', relief=tk.GROOVE, bg='#EEE8AA').place(x=0, y=55, width=120, height=30)
entry1_height = tk.Entry(frame1, fg="green", bg="white")
entry1_height.place(x=125, y=55, width=120, height=30)

# минимально количество жидкости в трубочке по вертикали после которого вода течёт
tk.Label(frame1, text='DOWN_MIN:', relief=tk.GROOVE, bg='#EEE8AA').place(x=0, y=90, width=120, height=30)
entry_down_min = tk.Entry(frame1, fg="green", bg="white")
entry_down_min.place(x=125, y=90, width=120, height=30)

# доля от объёма воды, который утекает
tk.Label(frame1, text='DOWN_PERC:', relief=tk.GROOVE, bg='#EEE8AA').place(x=0, y=125, width=120, height=30)
entry_down_pers = tk.Entry(frame1, fg="green", bg="white")
entry_down_pers.place(x=125, y=125, width=120, height=30)

# доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax1
tk.Label(frame1, text='DOWN_PERC_ax1:', relief=tk.GROOVE, bg='#EEE8AA').place(x=0, y=160, width=120, height=30)
entry_down_pers_ax1 = tk.Entry(frame1, fg="green", bg="white")
entry_down_pers_ax1.place(x=125, y=160, width=120, height=30)

# доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax2
tk.Label(frame1, text='DOWN_PERC_ax2:', relief=tk.GROOVE, bg='#EEE8AA').place(x=0, y=195, width=120, height=30)
entry_down_pers_ax2 = tk.Entry(frame1, fg="green", bg="white")
entry_down_pers_ax2.place(x=125, y=195, width=120, height=30)

# минимальноеколичество по горизонтали для вытекания
tk.Label(frame1, text='LR_MIN:', relief=tk.GROOVE, bg='#EEE8AA').place(x=0, y=230, width=120, height=30)
entry_lr_min = tk.Entry(frame1, fg="green", bg="white")
entry_lr_min.place(x=125, y=230, width=120, height=30)

# Сколько вытекает в общем по горизонтали
tk.Label(frame1, text='LR_PERC:', relief=tk.GROOVE, bg='#EEE8AA').place(x=0, y=265, width=120, height=30)
entry_lr_pers = tk.Entry(frame1, fg="green", bg="white")
entry_lr_pers.place(x=125, y=265, width=120, height=30)

# то, сколько перетекает влево
tk.Label(frame1, text='LR_PERC_L:', relief=tk.GROOVE, bg='#EEE8AA').place(x=0, y=300, width=120, height=30)
entry_lr_pers_l = tk.Entry(frame1, fg="green", bg="white")
entry_lr_pers_l.place(x=125, y=300, width=120, height=30)

# то, сколько перетекает вправо
tk.Label(frame1, text='LR_PERC_R:', relief=tk.GROOVE, bg='#EEE8AA').place(x=0, y=335, width=120, height=30)
entry_lr_pers_r = tk.Entry(frame1, fg="green", bg="white")
entry_lr_pers_r.place(x=125, y=335, width=120, height=30)

# фрейм сохранения значений
frame2 = tk.Frame(win, bg='#696969')
frame2.place(relx=0.25, rely=0, relwidth=0.50, relheight=1)
frame2.grid_columnconfigure(0, minsize=250)

an = tk.Label(frame2, text='  Выберете режим! ', font=('Arial', 15),relief=tk.RAISED,bd=5,bg='#EEE8AA').place(x=0, y=0,width=500, height=50)

# фрейм с кнопками взятия разреза, старта и справки по проге
frame3 = tk.Frame(win, bg='#5E5E5E')
frame3.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)
# разрез
tk.Label(frame3, text=('Укажите номер' + '\n' + 'разреза'), font=('Arial', 10, 'bold'), height=3, relief=tk.RAISED, bd=5, bg='#EEE8AA').place(x=0, y=0, width=250, height=50)
entry_incision = tk.Entry(frame3, fg="green", bg="white", relief=tk.RAISED, bd=5)
# размещение надо прописывать отдельно, иначе не будет работать
entry_incision.place(x=5, y=50, width=240, height=30)
tk.Button(frame3, text='Сохранить номер', command=incision, font=('Arial', 10),activebackground = '#90EE90',bg = 'white' , relief=tk.RAISED, bd=5).place(x=35, y=80, width=180, height=50)

tk.Label(frame3, text="Укажите количество итераций", font=('Arial', 10), height=3, relief=tk.RAISED, bd=5, bg='#EEE8AA').place(x=0, y=135, width=250, height=50)
entry_iteration_count = tk.Entry(frame3, fg="green", bg="white", relief=tk.RAISED, bd=5)
entry_iteration_count.place(x=5, y=185, width=240, height=30)
tk.Button(frame3, text="Сохранить итерацию", command=Iter_change,activebackground = '#90EE90',bg = 'white' ,font=('Arial', 10), relief=tk.RAISED, bd=5).place(x=35, y=215, width=180, height=50)


text_s = '''Эта программа показывает, как распространяется жидкость \n
в той или иной почве. Ваша задача ввести свои коэффициенты и нажать пару кнопок, \n
а затем вы увидите результат в заданном срезе. \n
Описание коэффициентов: \n
height - высота, с которой начинается слой почвы (имейте в виду, что в этой программе отсчёт идёт \n
сверху вниз, то есть чем ниже уровень почвы, тем "номер ячейки" по вертикали больше) \n
DOWN_MIN - минимальное количество жидкости в трубочке по вертикали, необходимое для растекания воды \n
DOWN_PERS - доля утекающей воды от общего объёма воды в трубочке \n
DOWN_PERS_ax1 - доля утекающей жидкости (от DOWN_PERS), которая остаётся в этой ячейке, но переходит в горизонталь ax1 \n
DOWN_PERS_ax2 - доля утекающей жидкости (от DOWN_PERS), которая остаётся в этой ячейке, но переходит в горизонталь ax2 \n
LR_MIN - минимальное количество жидкости в трубочке по горизонтали, необходимое для вытекания из неё жидкости \n
LR_PERS - доля всей жидкости, которая вытекает по горизонтали \n
LR_PERS_L - доля жидкости (от LR_PERS), которая перетекает в левый бок по горизонтальной оси \n
LR_PERS_R - доля жидкости (от LR_PERS), которая перетекает в правый бок по горизонтальной оси \n
Нажав на кнопку "Режим"*, вы можете выбрать такие пункты как: \n
- Стандартный режим. У вас будет только один однородный слой, для которого \n
вы сможете устанавливать свои коэффиценты. \n
- Несколько слоёв. Вы можете ввести несколько слоёв (от 2х до 5ти), определить коэффиценты для каждого, \n
а также указать высоту, на которой они начинаются. Чтобы сохранить коэффиценты, нажмите \n
на кнопку с номером нужного вам слоя. \n
- Склон. Здесь только два слоя, и разделение между ними происходит по диагонали. \n
*) У всех режимов есть кнопка запуска, после нажатия на которую запустится \n
модель растекания. Однако, если вы не заполните все коэффиценты, то программа \n
не выдаст вам правильно отработанный результат. Поэтому заполняйте всё и проверяйте, \n
что вы ничего не забыли. \n
Также вы можете указать номер разреза. Изначально взят разрез посередине стороны \n 
"кубика" почвы (axis 2). Поэтому вы можете указывать отрицательные числа, чтобы уйти влево, \n 
и положительные, чтобы уйти вправо (увеличить/уменьшить номер разреза).'''

def onInfo():
    global text_s
    mbox.showinfo("Информация", text_s)
tk.Button(frame3, text='Справка', command=onInfo, font=('Arial', 10)).place(x=95, y=450,width=150, height=45)


app = Example()
win.mainloop()