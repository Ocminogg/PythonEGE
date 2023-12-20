# count = 1
# docum = open('24_demo.txt').readline()
# # print(docum)
# MAXcount = 0
# for i in range(1, len(docum)):
#     if (docum[i] != docum[i-1]):
#         count += 1
#     else:
#         MAXcount = max(count,MAXcount)
#         count = 1
# print(MAXcount)

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

count = 0
MAXcount = 0
i = 0
propusk = ""
propusk1 = ""
propusk2 = ""
docum = open('24.txt').readline()
while i != (len(docum) - 1):
    if i < len(docum) - 2:
        propusk = docum[i] + docum[i + 1] + docum[i + 2]
        if i > 0:
            propusk1 = docum[i - 1] + docum[i] + docum[i + 1]
        if i > 1:
            propusk2 = docum[i - 2] + docum[i - 1] + docum[i]
    if (("A" in propusk) and ("B" in propusk) and ("C" in propusk)) or (("A" in propusk1) and ("B" in propusk1) and ("C" in propusk1)) or (("A" in propusk2) and ("B" in propusk2) and ("C" in propusk2)) :
        MAXcount = max(MAXcount,count)
        count = 0
        i += 1
    else:
        count += 1
        i += 1
print(MAXcount)