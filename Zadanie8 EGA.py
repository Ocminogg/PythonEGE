# p, o = 'левий', 0
# for i in p:
#     for u in p:
#         for y in p:
#             for t in p:
#                 for r in p:
#                     # o += 1
#                     word = i + u + y + t + r + " "
#                     index = word.find("е")
#                     if word[index + 1] != 'и' and word[0] != 'й':
#                         o += 1
#                         # print(o, i + u + y + t + r)
# print(o)

# al='МАТВЕЙ'
# k=0
# for b1 in 'МАТВЕ':
#     for b2 in al:
#         for b3 in al:
#             for b4 in al:
#                 for b5 in al:
#                     for b6 in al:
#                         s=b1+b2+b3+b4+b5+b6
#                         bb=set(s)
#                         if len(s)==len(bb) and s.count('АЕ')==0:
#                             k+=1
# print(k)

# import itertools
# alphabet = "ДЕМЬЯН"
# vol = 'ЕЯ'
# ar = itertools.permutations(alphabet) #Перестановка
# arl = []
# for i in ar:
#     arl.append(list(i))
# count = 0
# for e in arl:
#     flag = True
#     for i in range(6):
#         if (e[0] == "Ь") or (e[i] == "Ь" and e[i-1] in vol):
#             flag = False
#     if flag:
#         count += 1
# print(count)

# count = 0
# for x in range(4):
#     for y in range(4):
#         for z in range(4):
#             if (x + z > y) and x != 0:
#                 count +=1
# print(count)

# count = 0
# for x in range(7):
#     for y in range(7):
#         for z in range(7):
#             for w in range(7):
#                 if x > y and y > z and z > w:
#                     count += 1
# print(count)