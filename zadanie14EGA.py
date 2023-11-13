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

for x in '0123456789A':
    for y in '0123456789A':
        t = int( x + '341' + y, 11) + int('56' + x + '1' + y, 19)
        if t % 305 == 0:
            print(t // 305)
            break



