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

docum = open("C:\\PythonEGE\\Входящие данные\\17.txt").readlines()
count = 0
MAXPara = 0
for i in range(len(docum)):
    docum[i] = int(docum[i])

for i in range(len(docum)):
    for j in range(i+1,len(docum)):
        a1 = docum[i]
        a2 = docum[j]
        if (a1 - a2) % 80 == 0:
            count += 1
            MAXPara = max(MAXPara,(a1 - a2))
print(count, MAXPara)