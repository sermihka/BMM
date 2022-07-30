#import version_2
from tkinter import *
import numpy as np
from tkinter import messagebox
import matplotlib.pyplot as plt

fig_graf = plt.figure(figsize=(7, 7))

ax_graf = fig_graf.add_subplot()

ax_graf.minorticks_on()
ax_graf.grid(which='major')




win = Tk()
# the background
win['bg'] = '#fafafa'
# name of win
win.title('просачивание жидкостей')
# раззмер окна
win.geometry('500x350')
# запрет на изменение размера:
win.resizable(width=False, height=False)

#рамка для расположение объектов
# во фрейме проще чем внутри класса TK
frame = Frame(win, bg='gray')
# указываем сколько фрейм будет занимать от окна
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# создаём надпись с просьбой ввести значения
title_k = Label(win, text='введите пожалуйста последовательно вязкость, плотность и проницаемость', bg='white', font=('Arial', 10))
title_k.grid()

# Вязкость
viscosity_Input = Entry(frame, bg='white')
viscosity_Input.grid()
# Плотность
density_Input = Entry(frame, bg='white')
density_Input.grid()
# Проницаемость
permeability_Input = Entry(frame, bg='white')
permeability_Input.grid()


def btn_click():
    # функция, которую потом вызывает нажатие кнопки
    viscosity = viscosity_Input.get()
    density = density_Input.get()
    permeability = permeability_Input.get()
    # z = 19 у нас по сути кубик возвышается над осью на 19 делений,
    # и по сути чтобы это учесть надо прописать: (z - (n+1))
    # пока что мы просто учитываем количество пройденных ячеек
    N = 0.
    L = 0.00008 # это вроде как расстояние между песчинками
    # (сделали пока равным диаметру песчинки)
    g = 9.8 # константа (9.8)
    # смещение по горизонтали
    x = 0.
    x_grid = np.array([])
    y_grid = np.array([])
    for n in range(2, 1000):
        N += 1/n
        # чисто по вертикали
        t_vertical = (N * L * float(viscosity))/(float(density) * g * float(permeability))
        # тупо по вертикали не учитывая распространения по горизонтали
        x_grid = np.append(x_grid, 0.8*n*(10**(-4)))
        y_grid = np.append(y_grid, t_vertical)
    graf = ax_graf.plot(y_grid, x_grid)
    plt.show()






    info_str = f'Данные: вязкость - {str(viscosity)}, плотность - {str(density)}, проницаемость - {str(permeability)}'
    messagebox.showinfo(title='Результат', message=info_str)
    # получаем введёный текст в поля loginInput и passField

# Кнопка вызова результата
btn = Button(frame, text='кнопка', bg='yellow', command=btn_click)

btn.grid()

win.mainloop()
#version_2.func()


