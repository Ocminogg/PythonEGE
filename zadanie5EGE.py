
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

# R = 0
# maxR = 0
# for n in range(103):
#     n = bin(n)[2:]
#     if n[len(n)-1] == '0':
#         n = n + '10'
#     else:
#         n = n + '01'
#     R = int(n,2)
#     if R < 102:
#         maxR = max(maxR,R)
# print(maxR)
# N = "123456789"
# print(N[-3:])
Nbin = ""
R = 0
ArrayR = []
for N in range(1,200):
    Nbin = bin(N)[2:]
    if N % 3 == 0:
        Nbin = Nbin + Nbin[-3:]
    else:
        Nbin = Nbin + bin((N % 3) * 3)[2:]
    R = int(Nbin, 2)
    if R > 151:
        ArrayR.append(R)
print(min(ArrayR))
print('Индекс искомого числа в массиве ',ArrayR.index(min(ArrayR)))
print(ArrayR)


