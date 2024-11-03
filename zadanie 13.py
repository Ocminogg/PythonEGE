# print(bin(248)[2:])
# print("00" + bin(46)[2:])
# print(bin(16)[2:])
# print(bin(128)[2:])
# s = bin(2**15 - 1)[2:]
# print(s)
# print(len(s))
# print(6**5 + 2700)
# count = 0
# for i in range(2**14):
#     s = bin(i)[2:]
#     if (s.count("1") + 6) % 2 == 1:
#         count += 1
# print(count)

# count = 0
# flag = True
# for i in range(17):
#     for j in range(2**i):
#         s = bin(j)[2:]
#         if (6 > s.count("0")):
#             flag = False
#             break
#     if flag == True:
#         print(i)
#         break


# A = "0" * 8
# print(A)
# for i in range(8):
#     A = A.replace(A[i],"1",1)
#     print(A)

import sys
sys.setrecursionlimit(10**6)

def F(n):
    if n < 11:
        return 10
    elif n >= 11:
        return n + F(n-1)
print(F(2022) - F(2019))
