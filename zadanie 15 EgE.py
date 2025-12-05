# for A in range(10000):
#     Flag = True
#     for x in range(10000):
#         if (((x & 5160 > 0) or (x & 3650 > 0)) <= ((x & 9545 == 0) <= (x & A > 0))) == 0:
#             Flag = False
#             break
#     if Flag:
#         print(A)
#         break

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
# for i in range(25, 51):
#     P.append(i)
# for i in range(32, 48):
#     Q.append(i)
# ListCount = []
#
# for x1 in range(0, 60):
#     for y in range(x1+1, 60):
#         A = [i for i in range(x1, y)]
#         Flag = True
#         for x in range(0, 101):
#             if (((not (x in A)) <= (x in P)) <= ((x in A) <= (x in Q))) == 0:
#                 Flag = False
#         if Flag:
#             ListCount.append(len(A))
# print(ListCount)
# print(max(ListCount) - 1)

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
#     k = True
#     for x in range(300):
#         for y in range(300):
#             if ((x * y < A) or (x < y) or (x >= 12)) == 0:
#                 k = False
#                 break
#     if k == True:
#         print(A)
#         break


# for A in range(128):
#     B = True
#     for x in range(128):
#         if ((x & 105 == 0) <= ((x&12!=0) or (x&A!=0)))==0:
#             B=False
#     if B:
#         print(A)
#         break

# for A in range(127):
#     B = True
#     for x in range(127):
#         B = B and (((x & 105 != 0) or (x & 58 == 0) or (x & A != 0)))
#     if B:
#         print(A)
#         break
# P = []
# for i in range(17,41):
#     P.append(i)
# Q = []
# for i in range(20,58):
#     Q.append(i)
#
# Array_A = []
#
# for A in range(0,100):
#     flag = True
#     for x in range(0,100):
#         if (not(x == A) <= (((x in P) and (x in Q)) <= (x == A))) == 0:
#             flag = False
#             break
#     if flag == True:
#         Array_A.append(A)
# print(Array_A)
# print(len(Array_A) - 1)

# #КОД с РЕШУ ЕГЭ
# P = [i for i in range(25, 51)]
# Q = [i for i in range(32, 48)]
# m = 0
# for Amin in range(0, 60):
#     for Amax in range(Amin + 1, 60):
#         check = 1
#         A = [i for i in range(Amin, Amax)]
#         for x in range(0, 101):
#             f = ((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))
#             if not f:
#                 check = 0
#                 break
#         if check == 1:
#             m = max(m,Amax - Amin)
# print(m - 1)
# #КОД с РЕШУ ЕГЭ
# list = []
# P = []
# for i in range(30,46):
#     P.append(i)
# Q = []
# for i in range(40,56):
#     Q.append(i)
# # R = []
# # for i in range(5,16):
# #     R.append(i)
#
# for Amin in range(1, 56):
#     for Amax in range(Amin + 1, 57):
#         A = [i for i in range(Amin, Amax)]
#         flag = True
#         for x in range(1, 100):
#             if ((not(x in A)) <= (not(x in P)) and ((x in Q)) <= ((x in A))) == 0:
#                 flag = False
#                 break
#         if flag == True:
#             print(A)
#             m = Amax - Amin
#             list.append(m)
# print(min(list) - 1)

# testList = []
# list = []
# P = [i for i in range(17, 41)]
# Q = [i for i in range(20, 58)]
# for Amin in range(1, 100):
#     for Amax in range(Amin + 1, 100):
#         check = 1
#         A = [i for i in range(Amin, Amax)]
#         for x in range(-100, 100):
#             f = (not(x in A)) <= ((((x in P) and (x in Q)) <= (x in A)))
#             if not f:
#                 check = 0
#                 break
#         if check == 1:
#             m = Amax - Amin
#             testList.append(A)
#             list.append(m)
# print(min(list)-1)

# P = []
# for i in range(3,39):
#     P.append(i)
# Q = []
# for i in range(21,58):
#     Q.append(i)
#
# A = []
# for i in range(38,58):
#     A.append(i)
#
# for x in range(1,90):
#     flag = True
#     if ((x in Q) <= (x in P)) <= (not (x in A)):
#         flag = True
#     else:
#         flag = False
#         break
#
# if flag == True:
#     print(A)
#     print(len(A))

# for A in range(1,90):
#     flag = True
#     for x in range(1,90):
#         if (x in P) <= (((x in Q) and not(x == A)) <= (not(x in P))):
#             flag = True
#         else:
#             flag = False
#             break
#     if flag == True:
#         print(A)

# k = 0
# for A in range(13,22):
#     k = 0
#     for m in range(50):
#         for n in range(50):
#             if ((2*m + 3*n) > 40) or ((m < A) and (n <= A)):
#                 k += 1
#     if k == 50*50:
#         print(A)

# P = range(160653, 428792)
# Q = range(265386, 776116)
# R = range(357752, 897168)
# A = [int(i) for i in range(160000, 900000)]
# for x in range(900000):
#     if ((not(x in A)) <= (((x in P) == (x in Q)) <= ((x in R) == (x in Q)))) == 0:
#         A = A[1:]
#     else:
#         # print(A)
#         print(len(A))
#         break

# P = range(160653, 428792)
# Q = range(265386, 776116)
# R = range(357752, 897168)
# A = [i for i in range(0, 900000)]
# for startA in range(0, 900000):
#     for endA in range(1, 900000):
#         A = [i for i in range(startA, endA)]
#         Flag = True
#         for x in range(900000):
#             if ((not (x in A)) <= (((x in P) == (x in Q)) <= ((x in R) == (x in Q)))) == 0:
#                 Flag = False
#                 break
#         if Flag:
#             print(len(A))
# for A in range(900000):
#     Flag = True
#     for x in range(900000):
#         if ((not (x == A)) <= (((x in P) == (x in Q)) <= ((x in R) == (x in Q)))) == 0:
#             Flag = False
#             break
#     if Flag:
#         print(A)

# P = range(160653, 428792)
# Q = range(265386, 776116)
# R = range(357752, 897168)
# MassivA = []
# MassivLenA = []
# for Ax in range(100000,897169):
#     for Ay in range(100001,897169):
#         A = [i for i in range(Ax, Ay)]
#         flag = True
#         for x in range(-30,100):
#             if ((not (x in A)) <= (((x in P) == (x in Q)) <= ((x in R) == (x in Q)))) == 0:
#                 flag = False
#                 break
#         if flag:
#             MassivA.append(A)
#             MassivLenA.append(len(A))
# for elem in MassivA:
#     print(elem, len(elem) - 1)

P = 153697, 780411
Q = 275071, 904082
R = 722050, 984086

def f(x):
    return ((P[0] <= x <= P[1]) == (Q[0] <= x <= Q[1])) <= ((R[0] <= x <= R[1]) == (Q[0] <= x <= Q[1]))

bad = [x for x in range(P[0], R[1] + 1) if not f(x)]
print(max(bad) - min(bad))
