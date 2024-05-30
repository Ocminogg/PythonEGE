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