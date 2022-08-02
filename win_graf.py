"""
Окно три столбца, первый столбец выбрать жидкость , пока что только вода, второй столбец выбор почвы ,
пока что только песок , последний столбец кнопка старт (начало)
"""
import tkinter as tk
import pipeline_3d_model
choice_soil = ''
choice_liquid = ''

# функция вызванная кнопкой воды
def water():
    global choice_liquid
    choice_liquid = 'water'

# функция вызванная кнопкой "sand"
def sand():
    global choice_soil
    choice_soil = 'sand'

# функция вызываемая кнопкой "liquid"
def liquid():
    tk.Button(win, text='water', command=water, activebackground='blue').grid(row=3, column=0, stick='we')
# функция вызываемая кнопкой "soil"
def soil():
    tk.Button(win, text='sand', command=sand, activebackground='yellow').grid(row=3, column=1, stick='we')

def start():
    global choice_liquid
    global choice_soil
    if choice_soil == 'sand' and choice_liquid == 'water':
        v, h1, h2 = pipeline_3d_model.cycle(300)
        RES = pipeline_3d_model.incision(v, h1, h2)
        pipeline_3d_model.graph(RES)

win = tk.Tk()

# интерфейс окна
win.config(bg='#55E0FF')
win.title('Матиматическое моделирование процесса просацивания жидкости в пористые среды')
# размеры
win.geometry("800x400+100+200")
win.minsize(300, 400)
win.maxsize(700, 800)
# запрет на именения размера окна
win.resizable(False, False)
# текстовые надписи
tk.Label(win, text='Выберите жидкость', bg='#43FF91', font=('Arial', 10, 'bold'), width=15, height=5,).grid(row=0, column=0, stick='we')
tk.Label(win, text='Выберите породу', bg='#43FF91', font=('Arial', 10, 'bold'), width=15, height=5,).grid(row=0, column=1, stick='we')
tk.Label(win, text='Нажмите для вывода', bg='#43FF91', font=('Arial', 10, 'bold'), width=15, height=5, justify=tk.CENTER).grid(row=0, column=2, stick='we')
# кнопки
tk.Button(win, text='liquid', command=liquid).grid(row=1, column=0, stick='we', rowspan=(2))
tk.Button(win, text='soil', command=soil).grid(row=2, column=1, stick='we')
tk.Button(win, text='start', command=start).grid(row=3, column=2)
# минимальные размеры колонок
win.grid_columnconfigure(0, minsize=250)
win.grid_columnconfigure(1, minsize=250)
win.grid_columnconfigure(2, minsize=200)
win.mainloop()