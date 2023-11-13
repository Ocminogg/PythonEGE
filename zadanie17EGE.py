count = 0
MAXSUM = -1000000
SUM = 0
docum = open('17.txt').readlines()
print (docum)

# x = docum.readlines()
# print(x)
# print(int(x[3]))
#
# l = [int(i) for i in docum]
# print(l)

for i in range(len(docum)):
    docum[i] = int(docum[i])
print(docum)
# l = []
# for element in docum:
#     l.append(int(element))
# print(l)

for i in range(len(docum)):
    for j in range(i+1, len(docum)):
        if ((docum[i] + docum[j]) % 9 ) == 0:
            count += 1
            MAXSUM = max(MAXSUM,docum[i] + docum[j])
print(f"Максимальная сумма:{MAXSUM} \nКоличество пар элементов {count} ")
print(MAXSUM, count)




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
