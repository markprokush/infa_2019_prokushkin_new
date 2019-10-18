from tkinter import *
from random import randrange as rnd
import time
import math

root = Tk()
root.geometry('1000x1000')
c = Canvas(root, bg='white')
c.pack(fill=BOTH, expand=1)


def ball():
    global list_of_balls, list_of_parameters, x, y, R, dx, dy, color, o
    x = rnd(200, 600)
    y = rnd(200, 600)
    R = rnd(30, 150)
    dx = rnd(-10, 10)
    dy = rnd(-10, 10)
    import random
    r = lambda: random.randint(0, 255)
    color = '#%02X%02X%02X' % (r(), r(), r())  # цвет шарика принимает случайное значение от (0, 0, 0) до (255, 255,
    # 255)
    list_of_parameters.append([x, y, R, dx, dy])  # заполняем список параметров шарика (координаты, радиус,
    # перемещение за ед. времени) новыми парметрами
    o = c.create_oval(x - R, y - R, x + R, y + R, fill=color, width=0)

    list_of_balls.append(o)  # добавляем новый шарик в список шариков
    root.after(2000, ball)


def ball_motion():
    global list_of_balls, list_of_parameters
    for i in range(len(list_of_balls)):
        import random

        if list_of_parameters[i][0] - list_of_parameters[i][2] + list_of_parameters[i][3] < 0 or list_of_parameters[i][
            0] + list_of_parameters[i][2] + list_of_parameters[i][3] > 800:  # проверка, есть ли стенка справа или
            # слева
            list_of_parameters[i][3] *= -random.gauss(0.5, 1.2)  # горизонатльная компонента перемещения меняет
            # направление на противоположное

        if list_of_parameters[i][1] - list_of_parameters[i][2] + list_of_parameters[i][4] < 0 or list_of_parameters[i][
            1] + list_of_parameters[i][2] + list_of_parameters[i][4] > 800:  # проверка, есть ли стенка сверху или
            # снизу
            list_of_parameters[i][4] *= -random.gauss(0.5, 1.2)  # вертикальная компонента перемещения меняет
            # направление на противоположное

        c.move(list_of_balls[i], list_of_parameters[i][3], list_of_parameters[i][4])     # шарик двигается с новой
        # скоостью
        list_of_parameters[i][0] += list_of_parameters[i][3]       # меняем координаты на величину перемещения
        list_of_parameters[i][1] += list_of_parameters[i][4]

    root.after(10, ball_motion)


def click_1(event):
    global j

    for i in range(len(list_of_balls)):
        if (list_of_parameters[i][0] - event.x) ** 2 + (list_of_parameters[i][1] - event.y) ** 2 < \
                list_of_parameters[i][2] ** 2:
            c.delete(list_of_balls[i])

            j += 1
            button1 = Button(root, text='result: ' + str(j), width=25, height=5, bg='black', fg='black',
                             font='calibri 25')
            button1.pack()
            button1.place(x=30, y=30)


j = 0
list_of_balls = []
list_of_parameters = []

ball()
ball_motion()
c.bind('<Button-1>', click_1)



mainloop()