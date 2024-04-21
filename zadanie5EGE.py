
# for i in range(33):
#     N = i
#     R = 0
#     N = bin(N)
#     N = str(N) + str(N.count("1") % 2)
#     N = str(N) + str(N.count("1") % 2)
#     R = int(N,2)
#     if R > 77:
#         print(i)
#         break


# for x in range(256):
#     x = bin(x)
#     x = x.replace("0b",'',1)
#
#     if len(x) != 8:
#         t = len(x)
#         x = (8-t)*"0" + x
#     y = ""
#
#     for i in range(8):
#         if x[i] == "0":
#             y = y + "1"
#         elif x[i] == "1":
#             y = y + "0"
#
#     x = int(x, 2)
#
#
#     y = int(y, 2)
#     if (y - x) == 111:
#         print(x)
#         print(bin(x))
#         break

# for N in range(100,3001):
#     start = str(N)
#     N = bin(N)
#     N = str(N)
#     N = N.replace("0b","",1)
#     Ndop = N
#     count = 0
#     for i in range(len(N) - 1):
#         if N[i+1] == "0":
#             count += 1
#         else:
#             break
#     N = N.replace("1","",1)
#     N = N.replace("0","",count)
#     if N == "":
#         N = "0"
#
#     print(N)

# a = []
# for x in range(100, 3001):
#     i = int(bin(x)[3:], 2)
#     if x - i not in a:
#         a.append(x-i)
# print(len(a))


import turtle as t
t.left(90)
t.speed(0)
k = 30
x = 4
t.down()
for i in range(4):
    t.forward(x * k)
    t.right(90)
    t.forward(x * k)
    t.left(90)
    t.forward(x * k)
    t.right(90)
t.up()
for i in range(0, 3 * x + 1):
    for y in range(-x, 2 * x + 1):
        t.goto(i * k, y * k)
        t.dot()
t.mainloop()