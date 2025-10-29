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
# Nbin = ""
# R = 0
# ArrayR = []
# for N in range(1,200):
#     Nbin = bin(N)[2:]
#     if N % 3 == 0:
#         Nbin = Nbin + Nbin[-3:]
#     else:
#         Nbin = Nbin + bin((N % 3) * 3)[2:]
#     R = int(Nbin, 2)
#     if R > 151:
#         ArrayR.append(R)
# print(min(ArrayR))
# print('Индекс искомого числа в массиве ',ArrayR.index(min(ArrayR)))
# print(ArrayR)

# for N in range(128, 256):
#     s = bin(N)[2:]
#     s = s.replace("1", "2")
#     s = s.replace("0", "1")
#     s = s.replace("2", "0")
#     res = int(s,2)
#     sub = N - res
#     if sub == 105:
#         print(N)

# A = []
# for N in range(10000, 100000):
#     # first
#     s = oct(N)[2:]
#     for i in range(len(s)):
#         if int(s[i]) % 2 != 0:
#             s = s.replace(s[i],"2")
#     s = s + str(N % 8)
#     res = int(s, 8)
#     # second
#     s = oct(res)[2:]
#     for i in range(len(s)):
#         if int(s[i]) % 2 != 0:
#             s = s.replace(s[i], "2")
#     s = s + str(N % 8)
#     res = int(s, 8)
#     # final
#     if res % 2023 == 0:
#         A.append(N)
# print(sum(A))

# maxR = 0
# for N in range(123_456_789, 456_789_012):
#     N_bin = bin(N)[2:]
#     if N % 2 == 0:
#         N_bin = "11" + N_bin
#     else:
#         N_bin = "1" + N_bin + "10"
#     maxR = max(int(N_bin,2),maxR)
# print(maxR)

# for N in range(0, 100):
#     binN = bin(N)[2:]
#     sumNum = 0
#     for num in binN:
#         sumNum += int(num)
#     if sumNum % 2 == 0:
#         s = "10" + s[2:] + '0'
#     else:
#         s = "11" + s[2:] + "1"
#     if int(binN, 2) > 40:
#         print(N)
#         break
count = 0
startR = 1222222222
binStart = bin(startR)[2:-5]

endR = 1555555666
binEnd = bin(endR)[2:-5]
print(binStart, int(binStart, 2))
print(binEnd, int(binEnd, 2))

print(bin(0)[2:])

startN = int(binStart, 2)
endN = int(binEnd, 2)
for N in range(startN - 1000000, endN + 1000000):
    binN = bin(N)[2:]

    extra = bin(N % 3)[2:]
    if len(extra) < 2:
        extra = "0" + extra
    binN += extra

    extra = bin(int(binN, 2) % 5)[2:]
    if len(extra) < 2:
        extra = "00" + extra
    elif len(extra) < 3:
        extra = "0" + extra
    binN += extra

    R = int(binN, 2)
    if startR <= R <= endR:
        count += 1

print(count)#2083335
