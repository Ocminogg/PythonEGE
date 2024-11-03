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

# file = open('24 (2).txt').readlines()
# minG = 100000
# bufferstroka = ''
# befferletter = 'A'
# maxi = 0
# for i in range(len(file)):
#     file[i] = file[i].replace("\n",'')
#
# for stroka in file:
#     if minG > stroka.count('G'):
#         minG = stroka.count('G')
#         bufferstroka = stroka
# print(bufferstroka, minG)
#
# for letter in bufferstroka:
#     if maxi < bufferstroka.count(letter):
#         maxi = bufferstroka.count(letter)
#         befferletter = letter
#     elif maxi == bufferstroka.count(letter) and befferletter < letter:
#         befferletter = letter
# print(maxi, befferletter)

# stroka = open('24_demo.txt').readline()
# i=0
# count = 0
# maxi = 0
# while i != len(stroka) - 2:
#     if (stroka[i] + stroka[i+1] + stroka[i+2]) == "XYZ":
#         count += 3
#         i += 3
#         maxi = max(maxi,count)
#     elif (stroka[i] + stroka[i+1]) == "XY":
#         count += 2
#         maxi = max(maxi, count)
#         count = 0
#         i += 2
#     elif (stroka[i]) == "X":
#         count += 1
#         maxi = max(maxi, count)
#         count = 0
#         i += 1
#     else:
#         count = 0
#         i += 1
# print(maxi)

# f = open("C:\\Users\\User\\Downloads\\24 (2).txt").readline()
# k = 0
# m = 0
# # f = f.replace("KL", "*")
# # print(f)
# for i in range(len(f) - 1):
#     if (f[i] + f[i+1] == 'KL') or (f[i-1] + f[i] == 'KL') or (f[i] + f[i+1] == 'LK') or (f[i-1] + f[i] == 'LK'):
#         k += 1
#         m = max(m, k)
#         k = 1
#     else:
#         k += 1
# print(m)
#
# k = 1
# mx = 0
# for i in range(1, len(f)):
#     if (f[i] == 'K' and f[i-1] == 'L') or (f[i-1] == 'K' and f[i] == 'L'):
#         k = 1
#     else:
#         k += 1
#         if k > mx:
#             mx = k
# print(mx)

# t = open("C:\\Users\\User\\Downloads\\24 (2).txt").readline().replace("LK", "L/K").replace("KL", "K/L")
# maximum = 0
# counter = 0
# for i in range(len(t)):
#     if t[i] != "/":
#         counter += 1
#     else:
#         maximum = max(maximum, counter)
#         counter = 0
# print(maximum)

# f = open('C:\\Users\\User\\Downloads\\24 (3).txt').readline()
# s = f.split('D')
# m = 0
# k = 0
# res = []
# for i in range(len(s)):
#     if s[i].count('O') != 2:
#         res.append(s[i])
# for j in res:
#     m = max(m, len(j))
# print(m)

# s = "9" * 1000
# while ("999" in s) or ("888" in s):
#     if "888" in s :
#         s = s.replace ("888", "9", 1)
#     else:
#         s = s.replace ("999", "8", 1)
# print(s)