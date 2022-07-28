#import version_2
from tkinter import *

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

win.mainloop()
# version_2.func()


