# docum = open('28130_A.txt').readline()
# # docum = docum.split()
# count = int(docum[0])
# docum = open('28130_A.txt').readlines()
# docum.remove(docum[0])
# raznost = 10000000000
# SUM = 0
# for i in range(count):
#     para = docum[i].split()
#     ch1 = int(para[0])
#     ch2 = int(para[1])
#     if abs(ch1 - ch2) % 3 != 0:
#         raznost = min(raznost, abs(ch1 - ch2))
#     SUM += max(ch1,ch2)
#
# if SUM % 3 == 0:
#     print(SUM - raznost)
# else:
#     print(SUM)

# f = open("27-B_demo.txt")  # для файла A замените название
# s = f.readlines()
# n = int(s[0])  # количество пар
# summi = 0
# d = 10**6
# for i in range(1, n + 1):
#     x, y = map(int, s[i].split())
#     summi += max(x, y)
#     if abs(x - y) % 3 != 0:
#         d = min(d, abs(x - y))
# if summi % 3 != 0:
#     print(summi)
# else:
#     print(summi - d)


# def z():
#     from math import ceil
#     with open('27.txt') as f:
#         n , k = map(int, f.readline().split())
#         v = [int(i) for i in f][:n]
#         mix = 0
#         trashcar = 0
#         for i in v:
#             trashcar += i
#             if trashcar < 0:
#                 trashcar = 0
#             mix = max(mix, ceil(trashcar / k))
#         print(mix)
# z()

########### ДЕЛАЛИ НА УРОКЕ В ТЕТРИКЕ #################################
# docum = open("27990_B.txt").readlines()
# # print(docum)
# for i in range(len(docum)):
#     docum[i] = int(docum[i])
# # print(docum)
# N = docum[0]
# docum.remove(docum[0])
# # print(docum)
# COUNT = 0
# Count62 = 0
# Count31 = 0
# Count2 = 0
# for i in range(N):
#     if ((docum[i] % 62) == 0):
#         Count62 +=1
#         docum[i] = -1
# while -1 in docum:
#     docum.remove(-1)
# #####################################
# for i in range(len(docum)):
#     if ((docum[i] % 62) == 0):
#         print(docum[i])
# ##############################################
# COUNT = Count62 * (N-1) - Count62
# print(COUNT)
# print(len(docum))
#
# for i in range(len(docum)):
#     if ((docum[i] % 31) == 0):
#         Count31 +=1
#     elif ((docum[i] % 2) == 0):
#         Count2 +=1
# COUNT = (Count31 * Count2) + COUNT
# COUNT = Count62*(Count62 - 1)/2 + Count62*(N-Count62)+Count2*Count31
# print(COUNT)

################## Для А
# for i in range(len(docum)):
#     for j in range(i+1,len(docum)):
#         ch1 =docum[i]
#         ch2 = docum[j]
#         if ((ch1 * ch2) % 62 ) == 0:
#             COUNT +=1
#             print(COUNT)
# print(COUNT)





# path = 'D:\\TetrikaPython\\28130_B.txt' # для Windows
#
# docum = open(path).readlines()
# print(docum)
# count = 0
# docum.remove(docum[0])
# m = 80
# b = 50
# for i in range(len(docum)):
#     docum[i] = int(docum[i])
# print(docum)
#
# for i in range(len(docum)):
#     for j in range(i+1,len(docum)):
#         if (((docum[i]+docum[j]) % 80) == 0) and ((docum[i] > 50) or (docum[j] > 50)):
#             count +=1
#             print(count)
# print(count)



path = 'D:\\TetrikaPython\\27_A.txt' # для Windows

docum = open(path).readlines()
print(docum)
docum.remove(docum[0])

for i in range(len(docum)):
    docum[i] = docum[i].split(' ')
    docum[i][0] = int(docum[i][0])
    docum[i][1] = int(docum[i][1])
    docum[i][2] = int(docum[i][2])
print(docum)
SUM = 0
MINsrediMAX = docum[0]

for i in range(len(docum)):
    SUM += max(docum[i])
    if (max(MINsrediMAX) > max(docum[i])):
        MINsrediMAX = docum[i]


print(MINsrediMAX)
if (SUM % 109 == 0):
    SUM = SUM - max(MINsrediMAX) + MINsrediMAX[0]
    print(SUM)
else:
    print(SUM)