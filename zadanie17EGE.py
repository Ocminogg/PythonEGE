# count = 0
# MAXSUM = -1000000
# SUM = 0
# docum = open('17.txt').readlines()
# # print (docum)
#
# docum = [int(i) for i in docum]
# print(docum)

# for i in range(len(docum)):
#     docum[i] = int(docum[i])
# print(docum)
#
# l = []
# for element in docum:
#     l.append(int(element))
# print(l)

# for i in range(len(docum)):
#     for j in range(i+1, len(docum)):
#         if ((docum[i] + docum[j]) % 9 ) == 0:
#             count += 1
#             MAXSUM = max(MAXSUM,docum[i] + docum[j])
# print(f"Максимальная сумма:{MAXSUM} \nКоличество пар элементов {count} ")
# print(MAXSUM, count)




# for i in l:
#     if i % 2 == 1:
#         count += 1
#         SUM += i
# sred_arifm = SUM / count
# count = 0
# for i in range(len(l)-1):
#     if (l[i] % 5 == 0 and l[i+1] < sred_arifm) or (l[i+1] % 5 == 0 and l[i] < sred_arifm):
#         count += 1
#         MAXSUM = max(l[i] + l[i+1], MAXSUM)
# print(count,MAXSUM)

# for i in range(len(l)-1):
#     if (l[i] * l[i+1]) % 3 == 0:
#         count += 1
#         MAXSUM = max(l[i] + l[i+1], MAXSUM)
# print(count)
# print(MAXSUM)

# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if (l[i] - l[j]) % 2 == 0 and ((l[i] * l[j]) % 19 == 0):
#             count += 1
#             # print(count)
#             if (l[i] + l[j]) > MAXSUM:
#                 MAXSUM = l[i] + l[j]

# count = m = 0
# f = open('17 (2).txt')
# l = [int(i) for i in f]
# for i in range(len(l) - 1):
#     for j in range(i + 1, len(l)):
#         if (l[i] + l[j]) % 2 != 0 and (l[i] * l[j]) % 5 == 0:
#             count += 1
#             m = max(m, l[i] + l[j])
# print(count, m)

# count = 0
# MAXSUM = -1000000
# SUM = 0
# docum = open('17.txt').readlines()
# # print (docum)
#
# docum = [int(i) for i in docum]
# print(docum)
#
# for i in range(1,len(docum)):
#     if str(docum[i-1])


# docum = [int(i) for i in open("107_17.txt").readlines()]
# print(docum)
# minKratnoe = 10000000
# for i in docum:
#     if i < minKratnoe and i % 21 == 0:
#         minKratnoe = i
# print(minKratnoe)
# count = 0
# MAXsum = 0
# for i in range(len(docum) - 1):
#     if docum[i] % minKratnoe == 0 or docum[i+1] % minKratnoe == 0:
#         count += 1
#         MAXsum = max(MAXsum,docum[i] + docum[i+1])
# print(count, MAXsum)


# docum = open("C:\\PythonEGE\\Входящие данные\\17.txt").readlines()
# count = 0
# MAXPara = 0
# minNumber = 1000000
# for i in range(len(docum)):
#     docum[i] = int(docum[i])
#
# # print(abs(-126) % 10)
# for num in docum:
#     if abs(num) % 10 == 3:
#         minNumber = min(minNumber,num)
#
# for i in range(len(docum) - 1):
#     a1 = docum[i]
#     a2 = docum[i+1]
#     if abs(a1) % 10 == abs(a2) % 10:
#         # if abs(a1 * a2) % 3 == 0 and abs(a1 * a2) % 9 != 0: # неверное условие
#         if (abs(a1) % 3 == 0 and abs(a2) % 3 != 0) or (abs(a2) % 3 == 0 and abs(a1) % 3 != 0):
#             if a1**2 + a2**2 <= minNumber**2:
#                 MAXPara = max(MAXPara,a1**2 + a2**2)
#                 count +=1
#         # if abs(a1) % 3 == 0 and abs(a2) % 3 != 0 and a1 ** 2 + a2 ** 2 <= minNumber ** 2:
#         #     count += 1
#         #     MAXPara = max(MAXPara, a1 ** 2 + a2 ** 2)
#         # elif abs(a2) % 3 == 0 and abs(a1) % 3 != 0 and a1 ** 2 + a2 ** 2 <= minNumber ** 2:
#         #     count += 1
#         #     MAXPara = max(MAXPara, a1 ** 2 + a2 ** 2)
# print(count, MAXPara)

# docum = [int(i) for i in open("17 (2).txt").readlines()]
# print(docum)
# sum_nechet = 0
# count_nechet = 0
# for num in docum:
#     if num % 2 == 1:
#         sum_nechet += num
#         count_nechet += 1
# avrg = sum_nechet/count_nechet
# print(avrg)
# for i in range(len(docum)):
#     if docum[i] % 5 == 0 or docum[i+1] % 5 == 0:

# docum = open("C:\\Users\\User\\Desktop\\17 (2).txt").readlines()
# for i in range(len(docum)):
#     docum[i] = int(docum[i])

# count = 0
# maxSum = 0
# docum = [int(i) for i in open("C:\\Users\\User\\Desktop\\17 (2).txt").readlines()]
# print(docum)
# for i in range(len(docum)):
#     for j in range(i+1,len(docum)):
#         if (docum[i] + docum[j]) % 9 == 0:
#             count += 1
#             maxSum = max(maxSum, docum[i] + docum[j])
# print(count, maxSum)

# docum = [int(i) for i in open("C:\\Users\\User\\Downloads\\17 (3).txt").readlines()]

# path = "C:\\Users\\User\\Downloads\\17 (3).txt"
# docum = open(path)
# print(docum)
#
# docum = docum.readlines()
# print(docum)
#
# for i in range(len(docum)):
#     docum[i] = int(docum[i])
# print(docum)
#
# count = 0
# MAXSUM = 0
#
# for i in range(len(docum)):
#     for j in range(i+1, len(docum)):
#         if docum[i] % 160 != docum[j] % 160:
#             if docum[i] % 7 == 0 or docum[j] % 7 == 0:
#                  count += 1
#                  MAXSUM = max(MAXSUM,docum[i] + docum[j])
# print(count, MAXSUM)

# for x in '0123456789ABCDE':
#     s = int(x + 'B09', 17) + int(x + '8E8', 15)
#     if s % 155 == 0:
#         print(s // 155)
#         break


# docum = open("C:\\Users\\User\\Downloads\\17 (4).txt").readlines()
#
# for i in range(len(docum)):
#     docum[i] = int(docum[i])
#
# count = 0
# SUM = 0
# for i in range(len(docum)):
#     for j in range(i+1, len(docum)):
#         if (docum[i] * docum[j]) % 34 != 0:
#             count += 1
#             SUM = max(docum[i] + docum[j], SUM)
#
# print(count, SUM)

# N = int(input())
# SUM = 0
# for i in range(N):
#     x = int(input())
#     if x % 3 == 0:
#         SUM += x
# print(SUM)

# x = 1757
# print(x % 10)

# n = int(input())
# SUM = 0
# for i in range(n):
#     x = int(input())
#     if x % 10 == 4:
#         SUM += x
# print(SUM)

# SUM = 0
# x = 1
# while x != 0:
#     x = int(input())
#     if (x % 6 == 0) and (x % 10 == 4):
#         SUM += x
# print(SUM)

# n = int(input())
# MAX = 0
# LowSpeed = "NO"
# for i in range(n):
#     x = int(input())
#     if x < 30 and LowSpeed == "NO":
#         LowSpeed = "YES"
#     MAX = max(MAX, x)
# print(MAX)
# print(LowSpeed)
#
# n = int(input())
# x = 1
# SUM = 0
# Minus = 0
# Plus = 0
# while x != 0:

# n = int(input())
# COUNT = 0
# for i in range(n):
#     x = int(input())
#     if x % 3 == 0:
#         COUNT += 1
# print(COUNT)

# print(bin(10)[2::])

# docum = [int(i) for i in open("17 (5).txt").readlines()]
# maxsum = 0
# count = 0
# for i in range(len(docum) - 1):
#     for j in range(i + 1, len(docum)):
#         num1 = docum[i]
#         num2 = docum[j]
#         d = 160
#         p = 7
#         if (num1 % d != num2 % d) and (num1 % p == 0 or num2 % p == 0):
#             count += 1
#             maxsum = max(maxsum, num1 + num2)
# print(count, maxsum)

# for i in range(len(docum)):
#     docum[i] = int(docum[i])
#
# min_sp = 0
# for i in range(len(docum)):
#     if abs(docum[i]) % 10 == 7:
#         min_sp = min(min_sp, docum[i])
#
# count = 0
# max_sum = 0
# for i in range(len(docum) - 1):
#     if ((abs(docum[i]) % 10 == 7) and (abs(docum[i+1]) % 10 != 7)) or ((abs(docum[i]) % 10 != 7) and (abs(docum[i+1]) % 10 == 7)):
#         if ((docum[i]**2 + docum[i+1]**2) < min_sp**2):
#             count += 1
#             max_sum = max(max_sum, (docum[i]**2 + docum[i+1]**2))
# print(count,max_sum)