"""
Окно три столбца, первый столбец выбрать жидкость , пока что только вода, второй столбец выбор почвы ,
пока что только песок , последний столбец кнопка старт (начало)
"""
import tkinter as tk
import pipeline_3d_model
choice_soil = ''
choice_liquid = ''
ax_incision = (pipeline_3d_model.ax0_max)//2


def incision():
    global ax_incision
    n = int(entry_incision.get())
    if n > (-(pipeline_3d_model.ax0_max)//2) and n < ((pipeline_3d_model.ax0_max)//2):
        ax_incision = ((pipeline_3d_model.ax0_max)//2) + n


def water():
    # функция вызванная кнопкой воды
    global choice_liquid
    choice_liquid = 'water'


def sand():
    # функция вызванная кнопкой "sand"
    global choice_soil
    choice_soil = 'sand'


def liquid():
    # функция вызываемая кнопкой "liquid"
    tk.Button(frame1, text='water', command=water, activebackground='blue').grid(row=2, column=0, stick='we')


def soil():
    # функция вызываемая кнопкой "soil"
    tk.Button(frame2, text='sand', command=sand, activebackground='yellow').grid(row=2, column=0, stick='we')


def start():
    global choice_liquid
    global choice_soil
    if choice_soil == 'sand' and choice_liquid == 'water':
        v, h1, h2 = pipeline_3d_model.cycle(700)
        RES = pipeline_3d_model.incision(v, h1, h2, ax2_incision=ax_incision)
        pipeline_3d_model.graph(RES)

win = tk.Tk()

# интерфейс окна
win.title('Матиматическое моделирование процесса просацивания жидкости в пористые среды')

# размеры
win.geometry("1000x500")
"""win.minsize(300, 400)
win.maxsize(700, 800)"""

# запрет на именения размера окна
win.resizable(False, False)


# фрейм с жидкостью
frame1 = tk.Frame(win, bg='blue')
frame1.place(relx=0, rely=0, relwidth=0.25, relheight=1)
frame1.grid_columnconfigure(0, minsize=250)
# виджеты фрейма с жидкостью
tk.Label(frame1, text='Выберите жидкость', font=('Arial', 10, 'bold'), height=2).grid(stick='we')
tk.Button(frame1, text='liquid', command=liquid, font=('Arial', 10)).grid(row=1, column=0, stick='we')


# фрейм с породой
frame2 = tk.Frame(win, bg='brown')
frame2.place(relx=0.25, rely=0, relwidth=0.25, relheight=1)
frame2.grid_columnconfigure(0, minsize=250)
# виджеты фрейма с породой
tk.Label(frame2, text='Выберите породу', font=('Arial', 10, 'bold'), height=2).grid(stick='we')
tk.Button(frame2, text='soil', command=soil, font=('Arial', 10)).grid(row=1, column=0, stick='we')


# стартовый фрейм
frame3 = tk.Frame(win, bg='gray')
frame3.place(relx=0.50, rely=0, relwidth=0.25, relheight=1)
frame3.grid_columnconfigure(0, minsize=250)
frame3.grid_rowconfigure(1, minsize=300)
# виджеты стартового фрейма
tk.Label(frame3, text='Нажмите для вывода', font=('Arial', 10, 'bold'), height=2).grid(stick='we')
tk.Button(frame3, text='start', command=start, font=('Arial', 10), width=10, height=3).grid(row=1, column=0)

# фрейм с изменяемыми значениями
frame4 = tk.Frame(win, bg='black')
frame4.place(relx=0.75, rely=0, relwidth=0.25, relheight=1)
frame4.grid_columnconfigure(0, minsize=250)
# виджеты


tk.Label(frame4, text='Укажите номер разреза', font=('Arial', 10, 'bold'), height=2).grid(stick='we')
entry_incision = tk.Entry(frame4, fg="green", bg="white", width=50)
# размещение надо прописывать отдельно, иначе не будет работать
entry_incision.grid()
tk.Button(frame4, text='remember', command=incision, font=('Arial', 10)).grid(stick='we')


win.mainloop()