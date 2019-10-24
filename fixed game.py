from tkinter import *
from random import randrange as rnd
import math

root = Tk()
root.geometry('1000x1000')
c = Canvas(root, bg='white')
c.pack(fill=BOTH, expand=1)


def ball():
    global list_of_balls, list_of_b_parameters, colorb, o

    x = rnd(200, 600)
    y = rnd(200, 600)
    R = rnd(30, 150)
    dx = rnd(-10, 10)
    dy = rnd(-10, 10)

    import random
    r = lambda: random.randint(0, 255)
    colorb = '#%02X%02X%02X' % (r(), r(), r())  # цвет шарика принимает случайное значение от (0, 0, 0) до (255, 255,
    # 255)
    list_of_b_parameters.append([x, y, R, dx, dy])  # заполняем список параметров шарика (координаты, радиус,
    # перемещение за ед. времени) новыми парметрами
    o = c.create_oval(x - R, y - R, x + R, y + R, fill=colorb, width=0)
    list_of_balls.append(o)  # добавляем новый шарик в список шариков

    root.after(2000, ball)


def triangle():
    global list_of_triangles, list_of_t_parameters, colort

    x = rnd(200, 600)
    y = rnd(200, 600)
    R = rnd(30, 150)
    x01 = - R * math.cos(math.pi / 6)
    y01 = - R * math.sin(math.pi / 6)
    x02 = 0
    y02 = R * math.cos(math.pi / 6)
    x03 = R * math.cos(math.pi / 6)
    y03 = - R * math.sin(math.pi / 6)
    theta = rnd(-10, 10)

    import random
    r = lambda: random.randint(0, 255)
    colort = '#%02X%02X%02X' % (r(), r(), r())
    list_of_t_parameters.append([x, y, R, x01, y01, x02, y02, x03, y03, theta / 100])
    t = c.create_polygon(x - R * math.cos(math.pi / 6), y - R * math.sin(math.pi / 6), x, y + R * math.cos(math.pi / 6),
                         x + R * math.cos(math.pi / 6), y - R * math.sin(math.pi / 6), fill=colort, width=0, tag='t')
    list_of_triangles.append(t)

    root.after(3000, triangle)


def ball_motion():
    global list_of_balls, list_of_b_parameters
    for i in range(len(list_of_balls)):
        import random

        if list_of_b_parameters[i][0] - list_of_b_parameters[i][2] + list_of_b_parameters[i][3] < 0 or \
                list_of_b_parameters[i][
                    0] + list_of_b_parameters[i][2] + list_of_b_parameters[i][
            3] > 800:  # проверка, есть ли стенка справа или
            # слева
            list_of_b_parameters[i][3] *= -random.gauss(0.5, 1.2)  # горизонатльная компонента перемещения меняет
            # направление на противоположное

        if list_of_b_parameters[i][1] - list_of_b_parameters[i][2] + list_of_b_parameters[i][4] < 0 or \
                list_of_b_parameters[i][
                    1] + list_of_b_parameters[i][2] + list_of_b_parameters[i][
            4] > 800:  # проверка, есть ли стенка сверху или
            # снизу
            list_of_b_parameters[i][4] *= -random.gauss(0.5, 1.2)  # вертикальная компонента перемещения меняет
            # направление на противоположное

        c.move(list_of_balls[i], list_of_b_parameters[i][3], list_of_b_parameters[i][4])  # шарик двигается с новой
        # скоостью
        list_of_b_parameters[i][0] += list_of_b_parameters[i][3]  # меняем координаты на величину перемещения
        list_of_b_parameters[i][1] += list_of_b_parameters[i][4]

    root.after(10, ball_motion)


def rotation_of_triangle():
    for i in range(len(list_of_triangles)):
        global a, list_of_parameters
        c.delete('t')
        c.delete('a')
        # поворачиваем треугольник на # theta / 100:
        a = c.create_polygon(list_of_t_parameters[i][3] + list_of_t_parameters[i][0],
                             list_of_t_parameters[i][4] + list_of_t_parameters[i][1],
                             list_of_t_parameters[i][5] + list_of_t_parameters[i][0],
                             list_of_t_parameters[i][6] + list_of_t_parameters[i][1],
                             list_of_t_parameters[i][7] + list_of_t_parameters[i][0],
                             list_of_t_parameters[i][8] + list_of_t_parameters[i][1],
                             fill=colort, tag='a')
        list_of_t_parameters[i][3] = list_of_t_parameters[i][3] * math.cos(list_of_t_parameters[i][9]) + \
                                     list_of_t_parameters[i][4] * math.sin(list_of_t_parameters[i][9])
        list_of_t_parameters[i][4] = - list_of_t_parameters[i][3] * math.sin(list_of_t_parameters[i][9]) + \
                                     list_of_t_parameters[i][4] * math.cos(list_of_t_parameters[i][9])
        list_of_t_parameters[i][5] = list_of_t_parameters[i][5] * math.cos(list_of_t_parameters[i][9]) + \
                                     list_of_t_parameters[i][6] * math.sin(list_of_t_parameters[i][9])
        list_of_t_parameters[i][6] = - list_of_t_parameters[i][5] * math.sin(list_of_t_parameters[i][9]) + \
                                     list_of_t_parameters[i][6] * math.cos(list_of_t_parameters[i][9])
        list_of_t_parameters[i][7] = list_of_t_parameters[i][7] * math.cos(list_of_t_parameters[i][9]) + \
                                     list_of_t_parameters[i][8] * math.sin(list_of_t_parameters[i][9])
        list_of_t_parameters[i][8] = - list_of_t_parameters[i][7] * math.sin(list_of_t_parameters[i][9]) + \
                                     list_of_t_parameters[i][8] * math.cos(list_of_t_parameters[i][9])
        list_of_triangles[i] = a

    root.after(10, rotation_of_triangle)


def click_1(event):
    global deleting_list_1, deleting_list_2, file, score
    deleting_list_2 = []
    deleting_list_1 = []
    for i in range(len(list_of_balls)):
        if (list_of_b_parameters[i][0] - event.x) ** 2 + (list_of_b_parameters[i][1] - event.y) ** 2 < \
                (list_of_b_parameters[i][2]) ** 2:  # проверяем, попали ли в шарик
            c.delete(list_of_balls[i])
            deleting_list_1.append(i)
            score += 1
            button1 = Button(root, text='result: ' + str(score), width=25, height=5, bg='black', font='calibri 25',
                             fg="black")
            button1.pack()
            button1.place(x=30, y=30)
    for m in deleting_list_1:   # удаляем шарик и его параметры из соответствующих списков
        list_of_b_parameters.pop(m)
        list_of_balls.pop(m)

    for l in range(len(list_of_triangles)):
        if (list_of_t_parameters[l][0] - event.x) ** 2 + (list_of_t_parameters[l][1] - event.y) ** 2 < \
                list_of_t_parameters[l][2] ** 2:    # проверяем, попали ли в треугольник
            c.delete(list_of_triangles[l])
            deleting_list_2.append(l)
            score += 3
            button1 = Button(root, text='result: ' + str(score), width=25, height=5, bg='black', font='calibri 25',
                             fg="black")
            button1.pack()
            button1.place(x=30, y=30)
    for n in deleting_list_2:   # удаляем треугольник и его параметры из соответствующих списков
        list_of_t_parameters.pop(n)
        list_of_triangles.pop(n)

    file = open('Players.txt', 'a')     # добавляем результат игрока в файл
    file.write('\n')
    file.write(str(score))
    file.close()


def start():
    global file
    print('name:')
    name = str(input())
    file = open('Players.txt', 'a')
    file.write('\n')
    file.write('results of ')
    file.write(name)
    file.write(':')
    file.close()


error = 0
score = 0

list_of_balls = []
list_of_b_parameters = []
list_of_triangles = []
list_of_t_parameters = []

start()
ball()
ball_motion()
triangle()
rotation_of_triangle()
c.bind('<Button-1>', click_1)

mainloop()