# import math
# count = 0
# DEL = []
# for i in range(201455,201471):
#     # count = 0
#     DEL = []
#     for d in range(1,round(i**(0.5))):
#         if (i % d) == 0:
#             # count += 1
#             DEL.append(d)
#             DEL.append(i//d)
#             # print(DEL)
#         if len(DEL) > 4:
#             break
#     if len(DEL) == 4:
#         print(DEL)






# count = 0
# docum = open('242424.txt').readline()
# print(docum)
# DICT = {"A": 0,"B": 0}
# bukva = ""
# for i in range(len(docum) - 2):
#     if (docum[i] == docum[i+1]):
#         bukva = docum[i+2]
#         if not(DICT.get(bukva)):
#             DICT[docum[i+2]] = 1
#         else:
#             DICT[docum[i+2]] += 1
# MAXcount = 0
#
# for i in DICT:
#     if MAXcount < DICT.get(i):
#         MAXcount = DICT.get(i)
#         bukva = i
# print(bukva)


# count = 1
# docum = open('24_demo.txt').readline()
# COUNT = []
# L = 0
# for i in range(1, len(docum)):
#     if docum[i] != docum[i - 1]:
#         count += 1
#     elif L < count:
#         L = count
#         count = 1
#     else:
#         count = 1
# print(L)

# count = 0
# docum = open('zadanie24_1.txt').readline()
# MAXCOUNT = []
# i = 0
# while i != len(docum):
#     first = docum[i]
#     if i + 1 != len(docum):
#         second = docum[i + 1]
#     else:
#         second = ""
#     if ((first + second) == "AB"):
#         count += 2
#         i += 2
#     elif ((first) == "A"):
#         count += 1
#         i += 1
#         MAXCOUNT.append(count)
#         count = 0
#     else:
#         MAXCOUNT.append(count)
#         i += 1
#         count = 0
#
# print(max(MAXCOUNT))


# for i in range(len(docum)):
#     if (i == len(docum)-1):
#         break
#     elif (docum[i] != docum[i+1]):
#         count += 1
#     else:
#         COUNT.append(count)
#         count = 1
# print(max(COUNT))

# count = 0
# docum = open('24 (1).txt').readlines()
# # print(docum[3])
# strN = ""
# countN = 10000
# for i in docum:
#     if (i.count("N") < countN):
#         countN = i.count("N")
#         strN = i
# print(strN)
# bukva = ""
# countLetter = 0
# for i in strN:
#     if(strN.count(i) > countLetter):
#         countLetter = strN.count(i)
#         bukva = i
# print(bukva)


# docum = open('inf_22_10_20_24.txt').readlines()
# # print(docum)
# Count = 0
# for i in range(0, len(docum)):
#     if (docum[i].count("A") > docum[i].count("E")):
#         Count += 1
# print(Count)

# count = 0
# MAXcount = 0
# i = 0
# propusk = ""
# propusk1 = ""
# propusk2 = ""
# docum = open('24.txt').readline()
# while i != (len(docum) - 1):
#     if i < len(docum) - 2:
#         propusk = docum[i] + docum[i + 1] + docum[i + 2]
#         if i > 0:
#             propusk1 = docum[i - 1] + docum[i] + docum[i + 1]
#         if i > 1:
#             propusk2 = docum[i - 2] + docum[i - 1] + docum[i]
#     if (("A" in propusk) and ("B" in propusk) and ("C" in propusk)) or (("A" in propusk1) and ("B" in propusk1) and ("C" in propusk1)) or (("A" in propusk2) and ("B" in propusk2) and ("C" in propusk2)) :
#         MAXcount = max(MAXcount,count)
#         count = 0
#         i += 1
#     else:
#         count += 1
#         i += 1
# print(MAXcount)

# docum = open("zadanie24_1.txt").readline()
# count = 0
# MAXcount = 0
# for bukva in docum:
#     if bukva == "A":
#         count += 1
#         MAXcount = max(MAXcount,count)
#     else:
#         count = 0
# print(MAXcount)

# docum = open("zadanie24_1.txt").readline()
# count = 0
# MAXcount = 0
# for bukva in docum:
#     if bukva == "A":
#         count +=1
#         MAXcount = max(MAXcount,count)
#     else:
#         count = 0
# print(MAXcount)

# word = ''
# summ = 0
# def is_prime(n):
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n ** 0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# for z in range(10 ** 9):
#     for v in range(10):
#         for z1 in range(10 ** 9):
#             word = '7' + str(z) + '53' + str(v) + '3' + str(z1) + '1'
#             for i in word:
#                 summ += int(i)
#             if int(word) % 2627 == 0 and is_prime(summ):
#                 print(word, int(word) // 2627)

file = open('24.txt').readline()
count = 0
maxcount = 0
gl = ['A', 'O']
sgl = ['C', 'D', 'F']
for i in range(len(file)):
    if (file[i] in gl) and (file[i + 1] in gl) and (file[i + 2] in sgl):
        count += 0
    elif (file[i] in gl) and (file[i - 1] in gl) and (file[i + 1] in sgl):
        count += 0
    elif (file[i] in sgl) and (file[i - 1] in gl) and (file[i - 2] in gl):
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)