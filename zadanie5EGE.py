
for i in range(33):
    N = i
    R = 0
    N = bin(N)
    N = str(N) + str(N.count("1") % 2)
    N = str(N) + str(N.count("1") % 2)
    R = int(N,2)
    if R > 77:
        print(i)
        break


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
