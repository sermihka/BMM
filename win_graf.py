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

list_slope = np.array([[0, 0., 0., 0., 0., 0.0, 0., 0., 0.],
                       [1, 0., 0., 0., 0., 0.0, 0., 0., 0.]])


def rem_value():
    """
    сохранение коэффицентов для одного слоя
    тоесть тут "стандартная ситуация" и только один однородный слой
    """

    D = entry_down_min.get()
    if D == '':
        return
    if float(D) < 0 or float(D) > 1:
        return
    else:
        list[0][1] = float(D)

    Dp = entry_down_pers.get()
    if Dp == '':
        return
    if float(Dp) < 0 or float(Dp) > 1:
        return
    else:
        list[0][2] = float(Dp)

    Dpax1 = entry_down_pers_ax1.get()
    if Dpax1 == '':
        return
    if float(Dpax1) < 0 or float(Dpax1) > 1:
        return
    else:
        list[0][3] = float(Dpax1)

    Dpax2 = entry_down_pers_ax2.get()
    if Dpax2 == '':
        return
    if float(Dpax2) < 0 or float(Dpax2) > 1:
        return
    else:
        list[0][4] = float(Dpax2)

    LR = entry_lr_min.get()
    if LR == '':
        return
    if float(LR) < 0 or float(LR) > 1:
        return
    else:
        list[0][5] = float(LR)

    LRp = entry_lr_pers.get()
    if LRp == '':
        return
    if float(LRp) < 0 or float(LRp) > 1:
        return
    else:
        list[0][6] = float(LRp)

    LRpl = entry_lr_pers_l.get()
    if LRpl == '':
        return
    if float(LRpl) < 0 or float(LRpl) > 1:
        return
    else:
        list[0][7] = float(LRpl)

    LRpr = entry_lr_pers_r.get()
    if LRpr == '':
        return
    if float(LRpr) < 0 or float(LRpr) > 1:
        return
    else:
        list[0][8] = float(LRpr)


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
        list_layer[n][0] = int(H)

    D = entry_down_min.get()
    if D == '':
        return
    if float(D) < 0 or float(D) > 1:
        return
    else:
        list_layer[n][1] = float(D)

    Dp = entry_down_pers.get()
    if Dp == '':
        return
    if float(Dp) < 0 or float(Dp) > 1:
        return
    else:
        list_layer[n][2] = float(Dp)

    Dpax1 = entry_down_pers_ax1.get()
    if Dpax1 == '':
        return
    if float(Dpax1) < 0 or float(Dpax1) > 1:
        return
    else:
        list_layer[n][3] = float(Dpax1)

    Dpax2 = entry_down_pers_ax2.get()
    if Dpax2 == '':
        return
    if float(Dpax2) < 0 or float(Dpax2) > 1:
        return
    else:
        list_layer[n][4] = float(Dpax2)

    LR = entry_lr_min.get()
    if LR == '':
        return
    if float(LR) < 0 or float(LR) > 1:
        return
    else:
        list_layer[n][5] = float(LR)

    LRp = entry_lr_pers.get()
    if LRp == '':
        return
    if float(LRp) < 0 or float(LRp) > 1:
        return
    else:
        list_layer[n][6] = float(LRp)

    LRpl = entry_lr_pers_l.get()
    if LRpl == '':
        return
    if float(LRpl) < 0 or float(LRpl) > 1:
        return
    else:
        list_layer[n][7] = float(LRpl)

    LRpr = entry_lr_pers_r.get()
    if LRpr == '':
        return
    if float(LRpr) < 0 or float(LRpr) > 1:
        return
    else:
        list_layer[n][8] = float(LRpr)


def save_slope(n):
    global list_slope

    D = entry_down_min.get()
    if D == '':
        return
    if float(D) < 0 or float(D) > 1:
        return
    else:
        list_slope[n][1] = float(D)

    Dp = entry_down_pers.get()
    if Dp == '':
        return
    if float(Dp) < 0 or float(Dp) > 1:
        return
    else:
        list_slope[n][2] = float(Dp)

    Dpax1 = entry_down_pers_ax1.get()
    if Dpax1 == '':
        return
    if float(Dpax1) < 0 or float(Dpax1) > 1:
        return
    else:
        list_slope[n][3] = float(Dpax1)

    Dpax2 = entry_down_pers_ax2.get()
    if Dpax2 == '':
        return
    if float(Dpax2) < 0 or float(Dpax2) > 1:
        return
    else:
        list_slope[n][4] = float(Dpax2)

    LR = entry_lr_min.get()
    if LR == '':
        return
    if float(LR) < 0 or float(LR) > 1:
        return
    else:
        list_slope[n][5] = float(LR)

    LRp = entry_lr_pers.get()
    if LRp == '':
        return
    if float(LRp) < 0 or float(LRp) > 1:
        return
    else:
        list_slope[n][6] = float(LRp)

    LRpl = entry_lr_pers_l.get()
    if LRpl == '':
        return
    if float(LRpl) < 0 or float(LRpl) > 1:
        return
    else:
        list_slope[n][7] = float(LRpl)

    LRpr = entry_lr_pers_r.get()
    if LRpr == '':
        return
    if float(LRpr) < 0 or float(LRpr) > 1:
        return
    else:
        list_slope[n][8] = float(LRpr)


def start():
    if count_l_or_tr == 0:
        v, h1, h2 = pipeline_3d_model.cycle(500, list=list)
        RES = pipeline_3d_model.incision(v, h1, h2, ax2_incision=ax_incision)
        pipeline_3d_model.graph(RES, ax2_incision=ax_incision)
    if count_l_or_tr == 1:
        v, h1, h2 = pipeline_3d_model.cycle(1000, list=list_layer)
        RES = pipeline_3d_model.incision(v, h1, h2, ax2_incision=ax_incision)
        pipeline_3d_model.graph(RES, ax2_incision=ax_incision)
    if count_l_or_tr == 2:
        v, h1, h2 = pipeline_3d_model.cycle(1500, count=1, list=list_slope)
        RES = pipeline_3d_model.incision(v, h1, h2, ax2_incision=ax_incision)
        pipeline_3d_model.graph(RES, ax2_incision=ax_incision)


def situation_baze():
    global frame2
    global count_l_or_tr
    count_l_or_tr = 0
    frame2.destroy()

    frame2 = tk.Frame(win, bg='black')
    frame2.place(relx=0.25, rely=0, relwidth=0.50, relheight=1)
    frame2.grid_columnconfigure(0, minsize=250)

    tk.Label(frame2, text='__Один однородный слой__', font=('Arial', 15), relief=tk.GROOVE,
             bg='#EEE8AA').grid(column=0, row=0, columnspan=2, stick='we')

    tk.Button(frame2, text='Сохранить коэффиценты', font=('Arial', 15), command=rem_value).grid(stick='we')
    tk.Button(frame2, text="start", font=('Arial', 15), command=start).grid(stick='we')


def situation_layer():
    global frame2
    global count_l_or_tr
    list_layer = np.array([[0. for i in range(9)]])
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

    frame2 = tk.Frame(win, bg='black')
    frame2.place(relx=0.25, rely=0, relwidth=0.50, relheight=1)
    frame2.grid_columnconfigure([0, 1, 2, 3, 4, 5], minsize=30)

    tk.Label(frame2, text='__Несколько однородных слоёв [2,5]__', font=('Arial', 15), relief=tk.GROOVE,
             bg='#EEE8AA').grid(column=0, row=0, columnspan=5,
                                stick='we')
    # разделение на два грунта
    tk.Label(frame2, text='Укажите количество' + '\n' + 'слоёв [2,5]', font=('Arial', 10, 'bold'), height=3,
             relief=tk.GROOVE, bg='#2F4F4F').grid(column=0, columnspan=2, row=1, stick='we')
    entry_layer = tk.Entry(frame2, fg="green", bg="white")
    entry_layer.grid(column=2, row=1, stick='we')
    tk.Button(frame2, text='сохранить кол-во', font=('Arial', 10), command=layer__).grid(column=3, row=1, stick='we')

    def list1():
        global list_layer
        sh_layer = np.shape(list_layer)
        n = 0
        if n < sh_layer[0]:
            save_layer(n)

    tk.Button(frame2, text='1', font=('Arial', 15), command=list1).grid(row=2, column=0)

    def list2():
        global list_layer
        sh_layer = np.shape(list_layer)
        n = 1
        if n < sh_layer[0]:
            save_layer(n)

    tk.Button(frame2, text='2', font=('Arial', 15), command=list2).grid(row=2, column=1)

    def list3():
        global list_layer
        sh_layer = np.shape(list_layer)
        n = 2
        if n < sh_layer[0]:
            save_layer(n)

    tk.Button(frame2, text='3', font=('Arial', 15), command=list3).grid(row=2, column=2)

    def list4():
        global list_layer
        sh_layer = np.shape(list_layer)
        n = 3
        if n < sh_layer[0]:
            save_layer(n)

    tk.Button(frame2, text='4', font=('Arial', 15), command=list4).grid(row=2, column=3)

    def list5():
        global list_layer
        sh_layer = np.shape(list_layer)
        n = 4
        if n < sh_layer[0]:
            save_layer(n)

    tk.Button(frame2, text='5', font=('Arial', 15), command=list5).grid(row=2, column=4)

    tk.Button(frame2, text="start", font=('Arial', 15), command=start).grid(columnspan=5)


def situation_slope():
    global frame2
    global count_l_or_tr
    count_l_or_tr = 2
    frame2.destroy()

    frame2 = tk.Frame(win, bg='black')
    frame2.place(relx=0.25, rely=0, relwidth=0.50, relheight=1)
    frame2.grid_columnconfigure(0, minsize=250)

    tk.Label(frame2, text='  Склон (два однородных слоя)  ', font=('Arial', 15), relief=tk.GROOVE,
             bg='#EEE8AA').grid(column=0, row=0, columnspan=2, stick='we')

    def slope1():
        global list_slope
        save_slope(0)

    tk.Button(frame2, text='верхний слой', font=('Arial', 15), command=slope1).grid(row=1, column=0)

    def slope2():
        global list_slope
        save_slope(1)

    tk.Button(frame2, text='Нижний слой', font=('Arial', 15), command=slope2).grid(row=1, column=1)

    tk.Button(frame2, text="запуск", font=('Arial', 15), command=start).grid(stick='we')

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

tk.Label(frame1, text='__Коэффиценты__', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=0, columnspan=2, stick='we')

tk.Label(frame1, text='height:', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=1, stick='we')
entry1_height = tk.Entry(frame1, fg="green", bg="white")
entry1_height.grid(column=1, row=1, stick='we')

# минимально количество жидкости в трубочке по вертикали после которого вода течёт
tk.Label(frame1, text='DOWN_MIN:', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=2, stick='we')
entry_down_min = tk.Entry(frame1, fg="green", bg="white")
entry_down_min.grid(column=1, row=2, stick='we')

# доля от объёма воды, который утекает
tk.Label(frame1, text='DOWN_PERC:', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=3, stick='we')
entry_down_pers = tk.Entry(frame1, fg="green", bg="white")
entry_down_pers.grid(column=1, row=3, stick='we')

# доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax1
tk.Label(frame1, text='DOWN_PERC_ax1:', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=4, stick='we')
entry_down_pers_ax1 = tk.Entry(frame1, fg="green", bg="white")
entry_down_pers_ax1.grid(column=1, row=4, stick='we')

# доля(от DOWN_PERS) который остаётся в этой ячейке, но переходит в горизонталь ax2
tk.Label(frame1, text='DOWN_PERC_ax2:', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=5, stick='we')
entry_down_pers_ax2 = tk.Entry(frame1, fg="green", bg="white")
entry_down_pers_ax2.grid(column=1, row=5, stick='we')

# минимальноеколичество по горизонтали для вытекания
tk.Label(frame1, text='LR_MIN:', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=6, stick='we')
entry_lr_min = tk.Entry(frame1, fg="green", bg="white")
entry_lr_min.grid(column=1, row=6, stick='we')

# Сколько вытекает в общем по горизонтали
tk.Label(frame1, text='LR_PERC:', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=7, stick='we')
entry_lr_pers = tk.Entry(frame1, fg="green", bg="white")
entry_lr_pers.grid(column=1, row=7, stick='we')

# то, сколько перетекает влево
tk.Label(frame1, text='LR_PERC_L:', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=8, stick='we')
entry_lr_pers_l = tk.Entry(frame1, fg="green", bg="white")
entry_lr_pers_l.grid(column=1, row=8, stick='we')

# то, сколько перетекает вправо
tk.Label(frame1, text='LR_PERC_R:', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=9, stick='we')
entry_lr_pers_r = tk.Entry(frame1, fg="green", bg="white")
entry_lr_pers_r.grid(column=1, row=9, stick='we')

# фрейм сохранения значений
frame2 = tk.Frame(win, bg='black')
frame2.place(relx=0.25, rely=0, relwidth=0.50, relheight=1)
frame2.grid_columnconfigure(0, minsize=250)

an = tk.Label(frame2, text='  Выберете режим  ', relief=tk.GROOVE, bg='#EEE8AA').grid(column=0, row=0, columnspan=2,
                                                                                   stick='we')

# фрейм с кнопками взятия разреза, старта и справки по проге
frame3 = tk.Frame(win, bg='red')
frame3.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)

# разрез
tk.Label(frame3, text=('Укажите номер' + '\n' + 'разреза'), font=('Arial', 10, 'bold'), height=3, relief=tk.GROOVE,
         bg='#2F4F4F').grid(stick='we')
entry_incision = tk.Entry(frame3, fg="green", bg="white")
# размещение надо прописывать отдельно, иначе не будет работать
entry_incision.grid(stick='we')
tk.Button(frame3, text='сохранить номер', command=incision, font=('Arial', 10)).grid(stick='we')

text_s = 'тут \n будет \n справка' \
         ' \n по \n проге'
def onInfo():
    global text_s
    mbox.showinfo("Информация", text_s)
tk.Button(frame3, text='Справка по проге', command=onInfo, font=('Arial', 10)).grid(stick='we')


app = Example()
win.mainloop()