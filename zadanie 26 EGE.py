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

docum = open('26.txt').readline()
docum = docum.split(' ')
TovaraNaSklade = int(docum[0])
Money = int(docum[1])

docum = open('26.txt').readlines()
docum.remove(docum[0])

print(docum)
MASSIV_A = []
MASSIV_B = []
for i in range(len(docum)):
    docum[i] = docum[i].split(' ', 3)
    docum[i][0] = int(docum[i][0])
    docum[i][1] = int(docum[i][1])
    del docum[i][3]
    if docum[i][2] == "B":
        MASSIV_B.append(docum[i])
    if docum[i][2] == "A":
        MASSIV_A.append(docum[i])
print(docum)
print(MASSIV_A)
print(MASSIV_B)

MASSIV_A.sort()
print(MASSIV_A)
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