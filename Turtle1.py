from turtle import *
left(90)
k = 65 # масштаб
tracer(0) #скорость
up()
goto(0 * k, 5 * k) #начальное расположение
down()
for i in range(12):
    right(60)
    forward(1 * k)
    right(60)
    forward(1 * k)
    right(270)
up() #Черепаха поднимает хвост
for x in range(-5, 20):
    for y in range(-5, 20):
        goto(x * k, y * k)
        dot(3, "red")
        dot(1, "white")
mainloop()


# import turtle
#
# t = turtle.Turtle()
# t.reset()
# t.seth(90)
# t.width(2)
# t.speed(100)
# k = 10  # коэффициент для увеличения масштаба
# t.right(180)
# t.forward(2 * k)
# t.right(90)
# t.forward(40 * k)
# t.right(90)
# t.forward(2 * k)
#
# t.forward(2)
# for i in range(4):
#     t.seth(90)
#     t.circle(-5 * k, 180)
# t.penup()
#
# for x in range(0, -12, -1):
#     for y in range(-2, 8):
#         t.goto(x * k, y * k)
#         t.dot(5)
# turtle.mainloop()


# from turtle import * # Подключим модуль черепашка
#
# color('black', 'red')  # устанавливаем цвет пера и цвет заливки
# speed(100)
# lt(90)
# k = 15  # коэффициент для настраивания более удобного масштаба
# begin_fill()
# for i in range(7): # указываем число циклов необходимое до полного завершения фигуры
#     forward(10 * k)  # Пройти вперед на 10
#     right(120)
# end_fill()
# cnt = 0
# canvas = getcanvas()
# for x in range(0 * k, 40 * k, k):
#     for y in range(0 * k, 40 * k, k):
#         s = canvas.find_overlapping(x, y, x, y)
#         print(s)
#         if len(s) == 1 and s[0] == 5:
#             cnt += 1
# print(cnt)
# done()
# exit()
