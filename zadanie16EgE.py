# def F(n):
#     if n == 0:
#         return 3
#     if 0 < n and n <= 15:
#         return F(n-1)
#     if 15 < n and n < 100:
#         return 2.5 * F(n-3)
#     if n >= 100:
#         return 3.3 * F(n-2)
# print(F(100))


# def F(n):
#     if n == 0:
#         return 0
#     if n % 2 == 1:
#         return F(n - 1) + 1
#     if (n > 0) and (n % 2 == 0):
#         return F(n/2)

# count = 0
# for i in range(1000000000):
#     if F(i) == 2:
#         count += 1
#     print(count)
# print(count)

# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2*G(n-1)+5*n
# def G(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return F(n-1)+2*n
# print(F(4) + G(4))

# def F(n):
#     if n == 1:
#         return 1
#     if n % 2 != 0 and n > 1:
#         return n + F(n - 2)
#     if n % 2 == 0:
#         return n * F(n - 1)
#
# print(F(40))

# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2:
#         return 2 * F(n - 1) + (n - 2) * F(n - 2)
# print(F(6))

import sys
sys.setrecursionlimit(10**6)
def F(n):
    if n < 11:
        return 10
    else:
        return n + F(n - 1)
print(F(2124) - F(2122))
# def F(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return n + F(n-1)
#     if n > 1 and n % 2 == 1:
#         return 2*F(n-2)
# print(F(26))

# from functools import *
#
# # граничное значение
# a = list(map(int, str(2 ** 63 - 1)))
# @cache
# def f(s, l, fl):
#     # если последовательность нужной длины, проверяем, что сумма нам подходит,
#     # и выходим из рекурсии.
#     if l == 0:
#         return s == 159
#     # проверяем ограниченные подпоследовательности большей длины
#     return sum(f(s + x, l - 1, fl and (x == a[-l])) for x in range([10, a[-l] + 1][fl]))
#
# # ответ - количество ограниченных последовательностей необходимой длины
# print(f(0, len(a), 1))