# from turtle import *
# left(90)
# k = 70 # масштаб
# tracer(0) #скорость
# up()
# goto(0 * k, 0 * k) #начальное расположение
# down()
# for i in range(12):
#     right(60)
#     forward(1 * k)
#     right(60)
#     forward(1 * k)
#     right(270)
# up() #Черепаха поднимает хвост
#
# for x in range(-10, 10):
#     for y in range(-10, 10):
#         goto(x * k, y * k)
#         dot(3, "red")
#         dot(1, "white")
# mainloop()


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

# import turtle
# t=turtle.Turtle()
# t.reset()
# t.seth(90)
# t.width(2)
# t.speed(5)
# k = 10 #коэффициент для увеличения масштаба
# t.right(180)
# t.forward(5*k)
# t.right(90)
# t.forward(50*k)
# t.right(90)
# t.forward(5*k)
# for i in range(5):
#     t.seth(90)
#     t.circle(-5*k,180)
# t.penup()
# for x in range(0,-14,-1):
#     for y in range(-5,8):
#         t.goto(x*k , y*k )
#         t.dot(5)
# turtle.mainloop()

# import turtle
# t=turtle.Turtle()
# t.reset()
# t.seth(90)
# # t.width(2)
# t.speed(50)
# k = 50 #коэффициент для увеличения масштаба
# for i in range(5):
#     t.right(90)
#     t.circle(5*k,180)
# t.penup()
# for x in range(-15,6,1):
#     for y in range(-5,16):
#         t.goto(x*k , y*k )
#         t.dot(5)
# t.penup()
# turtle.mainloop()

# from turtle import *
# left(90)
# k=30
# tracer(0)
# up()
# goto(0 * k, -10 * k)
# down()
# right(315)
# for i in range(7):
#     forward(16 * k )
#     right(45)
#     forward(8 * k )
#     right(135)
# up()
# for x in range (-20, 5):
#     for y in range (-20, 13):
#         goto(x * k, y * k)
#         dot(3, 'red')
#         dot(1, 'white')
# mainloop()

# import turtle
# t=turtle.Turtle()
# t.reset()
# t.seth(90)
# t.width(2)
# t.speed(20)
# k = 10 #коэффициент для увеличения масштаба
# for i in range(5):
#     t.right(90)
#     t.circle(5*k,180)
#     t.right(90)
#     t.circle(5*k,180)
#     t.right(90)
#     t.circle(5*k,180)
#     t.right(90)
#     t.circle(5*k,180)
# t.penup()
# for x in range(-15,6,1):
#     for y in range(-5,16):
#         t.goto(x*k , y*k )
#         t.dot(5)
# t.penup()
# turtle.mainloop()

from turtle import *
left(90)
k = 30
tracer(0)
up()
goto(0 * k, 0 * k)
down()
x = 6
for i in range(4):
    forward(x * k)
    right(90)
    forward(x * k)
    left(90)
    forward(x * k)
    right(90)
up()
for x in range(-12, 20):
    for y in range(-12, 20):
        goto(x * k, y * k)
        dot(2,'red')
        dot(4,'green')
mainloop()