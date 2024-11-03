# import sys
# sys.setrecursionlimit(10**9)
# def F(a,b):
#     if b == 0:
#         return a
#     if a >= b > 0:
#         return F(a-b,b)
#     if a < b:
#         return F(b,a)
# count = 0
# for n in range(123456795,1234567889):
#     if n % 14 == 0:
#         continue
#     if F(n,14) == 1:
#         count += 1
#         print(count)
#
# print(count)

# a_2 = len(range(123456796, 1234567889, 2)) # привет
# a_7 = len(range(123456802, 1234567889, 7))
# a_14 = len(range(123456802, 1234567889, 14))
# print(len(range(123456795, 1234567888)) - a_2 - a_7 + a_14)


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

# import sys
# sys.setrecursionlimit(10**6)
# def F(n):
#     if n < 11:
#         return 10
#     else:
#         return n + F(n - 1)
# print(F(2124) - F(2122))
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

from functools import *


# def F(n):
#     if n < 10:
#         return n
#     if n >= 10:
#         return F(n%10) + F(n // 10)
# count = 0
# x = 0
# while F(x) != 159:
#     x += 1
# print(x)

# print(F(int("60" + 16 *"9")))
# for x in range(1,2**63):
#     if F(x) == 159:
#         count += 1
# print(count)


# from functools import *
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

# def F(n):
#     if n <= 1:
#         return 0
#     if n > 1 and n % 2 == 1:
#         return F(n - 1) + 3 * n**2
#     if n > 1 and n % 2 == 0:
#         return n/2 + F(n-1) + 2
# # n = 0
# # while F(n) != 11:
# #     n += 1
# print(F(49))

# def F(n):
#     if n > 10**6:
#         return n
#     if n <= 10 ** 6:
#         return n + F(2 * n)
# def G(n):
#     return F(n) / n
#
# G = G(1000)
#
# # for i in range(1,2000):
#
#
# print(len([1 for i in range(1, 2000) if (F(i) / i) == G]))

def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 2 == 0:
        return (4*n - F(n-3)) // 8
    elif n > 2 and n % 2 == 1:
        return (4*n - F(n-1) + F(n-2)) // 8

print(F(52) - F(38))
