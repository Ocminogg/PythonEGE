# for x in '012345678':
#     for y in '012345678':
#         t = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
#         if t % 61 == 0:
#             print(t // 61)
#             break


# for x in '0123456789ABCDE':
#     t = int('123' + x + '5', 15) + int('1' + x + '233', 15)
#     if t % 14 == 0:
#         print(t//14)
#         break


# S = min(result_search)
# S = S//61
# print(S)
#
# r = int('AF24', 16)
# print(r)

# E = False
# T = ''
# S = 49**10 + 7**20 - 49
# while S != 0:
#     T = T + str(S % 7)
#     S = S // 7
# print(T.count("6"))

# print(bin(4**511 + 2**511 - 511).count("1"))

# for x in range(5):
#     print(x)

# for x in '0123456789ABC':
#     for y in '0123456789ABC':
#         t = int("8" + x + "78" + y, 13) + int('79' + x + y + '7', 18)
#         if t % 9 == 0:
#             print(t // 9)
#             break
#     if t % 9 == 0:
#         break


A = ["0","1","2","3","4","5","6","7","8",]
for x in A:
    for y in '012345678':
        if (int("88" + x + "4" + y,9) + int("7" + x + "44" + y,11)) % 61 == 0:
            print((int("88" + x + "4" + y,9) + int("7" + x + "44" + y,11)) // 61)








































