# for A in range(0,128,1):
#     Flag = True
#     for x in range(128):
#         if ((x & 77 != 0) <= ((x & 12 == 0) <= (x & A != 0))) == 1:
#             Flag = True
#         else:
#             Flag = False
#             break
#     if Flag == True:
#         print(A)
#         break

# P = []
# Q = []
# A = []
# for i in range(5, 31):
#     P.append(i)
# for i in range(14, 24):
#     Q.append(i)
#
# for a in range(60):
#     Flag = True
#     for x in range(64):
#         if ((x in P) == (x in Q)) <= (not(x == a)):
#             Flag = True
#         else:
#             Flag = False
#             break
#     if Flag == True:
#         A.append(a)
# print(A)
#

# p=[int(i) for i in range(10,30)]
# q=[int(i) for i in range(13,19)]
# a=[int(i) for i in range(10,30)]
# for x in range(1,100):
#     if not(((x in a)<=(x in p)) or(x in q)):
#         a.remove(x)
# print(len(a)-1)

# MAX = 0
# for A in range(1, 100):
#     Flag = True
#     for x in range(500):
#         if (not(x % A == 0)) <= ((x % 6 == 0) <= (not(x % 4 == 0))):
#             Flag = True
#         else:
#             Flag = False
#             break
#     if Flag == True:
#         if A>=MAX:
#             MAX = A
#             print(MAX)

# for A in range(30):
#     Flag = True
#     for x in range(100):
#         if Flag == False:
#             break
#         for y in range(100):
#             if ((5 * x + 3 * y) != 60) or ((A > x) and (A > y)):
#                 Flag = True
#             else:
#                 Flag = False
#                 break
#     if Flag == True:
#         print(A)
#         break

# for a in range(0, 300):
#     k = 0
#     for x in range(0, 300):
#         for y in range(0, 300):
#             if (5*x + 3*y != 60) or ((a > x) and (a > y)):
#                 k += 1
#     if k == 90_000:
#         print(a)
#         break
# minA = -100000
# minB = -100000
# for a in range(-100, 100):
#     for b in range(a, 100):
#         Flag = True
#         for x in range(-100, 100):
#             if ((a<=x<=b) <= (x * x <= 100)) and ((x * x <= 64) <= (a<=x<=b)):
#                 Flag = True
#             else:
#                 Flag = False
#                 break
#
#         if Flag:
#             # a = max(minA, a)
#             # b = max(minB, b)
#             print(a,b)

# for a in range(-30, 30):
#     Flag = True
#     for x in range(-30, 30):
#         if ((x == a) <= (x * x <= 100)) and ((x * x <= 64) <= (x == a)):
#             Flag = True
#         else:
#             Flag = False
#             break
#     if Flag:
#         print(a)

# for a in range(300, 1, -1):
#     k = 0
#     for x in range(0, 300):
#         for y in range(0, 300):
#             if ((x <= 9) <= (x * x <= a)) and ((y*y <= a) <= (y <= 9)):
#                 k += 1
#     if k == 90_000:
#         print(a)
#         break

# Не работает 10 номер из решу ЕГЭ
# for a in range(-7, 20, 1):
#     Flag = True
#     for x in range(-7, 20):
#         for y in range(-7, 20):
#             if ((x == a) <= (x * x <= 81)) and ((y * y <= 36) <= (y <= a)):
#                 Flag = True
#             else:
#                 Flag = False
#                 break
#     if Flag:
#         print(a)


# a = set()
# def f(x,y,a):
#     return ((x in a) <= (x**2 <= 81)) and ((y**2 <= 36) <= (y in a))
#
# for x in range(-20,20):
#     for y in range(-20, 20):
#         if not f(x,y,a):
#             a.add(x)
# print(a)

# for a in range(0, 125, 1):
#     Flag = True
#     for x in range(0, 100):
#         if Flag:
#             for y in range(0, 100):
#                 if (x * y < a) or (x < y) or (x >= 12):
#                     Flag = True
#                 else:
#                     Flag = False
#                     break
#         else:
#             break
#     if Flag:
#         print(a)
#         break

# for A in range(300):
#     k = 0
#     for x in range(300):
#         for y in range(300):
#             if (x * y < A) or (x < y) or (x >= 12):
#                 k += 1
#     if k == 90_000:
#         print(A)
#         break

# for A in range(50):
#     flag = True
#     for x in range(50):
#         if ((x & 39)==0) or (((x & 11) == 0) <= ((x & A) != 0)):
#             flag = True
#         else:
#             flag = False
#             break
#     if flag == True:
#         print(A)
#         break

# P = []
# for i in range(10,30):
#     P.append(i)
# Q = []
# for i in range(13,19):
#     Q.append(i)
#
# for A in range(0,40):
#     flag = True
#     for x in range(0,40):
#         if ((x == A) <= (x in P)) or (x in Q):
#             flag = True
#         else:
#             flag = False
#             break
#     if flag == True:
#         print(A)

P = []
for i in range(20,51):
    P.append(i)
Q = []
for i in range(30,66):
    Q.append(i)
# A = []
# for i in range(30,51):
#     A.append(i)

# flag = True
# for x in range(20,70):
#     if (not(x in A)) <= ((x in P) <= (not (x in Q))):
#         flag = True
#     else:
#         flag = False
#         break
# if flag == True:
#     print(A)

for A in range(20,70):
    flag = True
    for x in range(20,70):
        if (not(x == A)) <= ((x in P) <= (not (x in Q))):
            flag = True
        else:
            flag = False
            break
    if flag == True:
        print(A)