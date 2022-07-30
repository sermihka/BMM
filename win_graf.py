#Окно три столбца, первый столбец выбрать жидкость , пока что только вода, второй столбец выбор почвы , пока что только песок , последний столбец кнопка старт (начало)
from operator import truediv
import tkinter as tk
choice_soil ='Ничего'
choice_liquid='Ничего'
water_p='вода'
oil_p='нейть'
butter_p='масло'
sand_p='песок'
clay_p='глина'
dert_p='земля'
def water():
    print('вы выбрали воду')
    global choice_liquid
    choice_liquid='Вода'
def oil():
    print('вы выбрали нефть')
    global choice_liquid
    choice_liquid='Нефть'
def butter():
    print('вы выбрали масло')
    global choice_liquid
    choice_liquid='Масло'   
def sand():
    print('вы выбрали песок')
    global choice_soil
    choice_soil='Песок'
def clay():
    print('вы выбрали глину')
    global choice_soil
    choice_soil='Глину'
def dert():
    print('вы выбрали землю')
    global choice_soil
    choice_soil='Землю'
def liquid():
    global liquid
    liquid=''
    tk.Button(win,text='water',command=water,activebackground='blue').grid(row=3,column=0,stick='we')
    tk.Button(win,text='oil',command=oil,activebackground='black').grid(row=4,column=0,stick='we')
    tk.Button(win,text='butter',command=butter,activebackground='yellow').grid(row=5,column=0,stick='we')
def soil():
    global soil
    soil = ''
    tk.Button(win,text='sand',command=sand,activebackground='yellow').grid(row=3, column=1, stick='we')
    tk.Button(win,text='clay',command=clay,activebackground='brown').grid(row=4, column=1, stick='we')
    tk.Button(win,text='dert',command=dert,activebackground='brown').grid(row=5, column=1, stick='we')
def start():
    global choice_liquid
    print('Вы выбрали условия жидкости', choice_liquid, 'и условие почвы', choice_soil)
win = tk.Tk()
#photo=tk.PhotoImage(file='D:\БММ\python графика уроки/62881.png')
#win.iconphoto(False, photo)
win.config(bg='#55E0FF')
win.title('Матиматическое моделирование процесса просацивания жидкости в пористые среды')
win.geometry("800x400+100+200")
win.minsize(300,400)
win.maxsize(700,800)
win.resizable(False,False)
tk.Label(win,text='Выберите жидкость',bg='#43FF91',font=('Arial',10,'bold'),width=15,height=5,).grid(row=0,column=0,stick='we')
tk.Label(win,text='Выберите породу',bg='#43FF91',font=('Arial',10,'bold'),width=15,height=5,).grid(row=0,column=1,stick='we')
tk.Label(win,text='Нажмите для вывода',bg='#43FF91',font=('Arial',10,'bold'),width=15,height=5,justify=tk.CENTER).grid(row=0,column=2,stick='we')
tk.Button(win,text='liquid',command=liquid).grid(row=1,column=0,stick='we',rowspan=(2))
tk.Button(win,text='soil',command=soil).grid(row=2,column=1,stick='we')
tk.Button(win,text='start',command=start).grid(row=3,column=2)
win.grid_columnconfigure(0, minsize=250)
win.grid_columnconfigure(1, minsize=250)
win.grid_columnconfigure(2, minsize=200)
win.mainloop()