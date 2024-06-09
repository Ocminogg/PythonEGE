# docum = open('28132.txt').readline()
# docum = docum.split(' ')
# Varhive = int(docum[0])
# Users = int(docum[1])
# docum = open('26 (1).txt').readlines()
# docum.remove(docum[0])
#
# print(docum)
#
# for i in range(len(docum)):
#     docum[i] = int(docum[i])
#
# print(docum)
# docum.sort()
# print(docum)
#
# UsersV = 0
# count = 0
# for i in docum:
#     if UsersV > Varhive:
#         count -= 1
#         UsersV = UsersV - int(docum[count])
#         print(docum[count])
#
#         print(count)
#         print(UsersV)
#         break
#     else:
#         UsersV += i
#         count += 1
#
# UsersV = UsersV - int(docum[count-1])
# zapas = Varhive - UsersV
# print("Конец")
# print(docum[count])
# print(UsersV)
# print(zapas)
# # print(X)
# MAX = 0
# for i in docum:
#     if (i <= zapas) and (i > MAX):
#         MAX = i
#     elif i > zapas:
#         break
# print("Ответ")
# print(MAX)
# print(count)
#
# # A = [754,234,11,23,3543,4]
# # print(A[-6])

# o=[int(i)for i in open('inf_22_10_20_26.txt')]
# l,k=[int(i)if 50<i<512else 0 for i in o],[]
# for i in range(len(o)):
#  for i in range(519):o.remove(o[i])if 50<o[i]<512else 0
# for i in l:k.append(i*.75)
# print(round(sum(o+k))-1740,max(l))

# docum = open('26.txt').readline()
# docum = docum.split(' ')
# CountGruzov = int(docum[0])
# VolumeCar = int(docum[1])
# docum = open('26.txt').readlines()
# docum.remove(docum[0])
#
# print(docum)
#
# for i in range(len(docum)):
#     docum[i] = int(docum[i])
#
# print(docum)
# docum.sort()
# print(docum)
#
# Zagruzili = 0
#
# for weight in docum:
#     if 200 <= weight and weight <= 210:
#         Zagruzili += weight
# for weight in docum:
#     if 200 <= weight and weight <= 210:
#         docum.remove(weight)
# print(docum)
# print(Zagruzili)

# Egor
# docum = open('26.txt').readline()
# docum = docum.split(' ')
# TovaraNaSklade = int(docum[0])
# Budget = int(docum[1])
#
# docum = open('26.txt').readlines()
# docum.remove(docum[0])
#
# # print(docum)
# MASSIV_A = []
# MASSIV_B = []
#
# for i in range(len(docum)):
#     docum[i] = docum[i].split(' ', 3)
#     docum[i][0] = int(docum[i][0])
#     docum[i][1] = int(docum[i][1])
#     del docum[i][3]
#     if docum[i][2] == "B":
#         MASSIV_B.append(docum[i])
#     if docum[i][2] == "A":
#         MASSIV_A.append(docum[i])
# # print(docum)
# # print(MASSIV_A)
# # print(MASSIV_B)
#
# MASSIV_A.sort()
# MASSIV_B.sort()
# # print(MASSIV_A)
#
# zatraty = 0
# price = 0
# for i in range(len(MASSIV_A)):
#     price = MASSIV_A[i][0]
#     kolvo = MASSIV_A[i][1]
#     zatraty += price * kolvo
# #     if zatraty > Budget:
# #         print("Первышен бюджет")
# #         print(zatraty)
# #         break
# # ostatok = Budget - zatraty
# # print(ostatok)
#
# countB = 0
# for i in range(len(MASSIV_B)):
#     price = MASSIV_B[i][0]
#     kolvo = MASSIV_B[i][1]
#
#     for j in range(kolvo):
#         zatraty += price
#         countB += 1
#         if zatraty > Budget:
#             break
#     if zatraty > Budget:
#         zatraty -= price
#         countB -= 1
#         print("Затраты")
#         print(zatraty)
#         print("Остаток")
#         print(Budget - zatraty)
#         print("Кол-во товара B")
#         print(countB)
#         break

# docum.sort()
# print(docum)

# docum = open('28132.txt').readline()
# docum = docum.split(' ')
# Varhive = int(docum[0])
# Users = int(docum[1])
# docum = open('28132.txt').readlines()
# docum.remove(docum[0])
#
# print(docum)
#
# for i in range(len(docum)):
#     docum[i] = int(docum[i])
#
# print(docum)
# docum.sort()
# print(docum)
#
# UsersV = 0
# count = 0
# for i in docum:
#     if UsersV <= Varhive:
#         UsersV += i
#         count += 1
#     else:
#         count -= 1
#         UsersV = UsersV - int(docum[count])
#         print(docum[count])
#         print(count)
#         print(UsersV)
#         break
#
# UsersV = UsersV - int(docum[count-1])
# zapas = Varhive - UsersV
# print("Конец")
# print(docum[count - 1])
# print(UsersV)
# print(zapas)
# MAX = 0
# for i in docum:
#     if (i <= zapas) and (i > MAX):
#         MAX = i
#     elif i > zapas:
#         break
# print("Ответ")
# print(MAX)
# print(count)

# f = open('28132.txt')
# data = f.readlines()
# s = data[0].split()
# s = int(s[0])
# del (data[0])  # первая строка больше не нужна, удаляем ее
# for i in range(0, len(data)):
#     data[i] = int(data[i])
# data = sorted(data)
# summa = 0
# for count in range(0, len(data)):
#     if summa + data[count] > s: break
#     summa += data[count]
# print(count)
# zapas = s - summa
# print("summa " + str(summa))
# print("zapas " + str(zapas))
# print("data[count] " + str(data[count]))
# for i in range(0, len(data)):
#     if data[i] - data[count - 1] <= zapas:
#         itog = data[i]
# print(itog)




# docum = open('26 (1).txt').readline()
# docum = docum.split(' ')
# print(docum)
# budget = int(docum[1])
#
# docum = open('26 (1).txt').readlines()
# docum.remove(docum[0])
# print(docum)
# A = []
# B = []
# for tovar in docum:
#     T = tovar.split(' ')
#     T[0] = int(T[0])
#     if T[1] == 'A\n':
#         A.append(T)
#     elif T[1] == 'B\n':
#         B.append(T)
#
# A.sort()
# B.sort()
# print(A)
# print(B)
# zatraty = 0
# count = 0
# for i in range(len(B)):
#     zatraty += B[i][0]
#     count += 1
#     if zatraty > budget:
#         zatraty -= B[i][0]
#         count -= 1
#         break
# print(budget - zatraty)
# print(count)

#Egor
# docum = open("inf_22_10_20_26.txt").readlines()
# docum.remove(docum[0])
#
# for i in range(len(docum)):
#     docum[i] = int(docum[i])
# print(docum)
# SUM = 0
#
# count = 0
# for i in range(len(docum)):
#     if docum[i] <= 100:
#         SUM += docum[i]
#         docum[i] = 0
#         count += 1
# print(docum)
#
# for i in range(count):
#     docum.remove(0)
# print(docum)
#
# docum.sort()
# print(docum)
#
# Length = len(docum)
# Length = Length // 2
# print(Length)
# print("Макс число со скидкой " + str(docum[Length - 1]))
# SUMskidka = 0
# for i in range(len(docum)):
#     if i <= Length-1:
#         SUMskidka += docum[i]
#     else:
#         SUM += docum[i]
# print(SUM + SUMskidka * 0.7)
# print(round(SUM + SUMskidka * 0.7))




# docum = open("26.txt").readlines()
# docum.remove(docum[0])
# print(docum)

# for i in range(len(docum)):
#     docum[i] = docum[i].split(" ")
#     docum[i][0] = int(docum[i][0])
#     docum[i][1] = int(docum[i][1])
# print(docum)

# print(docum)
# print(max(docum))
# print(docum.index(max(docum)))
# docum.remove(max(docum))
# print(max(docum))
# print(docum[2861])

# DocumSort = []
# while len(docum) != 0:
#     DocumSort.append(max(docum))
#     docum.remove(max(docum))
# print(DocumSort)
#
# first = [0,0]
# second = [0,0]
# third = [0,0]
# z = []
# # print(first,second,third)
# for i in range(len(DocumSort)):
#     first = [DocumSort[i][0],DocumSort[i][1] - 1] #Свободное
#     second = [DocumSort[i][0], DocumSort[i][1] - 2] #Свободное
#     third = [DocumSort[i][0], DocumSort[i][1] - 3] #Занятое
#     # print(first,second,third)
#     if (first not in DocumSort) and (second not in DocumSort) and (third in DocumSort):
#         print(second)
#         break
#     else:
#         continue

docum = open("26.txt").readlines()
docum.remove(docum[0])
for i in range(len(docum)):
    docum[i] = docum[i].split()
    docum[i][0] = int(docum[i][0])
    docum[i][1] = int(docum[i][1])
    # if docum[i][0] == 100000:
    #     print(docum[i])
docum = sorted(docum)
print(docum)
ArrayByLine = []

# f = open('26.txt').readlines()[1:]
# Sl = {i: [] for i in range(1, 10 ** 5 + 1)}
#
# for i in f:
#     ind, v = map(int, i.split())
#     Sl[ind] += [v]
#
#
# def func(v):
#     st = ''
#     for x, y in zip(v, v[1:]):
#         st += '*' if x + 1 == y else '* '
#     return len([1 for s in (st + '*').split() if len(s) >= 3])
#
#
# Sl = {i: func(sorted(set(v))) for i, v in Sl.items()}
# print((t := max(Sl.values())), \
#       list(Sl.keys())[::-1][list(Sl.values())[::-1].index(t)])
