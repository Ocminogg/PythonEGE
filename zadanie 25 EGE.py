# A = [int(i) for i in range(174457,174506)]
# DEL = []
# for number in A:
#     count = 0
#     delitel = 2
#     DEL = []
#     while number//2 >= delitel:
#         if (number % delitel) == 0:
#             count += 1
#             if (count > 2):
#                 break
#             else:
#                 DEL.append(delitel)
#         delitel += 1
#
#     if (count == 2):
#         # print(str(number) + "Число")
#         print(str(DEL[0]) + " " + str(DEL[1]))

# A = [int(i) for i in range(125256,125331)]
# DEL = []
# for number in A:
#     count = 0
#     DEL = []
#     for delitel in range(2,125331//2,2):
#         if ((number % delitel) == 0) and ((delitel % 2) == 0):
#             count += 1
#             if (count > 5):
#                 break
#             else:
#                 DEL.append(delitel)
#     if (count == 5):
#         # print(str(number) + "Число")
#         print(str(DEL[0]) + " " + str(DEL[1]) + " " + str(DEL[2])+ " " + str(DEL[3])+ " " + str(DEL[4]) + " " + str(number))



# for number in range(1000000, 2000001):
#     count = 0
#     for mnochitel in range(890, int(number ** (0.5))+1):
#         if (number % mnochitel) == 0:
#             if abs(mnochitel - (number / mnochitel)) <= 100:
#                 count+=1
#             if count==3:
#                 print(number)
#                 break



#
# for i in range(2000000, 3000001):
#     sqrti = i ** 0.5
#     k = 0
#     for j in range(1, round(sqrti) + 1):
#         if i % j == 0:
#             if (abs(i / j) - j) <= 115:
#                 k += 1
#     if k > 2: print(i)
#     k = 0

# for m in range(0, 31, 2):
#     for n in range(1, 19, 2):
#         if(200000000 <= 2 ** m * 3 ** n <= 400000000):
#             print(2 ** m * 3 ** n)



# count = 0
# i = 600001
# while count < 5:
#     halfI = i // 2
#     for j in range(2, halfI + 1):
#         if i % j == 0 and j % 10 == 7 and j != 7:
#             print(i, ' ', j)
#             count += 1
#             break
#     i += 1


# for x in range(10):
#     for y in range(10):
#         Number = "12345" + str(x) + "7" + str(y) + "8"
#         if ((int(Number) % 23) == 0):
#             print(Number, int(Number) // 23)

# def M(N):
#     for i in range(1,N):
#         if ((N%i) == 0):
#             DEL.append(i)
#     if (DEL.count() >= 5):
#         print(DEL[DEL.count() - 4])
#         return 1
#     else:
#         return 0
#
# count = 0
# while count != 5:
#     number = 460000000
#     DEL=[]
#     count += M(number)

# count = 0
# DEL = []
# for chislo in range(95632,95651):
#     count = 0
#     DEL = []
#     for delitel in range(1,chislo+1):
#         if count > 6:
#             break
#         if ((chislo % delitel) == 0) and (delitel % 2 != 0):
#             count += 1
#             DEL.append(delitel)
#     if count == 6:
#         print("\nDelitel")
#         for i in DEL:
#             print(str(i) , end = " ")

# m = []
# delitel_array = []
# count_d = 0
# for i in range(174457, 174506):
#     m.append(i)
# for i in range(len(m)):
#     for delit in range(2, m[i]):
#         if m[i] % delit == 0:
#             count_d += 1
#             delitel_array.append(delit)
#     if count_d == 2:
#         print(delitel_array)
#         # print(delitel_array[0],m[i] // delitel_array[0])
#         delitel_array.clear()
#     else:
#         delitel_array.clear()
#     count_d = 0


delitel_array = []
count_d = 0
for x in range(174457, 174506):
    for delit in range(2, x):
        if x % delit == 0:
            count_d += 1
            delitel_array.append(delit)
    if count_d == 2:
        print(sorted(delitel_array))
        delitel_array.clear()
    else:
        delitel_array.clear()
    count_d = 0
